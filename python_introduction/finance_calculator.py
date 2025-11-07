monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))
monthly_saving = monthly_income - monthly_expense
annual_interest = 0.05
projected_saving = (monthly_saving * 12) + (monthly_saving * 12 * annual_interest)
print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")