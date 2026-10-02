# Password Generator

A command-line tool written in pure Python that generates strong, secure, random passwords.

## Features

- Generate 1 to 10 passwords at a time
- Choose the length (8 to 64 characters)
- Choose whether to include uppercase letters, numbers and symbols
- Every selected character type is guaranteed to appear in each password
- Uses `random.SystemRandom`, the operating system's secure random source
- Strength rating for each password (Weak / Medium / Strong / Very Strong)
- Input validation: invalid input is rejected instead of crashing the program

## Tech Used

- Python 3.6+
- Concepts: loops, string handling, lists, functions
- Libraries: `random`, `string` (both built-in)

## Project Structure

```
passwordgenerator/
├── password_generator.py   # The program
├── requirements.txt        # Dependencies (none to install)
└── README.md               # Documentation
```

## How to Run

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python password_generator.py
```

On Mac/Linux you may need `python3 password_generator.py`.

## Example

```
=== Password Generator ===
How many passwords do you want? (1-10): 3
Password length? (8-64): 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Your passwords:
1. 6zU-JKac2%?j   [Very Strong]
2. =.;WmsaNzq^3   [Very Strong]
3. =o2I7)ZQAKUn   [Very Strong]

Generate more passwords? (y/n): n
```

## How It Works

1. The `string` module provides character sets (`ascii_lowercase`, `ascii_uppercase`, `digits`).
2. One character is picked from each selected group, so every type is guaranteed to appear.
3. The rest of the password is filled with random characters from all selected groups combined.
4. The characters are shuffled so the guaranteed ones are not always at the start.
5. They are joined into a final string with `"".join(...)`.
6. `check_strength()` scores the password on length and character variety.

## Security Notes

- Passwords are generated locally and never saved or sent anywhere.
- Use a different password for every account.
- Store passwords in a password manager.

## Learning Outcomes

- Secure password generation
- String handling and the `string` module
- Using loops, lists and functions
- Validating user input
