# -*- coding: utf-8 -*-


# import library

from __future__ import absolute_import, division, unicode_literals

from Crypto.Cipher import AES

from Crypto import Random

import time

from Crypto.Hash import SHA512


# padding
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

# encrypt data
def encrypt(data):
    h = SHA512.new()
    h.update(data)
    return h

# open file
origin_file = open('origin_file.txt', 'r')

# read file_data
file_data = origin_file.read()

origin_file.close()


start = time.time()
# do padding
file_data = pad(file_data)


file_data = str.encode(file_data)

a=encrypt(file_data)
print(a)
end = time.time()
running_time = end-start
print('PyCrypto SHA-512 encode time : '+str(running_time))


