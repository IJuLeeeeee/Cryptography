from Crypto.PublicKey import RSA

def create_RSA_Key():
	key = RSA.generate(2048)
	file = open('rsa_private_key.txt','w')
	file.write(key.exportKey())
	file.close()
	file = open('rsa_public_key.txt','w')
	file.write(key.publickey().exportKey())
	file.close()
create_RSA_Key()
