from cryptography.hazmat.primitives import padding

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptography.hazmat.backends import default_backend

import time, os

# do padding
def padding_data(data):
	padder = padding.PKCS7(128).padder()
	padded_data = padder.update(data)
	padded_data += padder.finalize()
	return padded_data


def unpad(data):
	unpadder = padding.PKCS7(128).unpadder()
	unpadded_data = unpadder.update(data)
	unpadded_data += unpadder.finalize()
	return unpadded_data



# encrypt
def encrypt(data,key):
	cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
	encryptor = cipher.encryptor()
	encode_data = encryptor.update(data) + encryptor.finalize()
	return encode_data

# decrypt
def decrypt(data,key):
	cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
	decryptor = cipher.decryptor()
	decode_data = decryptor.update(data) + decryptor.finalize()
	decode_data = unpad(decode_data)
	return decode_data




# open file
origin_file = open('origin_file.txt', 'r')
file_data = origin_file.read()
origin_file.close()

# str to bytes
file_data = bytes(file_data, 'utf-8')


file_data = padding_data(file_data)

backend = default_backend()
# set key
key = os.urandom(32)



start = time.time()

encode_data = encrypt(file_data,key)


end = time.time()
running_time = end-start
print('Cryptography AES-256-ECB encode time : '+str(running_time))

start = time.time()

decrypt(encode_data,key)

end = time.time()
running_time = end-start
print('Cryptography AES-256-ECB decode time : '+str(running_time))
