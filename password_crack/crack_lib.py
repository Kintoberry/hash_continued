import string

import hashlib

def compute_digest(data, hash_algo):
    hasher = hashlib.new(hash_algo)
    hasher.update(data)
    return hasher.hexdigest()

def generate_combination(alphabet, max_len):
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate_combination(alphabet, max_len-1):
            yield c + next


def get_ascii_lowercase(encode=False):
    if not encode:
        return string.ascii_lowercase
    return string.ascii_lowercase.encode('utf-8')

def get_ascii_uppercase(encode=False):
    if not encode:
        return string.ascii_uppercase
    return string.ascii_uppercase.encode('utf-8')

def get_ascii_letters(encode=False):
    if not encode:
        return string.ascii_letters
    return string.ascii_letters.encode('utf-8')

def get_alphanumeric(encode=False):
    alphanumeric = string.ascii_letters + string.digits
    if not encode:
        return alphanumeric
    return alphanumeric.encode('utf-8')

def get_printable_letters(encode=False):
    if not encode:
        return string.printable
    return string.printable.encode('utf-8')


if __name__ == "__main__":
    # combination_generator = generate_combination(get_ascii_letters(encode=False), 1)
    # for password in combination_generator:
    #     print(password)
    print(get_printable_letters())
    
