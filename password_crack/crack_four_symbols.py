from crack_lib import generate_combination, get_ascii_lowercase, get_ascii_uppercase, get_ascii_letters, get_alphanumeric, get_printable_letters, compute_digest
from time import time 

def crack_three_printable_letters(target_hash):
    alphanumeric = get_printable_letters(encode=False)
    generator = generate_combination(alphanumeric, 4)
    for passwd in generator:
        passwd = passwd.encode('utf-8')
        digest = compute_digest(passwd, 'md5')
        if digest == target_hash:
            print(f"Cracked the password for target hash: {target_hash}")
            print(f"The Password is: {passwd}")
            break

if __name__ == "__main__":
    start_time = time()
    target_hash = "a470225540f1d4c3741e6e6636bfff10"
    crack_three_printable_letters(target_hash)
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Cracking the password took: {elapsed_time} seconds")