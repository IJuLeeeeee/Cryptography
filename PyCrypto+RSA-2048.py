# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

from Crypto.Cipher import AES, PKCS1_OAEP

from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA

from Crypto.Cipher import PKCS1_v1_5

from Crypto.Hash import SHA512

from Crypto import Random

import time

#padding
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]



def encrypt(data,public_key,length = 200):
	public_recipient_key = RSA.importKey(public_key)
	cipher_rsa = PKCS1_v1_5.new(public_recipient_key)


	# because plaintext will too long , so load 200 at one time
	# the come out ciphertext will same length
	res = []
	for i in range(0,len(data),length):
		res.append(cipher_rsa.encrypt(data[i:i+length]))
		
	return res


def decrypt(data,private_key):

	private_recipient_key = RSA.importKey(private_key)
	plain_rsa = PKCS1_v1_5.new(private_recipient_key)

	dsize = SHA512.digest_size

	for i in range(0,len(data)):
		sentinel = Random.new().read(15 + dsize)
		plain_rsa.decrypt(data[i], sentinel)



# open file
origin_file = open('origin_file.txt', 'r')

file_data = origin_file.read()
origin_file.close()
# string into bytes by utf-8
file_data = bytes(file_data, 'utf-8')


start = time.time()

file = open('rsa_public_key.txt','r')
public_key = file.read()
file.close()

encode_file_data = encrypt(file_data,public_key)

end = time.time()
running_time = end-start
print('PyCrypto RSA-2048 encode time : '+str(running_time))


start = time.time()

file = open('rsa_private_key.txt','r')
private_key = file.read()
file.close()

decrypt(encode_file_data,private_key)

end = time.time()
running_time = end-start
print('PyCrypto RSA-2048 decode time : '+str(running_time))



