import string
import random


def generate_password(password_len) -> str:
    password_charset = list(string.ascii_letters + string.digits + string.punctuation)

    # do a first shuffling
    random.shuffle(password_charset)

    # build a string of the given length
    password = [password_charset[i] for i in range(password_len)]

    # reshuffle
    random.shuffle(password)

    return "".join(password)


should_generate_pass = input("Do you want to generate a password? (y/n) ")
if (str(should_generate_pass).lower()) == 'y':
    done = False
    while not done:
        password_len_str = input("Enter the length of the generated password: ")
        try:
            password_len = int(password_len_str)
            if password_len <= 0:
                raise ValueError("Zero or negative integer not allowed")
            done = True
        except Exception:
            print(">> length must be a positive integer")
            done = False
    password = generate_password(password_len)
    print(f"Generated password: {password}")
else:
    print("Exiting")
