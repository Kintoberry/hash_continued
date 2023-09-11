import hashlib
import os

hasher = hashlib.new('sha256')
file_path = os.path.join(os.getcwd(), 'text_files', 'short.txt')

with open(file_path, 'rb') as file:
    data = file.read()
hasher.update(data)
print(hasher.hexdigest())
