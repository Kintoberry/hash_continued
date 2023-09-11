import hashlib
sha256hasher = hashlib.sha256(b'dolphin')
digest = sha256hasher.hexdigest()
print(digest)