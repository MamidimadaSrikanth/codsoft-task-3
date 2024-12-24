# To generate the password
import random
import string
def generate_password(lenght,use_uppercase=True,use_lowercase=True,use_numbers=True,use_special_characters=True):
    #define characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else " "
    numbers = string.digits if use_numbers else" "
    special_characters = string.punctuation if use_special_characters else " "
    #combine all characters
    all_characters = uppercase + lowercase + numbers + special_characters
    #there is atleast one special  character
    if not all_characters:
        raise ValueError("atleast one character type must be choosen")
    # to generate password
    password = ''.join(random.choice(all_characters)for _ in range(length))
    return password
# User input
try:
    length = int(input("enter the desired password length:"))
    use_uppercase = input("include uppercaseletters?(yes/no):").strip().lower() == 'yes'
    use_lowercase = input("include lowercaseletters?(yes/no):").strip().lower() == 'yes'
    use_numbers = input("include numbers?(yes/no): ").strip().lower() == 'yes'
    use_special_characters = input("include special characters?(yes/no): ").strip().lower() == 'yes'
    # Generate and Display password
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_characters)
    print(f"generated password:{password}")
except ValueError as e:
    print(f"Error:{e}")
    
