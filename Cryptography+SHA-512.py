from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

import time






###### open data
origin_file = open('origin_file.txt', 'r')
file_data = origin_file.read()
origin_file.close()
file_data = bytes(file_data, 'utf-8')


####### encrypt
start = time.time()


digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
digest.update(file_data)
digest.finalize()


end = time.time()
running_time = end-start
print('Cryptography SHA-512 encode time : '+str(running_time))


