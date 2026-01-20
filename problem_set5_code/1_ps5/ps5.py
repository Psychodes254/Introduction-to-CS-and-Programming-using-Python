from PIL import Image, ImageFont, ImageDraw
import numpy


def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    if color == 'red':
        c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
    elif color == 'green':
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
    return c


def matrix_multiply(m1, m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """
    product = numpy.matmul(m1, m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of representing pixels.

    For RGB images, each pixel is a tuple containing (R,G,B) values.
    For BW images, each pixel is an integer.

    # Note: Don't worry about determining if an image is RGB or BW.
            The PIL library functions you use will return the 
            correct pixel values for either image mode.

    Returns the list of pixels.

    Inputs:
        filename: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values 
                 in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image
                 in form L such as [60,66,72...] for BW image
    """
    # Open the image, get data and convert into a list
    with Image.open(filename) as img:
        pixels = list(img.getdata())
    
    # Return the list of pixels
    return pixels


def pix_to_img(pixels_list, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels_list: a list of pixels such as the output of
                img_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a 
              BW image, respectively
    returns:
        img: Image object made from list of pixels
    """
    # Create a new image object with the specified mode and size
    image = Image.new(mode, size)
    
    # Put the list of pixel data into the image
    image.putdata(pixels_list)
    
    # Return the Image
    return image


def filter(pixels_list, color):
    """
    pixels_list: a list of pixels in RGB form, such as
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing 
           the color deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """
    # Initialize empty list for transformed pixels
    transformed_pixels = []
    
    # Get the transformation matrix for the specified color
    transformation = make_matrix(color)
    
    # Iterate through each pixel in the input list
    for pixel in pixels_list:
        
        # Apply matrix multiplication
        mat = matrix_multiply(pixel, transformation)
    
        # Convert to integers
        result = tuple(int(x) for x in mat)
        
        # Add transformed pixel as tuple to result list
        transformed_pixels.append(result)
    
    return transformed_pixels


def extract_end_bits(num_end_bits, pixel):
    """
    Extracts the last num_end_bits of each value of a given pixel.

    example for BW pixel:
        num_end_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_end_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_end_bits: the number of end bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The num_end_bits of pixel, as an integer (BW) or tuple of integers (RGB).
    """
    # Check the integers
    if isinstance(pixel, int):
        return pixel % (2 ** num_end_bits)
    
    # Check the tuples
    if isinstance(pixel, tuple):
        return tuple(n % (2 ** num_end_bits) for n in pixel)


def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image. 
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    LSB_list = []
    
    # Load the image
    with Image.open(filename) as img:
        grayscale_img = img.convert("L")
        width, height = grayscale_img.size
    
    # Convert image → pixel list
    img_pixel_list = list(grayscale_img.getdata())
    
    # Extract the LSB from each pixel
    for pixel in img_pixel_list:
        LSB_list.append(extract_end_bits(1, pixel))
    
    # Rebuild the image
    new_img = Image.new('L', (width, height))
    
    # Scale 0→0 (black) and 1→255 (white) for visibility
    scaled_LSB = [bit * 255 for bit in LSB_list]
    
    new_img.putdata(scaled_LSB)
    
    return new_img


def reveal_color_image(filename):
    """
    Extracts the 3 LSBs for each pixel in the RGB input image. 
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    LSB_data = []
    
    # Open the image
    with Image.open(filename) as image:
        rgb_img = image.convert('RGB')
        width, height = rgb_img.size
      
    # Extract pixel data
    pixel_data = list(rgb_img.getdata())
    
    # Pixel data structure
    for (r, g, b) in pixel_data:
        # Extract LSBs per channel
        LSB_data.append(extract_end_bits(3, (r, g, b)))
    
    # Build the new pixel list by Making the hidden image visible
    new_pix_list = [(int(new_r * 255 / 7), int(new_g * 255 / 7), int(new_b * 255 / 7)) for (new_r, new_g, new_b) in LSB_data]
    
    # Rebuild the image
    rgb_img = Image.new('RGB', (width, height))
    
    rgb_img.putdata(new_pix_list)
    
    return rgb_img


def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a 
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return(reveal_bw_image(filename))
    elif im.mode == 'RGB':
        return(reveal_color_image(filename))
    else:
        raise Exception("Invalid mode %s" % im.mode)


def draw_kerb(filename, kerb):
    """
    Draws the text "kerb" onto the image located at "filename" and returns a PDF.
    Inputs:
        filename: string, input BW or RGB file
        kerb: string, your kerberos
    Output:
        Saves output image to "filename_kerb.xxx"
    """
    im = Image.open(filename)
    font = ImageFont.truetype("noto-sans-mono.ttf", 40)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), kerb, "white", font=font)
    idx = filename.find(".")
    new_filename = filename[:idx] + "_kerb" + filename[idx:]
    im.save(new_filename)
    return
