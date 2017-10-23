# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

from Crypto.Cipher import AES

from Crypto import Random

from Crypto.Util import Counter

import time

# padding
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

# set counter
ctr = Counter.new(128)

def encrypt(data, key):
	cryptor = AES.new(key, AES.MODE_CTR, counter=ctr)
	return cryptor.encrypt(data)

def decrypt(data, key):
	cryptor = AES.new(key, AES.MODE_CTR, counter=ctr)
	return cryptor.decrypt(data)


# open file and load
origin_file = open('origin_file.txt', 'r')
# set key
key = 'abcdefghijklmnopqrstuvwxyz123456'

file_data = origin_file.read()
origin_file.close()

start = time.time()
encode_file_data = encrypt(pad(file_data),key)
end = time.time()
running_time = end-start
print('PyCrypto AES-256-CTR encode time : '+str(running_time))




start = time.time()
decrypt(encode_file_data,key)
end = time.time()
running_time = end-start
print('PyCrypto AES-256-CTR decode time : '+str(running_time))