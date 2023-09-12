from crack_lib import generate_combination, get_ascii_lowercase, get_ascii_uppercase, get_ascii_letters, get_alphanumeric, get_printable_letters, compute_digest
from time import time 


def crack_lowercase(target_hash):
    lower_letters = get_ascii_lowercase(encode=False)
    generator = generate_combination(lower_letters, 1)
    for passwd in generator:
        passwd = passwd.encode('utf-8')
        digest = compute_digest(passwd, 'md5')
        if digest == target_hash:
            print(f"Cracked the password for target hash: {target_hash}")
            print(f"The Password is: {passwd}")

def crack_uppercase(target_hash):
    upper_letters = get_ascii_letters(encode=False)
    generator = generate_combination(upper_letters, 1)
    for passwd in generator:
        passwd = passwd.encode('utf-8')
        digest = compute_digest(passwd, 'md5')
        if digest == target_hash:
            print(f"Cracked the password for target hash: {target_hash}")
            print(f"The Password is: {passwd}")

def crack_alphanumeric(target_hash):
    alphanumeric = get_alphanumeric(encode=False)
    generator = generate_combination(alphanumeric, 1)
    for passwd in generator:
        passwd = passwd.encode('utf-8')
        digest = compute_digest(passwd, 'md5')
        if digest == target_hash:
            print(f"Cracked the password for target hash: {target_hash}")
            print(f"The Password is: {passwd}")

def crack_printable_letters(target_hash):
    alphanumeric = get_printable_letters(encode=False)
    generator = generate_combination(alphanumeric, 1)
    for passwd in generator:
        passwd = passwd.encode('utf-8')
        digest = compute_digest(passwd, 'md5')
        if digest == target_hash:
            print(f"Cracked the password for target hash: {target_hash}")
            print(f"The Password is: {passwd}")


if __name__ == "__main__":
    start_time = time()
    target_hash = "cbb184dd8e05c9709e5dcaedaa0495cf"
    crack_printable_letters(target_hash)
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Cracking the password took: {elapsed_time} seconds")