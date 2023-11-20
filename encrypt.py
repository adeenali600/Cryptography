from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes  # used to mask data
from cryptography.hazmat.primitives.asymmetric import padding

import sys
# reads our environment variable so that it can acces PEMK variables that we exported.
import os

if (len(sys.argv)) != 2:
    print('Usage: ./encrypt.py original_filename')
    exit(-1)

print('Original filename:', sys.argv[1])
#print the original file name and path at runtime
pub_pem = os.environ.get('PUB_PEMK')
print('Public key file:', pub_pem)

with open(sys.argv[1], 'rb') as org_file:  # opening file in read and binary mode
    org_data = org_file.read()  # all file contents will be saved in org_data

pub_pem = os.environ.get('PUB_PEMK')

with open(pub_pem, 'rb') as pub_key_file:
    public_key = serialization.load_pem_public_key(  # deserialization
        pub_key_file.read()
    )

# since encryption uses public key that's why we are sending public key as the parameter

encrypted = public_key.encrypt(
    org_data,  #original data file's path
    padding.OAEP(
        # Optimal Asymmetric Encryption Padding should be used for RSA Encryption.

        mgf=padding.MGF1(algorithm=hashes.SHA256()),

        # mgf(mask generation function) produces a mask that is associated with the
        # size of input data.
        # hashes.SHA256() produces a hash (message digest) to check the sent message
        # is unaltered, but in itself is of fixed size (In this case 256 bits).

        algorithm=hashes.SHA256(),
        label=None
    )
)

with open(sys.argv[1]+'.encrypted', 'wb') as file:
    file.write(encrypted)
