# collect the necessary input(principal,annual intrest rate, years)
# calculate the monthly payment
# show to the user

def main():
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years to pay back: "))
    
    monthly_interest_rate = apr/1200
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate /(1-(1 + monthly_interest_rate) ** (-number_of_months))
    
    print(f"The monthly payment for {principal} is {monthly_payment}")
    
    
main()