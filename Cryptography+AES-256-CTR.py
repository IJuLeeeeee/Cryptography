from cryptography.hazmat.primitives import padding

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptography.hazmat.backends import default_backend

import time, os


# encrypt
def encrypt(data,key,iv):
	cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)
	encryptor = cipher.encryptor()
	encode_data = encryptor.update(data) + encryptor.finalize()
	return encode_data

# decrypt 
def decrypt(data,key,iv):
	cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)
	decryptor = cipher.decryptor()
	decryptor.update(data) + decryptor.finalize()




# open file
origin_file = open('origin_file.txt', 'r')
file_data = origin_file.read()
origin_file.close()
file_data = bytes(file_data, 'utf-8')


# set key, iv, backend
backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)



start = time.time()

encode_data = encrypt(file_data,key,iv)


end = time.time()
running_time = end-start
print('Cryptography AES-256-CTR encode time : '+str(running_time))

start = time.time()

decrypt(encode_data,key,iv)

end = time.time()
running_time = end-start
print('Cryptography AES-256-CTR decode time : '+str(running_time))
