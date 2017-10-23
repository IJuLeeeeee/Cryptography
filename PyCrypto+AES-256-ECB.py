# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

from Crypto.Cipher import AES

from Crypto import Random

import time

# padding
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

# encrypt data
def encrypt(data, key):
    cryptor = AES.new(key, AES.MODE_ECB)
    return cryptor.encrypt(data)

# decrypt data
def decrypt(data, key):
	cryptor = AES.new(key, AES.MODE_ECB)
	return cryptor.decrypto(data)
 
# load 512MB file
origin_file = open('origin_file.txt', 'r')

# set key , 256 bits = 32 bytes
key = 'abcdefghijklmnopqrstuvwxyz123456'

# open file and load it
file_data = origin_file.read()
origin_file.close()

start = time.time()
encode_file_data = encrypt(pad(file_data),key)
end = time.time()
running_time = end-start
print('PyCrypto AES-256-ECB encode time : '+str(running_time))




start = time.time()
encrypt(encode_file_data,key)
end = time.time()
running_time = end-start
print('PyCrypto AES-256-ECB decode time : '+str(running_time))