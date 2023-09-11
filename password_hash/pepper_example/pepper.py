import configparser

config = configparser.ConfigParser()
config.read('config.ini')

pepper = config['security']['pepper']

def hash_password_with_pepper(password):
    peppered_password = password + pepper

    import hashlib
    hashed_password = hashlib.sha256(peppered_password.encode()).hexdigest()

    return hashed_password

password = "mysecretpassword"
hashed_password = hash_password_with_pepper(password)
print("Original Password:", password)
print("Hashed Password (with pepper):", hashed_password)
