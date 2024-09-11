monthlyincome=int(input("Enter your monthly income:"))
monthlyexpenses=int(input("Enter your total monthly expenses:"))
monthlysavings = monthlyincome - monthlyexpenses
ProjectedSavings = monthlysavings * 12 + (monthlysavings * 12 * 0.05)
print("Your monthly savings are ",monthlysavings)
print("Projected savings after one year, with interest, is: ",ProjectedSavings)