# ============================================================
# Password Generator
# Uses: loops, string handling, random module, string module
# ============================================================

import random
import string

# The string module gives us ready-made groups of characters:
LOWERCASE = string.ascii_lowercase      # abcdefghijklmnopqrstuvwxyz
UPPERCASE = string.ascii_uppercase      # ABCDEFGHIJKLMNOPQRSTUVWXYZ
DIGITS = string.digits                  # 0123456789
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"     # special characters

MIN_LENGTH = 8      # shorter passwords are too easy to crack
MAX_LENGTH = 64

# SystemRandom uses the operating system's secure random source.
# It is safer for passwords than the normal random functions,
# and it is still part of the "random" module.
secure_random = random.SystemRandom()


def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    """Create one password of the given length.
    Guarantees at least one character from every selected group.
    """
    # Step 1: decide which character groups are allowed
    groups = [LOWERCASE]                # lowercase is always included
    if use_upper:
        groups.append(UPPERCASE)
    if use_digits:
        groups.append(DIGITS)
    if use_symbols:
        groups.append(SYMBOLS)

    # Step 2: take one character from each group (guarantees variety)
    password_chars = []
    for group in groups:
        password_chars.append(secure_random.choice(group))

    # Step 3: join all allowed characters into one big pool
    all_characters = "".join(groups)

    # Step 4: fill the remaining length with random characters from the pool
    while len(password_chars) < length:
        password_chars.append(secure_random.choice(all_characters))

    # Step 5: shuffle so the guaranteed characters aren't always at the start
    secure_random.shuffle(password_chars)

    # Step 6: turn the list of characters into one string
    return "".join(password_chars)


def check_strength(password):
    """Give a simple strength rating based on length and variety."""
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c in LOWERCASE for c in password):
        score += 1
    if any(c in UPPERCASE for c in password):
        score += 1
    if any(c in DIGITS for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1

    if score <= 3:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"
    else:
        return "Very Strong"


def ask_number(message, minimum, maximum):
    """Keep asking until the user enters a whole number in the allowed range."""
    while True:
        text = input(message).strip()
        if not text.isdigit():
            print("Please enter a number.")
            continue
        number = int(text)
        if number < minimum or number > maximum:
            print(f"Please enter a number between {minimum} and {maximum}.")
            continue
        return number


def ask_yes_no(message):
    """Ask a yes/no question. Returns True for yes, False for no."""
    while True:
        answer = input(message + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


def main():
    print("=== Password Generator ===")

    while True:
        count = ask_number("How many passwords do you want? (1-10): ", 1, 10)
        length = ask_number(
            f"Password length? ({MIN_LENGTH}-{MAX_LENGTH}): ", MIN_LENGTH, MAX_LENGTH
        )

        use_upper = ask_yes_no("Include uppercase letters?")
        use_digits = ask_yes_no("Include numbers?")
        use_symbols = ask_yes_no("Include symbols?")

        print("\nYour passwords:")
        for i in range(1, count + 1):
            password = generate_password(length, use_upper, use_digits, use_symbols)
            print(f"{i}. {password}   [{check_strength(password)}]")

        print()
        if not ask_yes_no("Generate more passwords?"):
            print("Stay safe! Never reuse the same password everywhere.")
            break
        print()


if __name__ == "__main__":
    main()
