def choosing_interest_rate():
    ##############################################
    ## Get user input for initial_deposit below ##
    ##############################################
    user_input = float(input("Enter the initial deposit: "))
    
    #########################################################################
    ## Initialize other variables you need (if any) for your program below ##
    #########################################################################
    # Constant home cost
    home_cost = 800000
    
    # Down payment amount
    down_payment = home_cost * 0.25
    
    # 3 years needed for maximum time needed to reach down payment goal
    months = 36
    
    # Savings should be within $100 since hitting exact figure is challenging
    epsilon = 100
    
    # Initiate the steps that will take to accomplish the bisection search
    steps = 0
    
    # Initiate the upper bound
    upper_bound = 1
    
    # Initiate the lower bound
    lower_bound = 0
    
    # Initial midpoint
    mid_point = (upper_bound + lower_bound) / 2
    
    ##################################################################################################
    ## Determine the lowest rate of return needed to get the down payment for your dream home below ##
    ##################################################################################################
    # First check if it is possible to reach the goal with 100% interest
    if user_input * (1 + upper_bound / 12) ** months < down_payment:
        print("It is not possible to reach savings goal in 3 years!")
        
    # Start the while loop if the goal is possible
    while True:
        steps += 1
        
        # Determine the monthly rate
        monthly_rate = mid_point / 12
        
        # The compound interest formula to check saved amount
        amount_saved = user_input * (1 + monthly_rate) ** months
        
        # Break the loop if diff is lower or equal to epsilon
        if abs(amount_saved - down_payment) <= epsilon:
            break
        
        # Determine the lower or upper bound by the diff between saved amount and down payment
        if amount_saved > down_payment:
            upper_bound = mid_point
        else:
            lower_bound = mid_point
          
        # Recalculate the mid_point again
        mid_point = (upper_bound + lower_bound) / 2
            
        # Safely break the loop if steps exceeds 100
        if steps >= 100:
            break
            
    print(f"Best saving rate: {mid_point}")
    
    return steps

steps = choosing_interest_rate()

print(f"Steps in bisection search: {steps}")
    
    
    
