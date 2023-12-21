# collect email from user
# split the email using the @, the first part as useername, the second part as domain
# split domain using .

def main():
    print("Welcome to the emial slicer")
    print("")
    
    email_input = input("Input your email address: ")
    
    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")
    
main()
