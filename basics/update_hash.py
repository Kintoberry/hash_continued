import hashlib
sha256hasher = hashlib.sha256()
sha256hasher.update(b'dol')
sha256hasher.update(b'phin')
digest = sha256hasher.hexdigest()
print(digest)