from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def create_key():
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    )
    return private_key

def save_key(content, file_name):
    
    with open(file_name, "wb") as f:
        f.write(content)

PUBLIC_FILE = "pubKey.txt"
PRIVATE_FILE = "privateKey.txt"

my_private_key = create_key()

my_public_key = my_private_key.public_key()

pem_private = my_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)
pem_public = my_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

save_key(pem_public, PUBLIC_FILE)
save_key(pem_private, PRIVATE_FILE)


