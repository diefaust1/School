from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#read key from file
with open("privateKey.txt", "rb") as key_file:

    private_key = serialization.load_pem_private_key(

        key_file.read(),
        password=None,
    )

#message as bytes
with open("geheimtext.txt", "rb") as f:
    ciphertext = f.read() 

plaintext = private_key.decrypt(

    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open("geheimtext.txt", "wb") as f:
    f.write(plaintext)