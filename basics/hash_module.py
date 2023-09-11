import hashlib
import os

def compute_digest(data, hash_algo):
    hasher = hashlib.new(hash_algo)
    hasher.update(data)
    return hasher.hexdigest()

def compute_file_digest(file_path, hash_algo, buffer_size=8192):
    hasher = hashlib.new(hash_algo)
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            hasher.update(data)
        return hasher.hexdigest()
            
if __name__ == "__main__":
    print(compute_digest(b"a", "sha256"))
    file_path = os.path.join(os.getcwd(), 'text_files', 'short.txt')
    print(compute_file_digest(file_path, "md5"))