from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#read key from file
with open("privateKey.txt", "rb") as key_file:

    private_key = serialization.load_pem_private_key(

        key_file.read(),
        password=None,
    )

public_key = private_key.public_key()

#message as bytes
with open("geheimtext.txt", "rb") as f:
    message = f.read() 

# with a 2048-bit RSA key and OAEP/SHA-256, your plaintext must be ≤ 190 bytes

ciphertext = public_key.encrypt(

    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
with open("geheimtext.txt", "wb") as f:
    f.write(ciphertext)