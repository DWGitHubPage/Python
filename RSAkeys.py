# Python3.7.3
# Creating a public and private RSA key pair.


from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate private/public key pair.
key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=2048)

# Get public key in OpenSSH format.
public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, \
    serialization.PublicFormat.OpenSSH)

# Get private key in PEM container format.
pem = key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())

# Decode to printable strings.
private_key_str = pem.decode('utf-8')
public_key_str = public_key.decode('utf-8')

print('Private key = ')
print(private_key_str)
print('Public key = ')
print(public_key_str)
