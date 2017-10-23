from cryptography.hazmat.primitives import padding

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptography.hazmat.backends import default_backend

import time, os

def padding_data(data):
	padder = padding.PKCS7(128).padder()
	padded_data = padder.update(data)
	padded_data += padder.finalize()
	return padded_data

def encrypt(data,key,iv):
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
	encryptor = cipher.encryptor()
	encode_data = encryptor.update(data) + encryptor.finalize()
	return encode_data


def decrypt(data,key,iv):
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
	decryptor = cipher.decryptor()
	decryptor.update(data) + decryptor.finalize()





origin_file = open('origin_file.txt', 'r')
file_data = origin_file.read()
origin_file.close()

# str to bytes
file_data = bytes(file_data, 'utf-8')

# padding
file_data = padding_data(file_data)

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)



start = time.time()

encode_data = encrypt(file_data,key,iv)


end = time.time()
running_time = end-start
print('Cryptography AES-256-CBC encode time : '+str(running_time))

start = time.time()

decrypt(encode_data,key,iv)

end = time.time()
running_time = end-start
print('Cryptography AES-256-CBC decode time : '+str(running_time))
