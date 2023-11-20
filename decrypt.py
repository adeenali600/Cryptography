from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes  # used to mask data
from cryptography.hazmat.primitives.asymmetric import padding

import sys
import os

if (len(sys.argv)) != 2:
    print('Usage: ./decrypt.py original_filename')
    exit(-1)

with open(sys.argv[1], 'rb') as encrypt_file:  # opening file will be replaced
    # by encrypt_file
    encrypted_data = encrypt_file.read()

priv_pem = os.environ.get('PEMK')

with open(priv_pem, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(  # deserialization
        key_file.read(),
        password=None
    )

    decrypted = private_key.decrypt(  # public_key->private_key
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None)
    )

    with open(sys.argv[1]+'.decrypted', 'wb') as file:
        file.write(decrypted)
