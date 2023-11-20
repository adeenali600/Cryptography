from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
#serialiaztion= to create byte representations of objects so we can save in files

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

print(private_key) ;#private key object is generated

#Let's serialize this object in a file in human-readable form

priv_pem=private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

print(priv_pem)

with open ('priv.pem','wb') as priv_pem_file:
    #writing our private object in file in binary mode
    priv_pem_file.write(priv_pem)

# 'set PEMK=./priv.pem' = Now I will just enter 'PEMK' and it will fetch the whole path
#No need to write the whole path each time

#Lets create public key to share with the reciever: 

public_key=private_key.public_key() ;"public_key = variable initialized"
#Lets serialize public key now like we did for private
pub_pem=public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open ('pub.pem','wb') as pub_pem_file:
    #writing our public object in file in binary mode
    pub_pem_file.write(pub_pem)