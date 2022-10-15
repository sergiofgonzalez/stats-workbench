from datetime import date, timedelta

print("== Date difference in months calculator ==")

initial_date_str = input("Enter initial date im ISO 8601 format (YYYY-MM-DD): ")
initial_date = date.fromisoformat(initial_date_str)

end_date_str = input("Enter end date im ISO 8601 format (YYYY-MM-DD): ")
end_date = date.fromisoformat(end_date_str)

delta_years = end_date.year - initial_date.year
delta_months = end_date.month - initial_date.month
delta_days = end_date.day - initial_date.day

result = delta_years * 12 + delta_months if delta_days >= 0 else delta_years * 12 + delta_months - 1

print(f"Number of months between dates={result}")
