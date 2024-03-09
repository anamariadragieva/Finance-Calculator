import math


LINE = "-"*80
HOME_MENU = '''\tWelcome to the investment calculator!\n \n \
    \tinvestment - to calculate the amount of interest you'll earn on your investment\n \
    \tbond       - to calculate the amount you'll have to pay on a home loan\n '''

# user can choose between investment or bond calculator
print(f"{HOME_MENU}\n\t{LINE}")

while True:
    choice = input("\tEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    if choice == "investment":
        print("\n\n\tYou've chosen to calculate the amount of interest you'll earn on your investment.")

        
        # user inputs the data needed to calculate investment
        while True:
            deposit_amount = input("\n\tEnter the amount of money you're depositing (£): ")
            if "-" in deposit_amount:
                print("\n\tThe deposit amount cannot be negative!")
            elif not deposit_amount.isnumeric():
                print("\n\tPlease use numbers only!")
            elif float(deposit_amount) == 0:
                print("\n\tThe deposit amount cannot be 0!")
            else: 
                deposit_amount = float(deposit_amount)
                break

        while True:
            interest_rate = input("\n\tEnter the interest rate (%): ")
            if "-" in interest_rate:
                print("\n\tThe interest rate cannot be negative!")
            elif not interest_rate.replace(".","",1).isnumeric():
                print("\n\tPlease use numbers only!")
            elif float(interest_rate) == 0:
                print("\n\tThe interest rate cannot be 0!")
            else: 
                interest_rate = float(interest_rate)
                break

        while True:
            years = input("\n\tEnter the number of years you'll be investing for: ")
            if "-" in years:
                print("\n\tThe years spent investing cannot be negative!")
            elif not years.isnumeric():
                print("\n\tPlease use numbers only!")
            elif int(years) == 0:
                print("\n\tThe years spent investing cannot be 0!")
            else: 
                years = int(years)
                

                # asking the user if they want the simple or compound % calculated
                while True:
                
                    interest = input("\n\tDo you want to calculate 'simple' or 'compound' interest? ").lower()

                    # calculating the simple interest using the formula: A = P *(1 + r*t)
                    if interest == "simple":
                        total_amount = deposit_amount *(1 + (interest_rate / 100)* years)
                        print(f"\n\tThe total amount earned after {years} years is £{total_amount:.2f}.\n")
                        break

                    # calculating the compound interest using the formula: A = P * math.pow((1+r),t)
                    elif interest == "compound":
                        total_amount = deposit_amount * math.pow((1 + (interest_rate / 100)), years)
                        print(f"\n\tThe total amount earned after {years} years is £{total_amount:.2f}.\n")
                        break

                    elif not interest.isalpha():
                        print("\n\tPlease type letters only!")

                    elif interest != "simple" and interest != "compound":
                        print("\n\n\tInvalid choice! Please select one of the options above.")
                break



    elif choice == "bond":
        print("\n\n\tYou've chosen to calculate the amount you'll have to pay on a home loan.")

        # user inputs the data needed to calculate monthly home loan repayment
        while True:
            house_value = input("\n\tEnter the present value of the house (£): ")
            if not house_value.replace(".", "", 1).isdigit() or float(house_value) <= 0:
                print("\n\tPlease enter a valid positive number for the house value.")
            else:
                house_value = float(house_value)
                break

        while True:
            interest_rate = input("\n\tEnter the interest rate (%): ")
            if not interest_rate.replace(".", "", 1).isdigit() or float(interest_rate) <= 0:
                print("\n\tPlease enter a valid positive number for the interest rate.")
            else:
                interest_rate = float(interest_rate)
                break

        while True:
            months = input("\n\tEnter the number of months needed to repay the bond: ")
            if not months.isdigit() or int(months) <= 0:
                print("\n\tPlease enter a valid positive integer for the number of months.")
            else:
                months = int(months)
                break


        # calculating the repayment using the formula A = (i * P) / (1 - (1 + i) ** (-n))
        repayment = (((interest_rate / 100)/ 12)* house_value)/(1 - (1 + ((interest_rate / 100)/ 12))**(-months))
        print(f"\n\tThe amount to be paid each months is £{repayment:.2f}\n")

    elif not choice.isalpha() or choice not in ["investment", "bond"]:
        print("\n\n\tInvalid choice! Please select either 'investment' or 'bond' from the options above.")
        