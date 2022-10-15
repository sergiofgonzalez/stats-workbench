print("=== Monthly payment calculator")
print()

principal = float(input("Enter the loaned amount: "))
apr = float(input("Enter the APR without the '%': "))
num_years = int(input("Enter the number of years: "))

monthly_interest_rate = apr / (12 * 100)
num_months = num_years * 12
monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-num_months))

print(f"Your monthly payment for this loan is: ${round(monthly_payment, 2)}")
