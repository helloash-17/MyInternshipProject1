import random
import string

def generate_strong_password(length=16):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least two characters from each set
    password = (
        random.choice(uppercase_letters)
        + random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(digits)
        + random.choice(special_characters)
        + random.choice(special_characters)
    )

    # Generate the remaining characters
    password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - 8))

    # Shuffle the password characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_strong_passwords(num_passwords, length=16):
    passwords = [generate_strong_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    # Get user input for password length and number of passwords
    password_length = int(input("Enter the desired password length: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate and display strong passwords
    strong_passwords = generate_strong_passwords(num_passwords, password_length)
    print("\nGenerated Strong Passwords:")
    for i, password in enumerate(strong_passwords, start=1):
        print(f"Password {i}: {password}")
