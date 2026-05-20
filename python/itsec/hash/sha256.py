import hashlib

text = "Hallo"

hashwert = hashlib.sha256(text.encode()).hexdigest()

print(hashwert)