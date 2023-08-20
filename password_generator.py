import random
import string #grab all of the lowercase and uppercase letters that exist, as well as all the nulbers or digits and special characters 

def generate_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

#combine all of the variables into one list, or large string that we are going to randoply choose from
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_critiria = False
    has_number = False
    has_special = False

    while not meets_critiria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_critiria = True
        if numbers:
            meets_critiria = has_number
        if special_characters:
            meets_critiria = meets_critiria and has_special

    return pwd

min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

pwd = generate_password(min_lenght, has_number, has_special)  # If i define min_lenght to be 10 characters, if i continue and write second parameter False , means there are no numbers , but the special_characters are accepted cause i did'nt specify third parameter
print("The generated password is: ", pwd)