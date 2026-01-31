# User inputs
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

# Down payment portion 25% of home cost
portion_down_payment = 0.25

 # Annual earn return rate
annual_return = 0.05

# Initialize months
months = 0

# Initialize previous month contribution
monthly_check = 0

# Monthly contribution
monthly_cont = (yearly_salary * portion_saved) / 12

# The target to reach the down payment
target_saving = cost_of_dream_home * portion_down_payment

# Calculate monthly rate
rate = annual_return / 12

# A loop to check if the target achieved, and no. of months
while monthly_check < target_saving:
    monthly_check += (monthly_check * rate) + monthly_cont
    months += 1
  
# Print no. of months it takes to achieve the target
print(months)