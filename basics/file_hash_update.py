import hashlib
import os

file_name = os.path.join(os.getcwd(), 'text_files', 'long.txt')
hasher = hashlib.new('sha256')

with open (file_name, 'rb') as file:
    while True:
        data = file.read(100)
        if not data:
            break
        print(data)
        hasher.update(data)

print(hasher.hexdigest())