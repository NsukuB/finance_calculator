# importing the math module for mathematical operations
import math

# Displaying options for the user to choose from
print("""investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:""")

# Input for the user's choice
choice = input()

# Case 1: Investment
if choice.lower() == 'investment':
    # Input for investment values
    amount_deposited = float(input("Enter the deposit amount: "))
    interest_rate = float(input("Enter the rate of interest: "))/100
    years_number = int(input("Enter the number of years: "))
    type_interest = input("Enter the type of interest (compound/simple): ")

    # Calculating interest based on the type selected
    if type_interest.lower() == "simple":
        total_after_interest = amount_deposited * (1 + interest_rate * years_number)
        total_after_interest = amount_deposited *(1 + interest_rate * years_number)
    elif type_interest.lower() == "compound":
        total_after_interest = amount_deposited * math.pow((1 + interest_rate), years_number)
    else:
        print("Invalid type of interest selected!")
    print("The amount after", years_number, "years is", round(total_after_interest, 2))

# Case 2: Bond
elif choice.lower() == 'bond':
    # Input for bond values
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the rate of interest: "))
    months_number = int(input("Enter the number of months for the bond: "))
    monthly_interest = (interest_rate/100) / 12
    repayment = (monthly_interest * present_value) / (1 - (1 + monthly_interest) ** (-months_number))
    print("The repayment after", months_number, "months is", round(repayment, 2))

# Invalid choice
else:
    print("Invalid choice!")