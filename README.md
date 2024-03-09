# Investment and Bond Calculator

This Python script provides a simple investment and bond calculator. Users can calculate the amount of interest they will earn on an investment or the amount they will have to pay on a home loan (bond).

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Running the Script

1. Clone the repository or download the script file `investment_bond_calculator.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where `investment_bond_calculator.py` is located.
4. Run the script using the command: `python investment_bond_calculator.py`

## How to Use

Upon running the script, you will be presented with a menu with two options: `investment` or `bond`. Follow the on-screen instructions to input the required information.

### Investment Calculator

- Calculate the amount of interest you'll earn on your investment.
- Input the following details:
  - Deposit Amount (£)
  - Interest Rate (%)
  - Number of Years

You will then be asked if you want to calculate `simple` or `compound` interest. The script will calculate and display the total amount earned after the specified number of years.

### Bond Calculator

- Calculate the amount you'll have to pay on a home loan (bond).
- Input the following details:
  - Present Value of the House (£)
  - Interest Rate (%)
  - Number of Months to Repay

The script will calculate and display the monthly repayment amount for the home loan.

## Sample Code

```python
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
            # More input validation and calculation code...

    elif choice == "bond":
        print("\n\n\tYou've chosen to calculate the amount you'll have to pay on a home loan.")
        # More input validation and calculation code...

    elif not choice.isalpha() or choice not in ["investment", "bond"]:
        print("\n\n\tInvalid choice! Please select either 'investment' or 'bond' from the options above.")
```

## Contribution

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.
