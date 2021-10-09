from errors import *

valid_domains = {"com", "bg", "org", "net"}

while True:
    user_email = input()

    if user_email == "End":
        break

    email_data = user_email.split('@')

    if len(email_data) == 1:
        raise MustContainAtSymbolError(f"Email must contain @")

    username, domain_data = email_data

    if len(username) <= 4:
        raise NameTooShortError(f"Name must be more than 4 characters")

    domain = domain_data.split('.')[-1]

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")







