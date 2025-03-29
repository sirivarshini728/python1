def get_person_details():
    """
function to read a person's details from the keyboard.
"""
    name=input("enter your name:")
    address=input("enter your address:")
    email=input("enter your email:")
    phone=input("enteryour phone number:")
    returnname,adderss,email,phone
    def print_person_details(name,address,email,phone):
        """
function to print a person's details.
"""
        print("\n---personal details---")
        print(f"name:{name}")
        print(f"address:{address}")
        print(f"email:{email}")
        print(f"phone number:{phone}")
#get details from the user
        name,address,email,phone=get_person_details()
        #print the details
        print_person_details(name,address,email,phone)
