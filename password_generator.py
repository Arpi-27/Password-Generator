import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    
    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all categories
    all_characters = lowercase + uppercase + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        print(f"Your generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()