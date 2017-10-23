from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives import hashes

import time


###### open data
origin_file = open('origin_file.txt', 'r')
file_data = origin_file.read()
origin_file.close()
file_data = bytes(file_data, 'utf-8')



###### create and load private key
private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())

###### create and load public key
public_key = private_key.public_key()
pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)

####### encrypt
start = time.time()

encode_data = []
length = 200
# plaintext will too long so load part of to encrypt
for i in range(0,len(file_data),length):
	encode_data.append(public_key.encrypt(file_data[i:i+length],padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),algorithm=hashes.SHA1(),label=None)))
end = time.time()
running_time = end-start
print('Cryptography RSA-2048 encode time : '+str(running_time))

####### decrypt
start = time.time()
plaintext = []
for i in range(0,len(encode_data)):	
	plaintext.append(private_key.decrypt(encode_data[i],padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),algorithm=hashes.SHA1(),label=None)))

end = time.time()
running_time = end-start
print('Cryptography RSA-2048 decode time : '+str(running_time))




