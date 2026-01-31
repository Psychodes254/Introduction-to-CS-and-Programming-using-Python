# User inputs
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
salary_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Down payment portion 25% of home cost
portion_down_payment = 0.25

 # Annual earn return rate
annual_return = 0.05

# Initialize months
months = 0

# Initialize previous savings
total_savings = 0

# Monthly contribution
monthly_cont = (yearly_salary * portion_saved) / 12

# The target to reach the down payment
target_saving = cost_of_dream_home * portion_down_payment

# Calculate monthly rate
rate = annual_return / 12

# A loop to check if the total savings has achieved target savings, and no. of months
while total_savings < target_saving:
    total_savings += (total_savings * rate) + monthly_cont
    months += 1
    
    # Check the salary raise after every 6 months
    if months % 6 == 0:
        monthly_cont = monthly_cont * (1 + salary_raise)
   
# Print no. of months it takes
print(months)