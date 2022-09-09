print("Welcome to the tip calculator.\n")
total_bill=float(input("What was the total bill? "))
tip=int(input("What percentage tip would you like to give ? 10, 12, or 15? "))

num_ppl=int(input("How many people to split the bill? "))


total_bill_with_tip=total_bill+ (total_bill)* ((tip)/100)
#Can't use round function here we need to use "{:.2f}".format() instead!!!!!!!!!!
bill_with_format="{:.2f}".format(total_bill_with_tip/num_ppl)
print(f"Each person should pay : {bill_with_format}")