import hashlib
import os

hasher = hashlib.new('sha256')
file_path = os.path.join(os.getcwd(), 'text_files', 'harrypotter.txt')

with open (file_path, 'rb') as file:
    while True:
        data = file.read(8192)
        if not data:
            break
        hasher.update(data)

print(hasher.hexdigest())