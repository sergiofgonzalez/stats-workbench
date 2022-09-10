def main():
    print("== Welcome to the email address slicer ==")
    print("")

    email_input = input("Enter your email address: ")
    [username, domain] = email_input.split("@")
    [domain_name, domain_ext] = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain Name: {domain_name}")
    print(f"Domain extension: {domain_ext}")

main()
