monthly_income=int(input("Enter your monthly income:"))
monthly_expens=int(input("Enter your total monthly expenses:"))
monthly_saving = monthly_income - monthly_expens
ProjectedSavings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print("Your monthly savings are ",monthly_saving)
print("Projected savings after one year, with interest, is: ",ProjectedSavings)