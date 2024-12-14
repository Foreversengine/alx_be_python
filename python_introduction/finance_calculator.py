#!/usr/bin/python3
# Prompt the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% annual interest
annual_savings = monthly_savings * 12
annual_savings_with_interest = annual_savings + (annual_savings * 0.05)

# Display the results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings, including 5% interest, are: ${annual_savings_with_interest:.2f}")