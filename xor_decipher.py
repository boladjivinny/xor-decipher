import sys
from collections import Counter

def string_xor (cipher, key):
	i = 0
	result = ''
	while (i < len(cipher)):
		result = result + chr(ord(cipher[i:i+2].decode('hex')) ^ ord(key[i:i+2].decode('hex')))
		i = i+2
	return result
		
if __name__=='__main__':
	args = {"maxi" : 5, "char" : 'e'}
	
	for pair in sys.argv[1:]:
		data = pair.split('=')
		args[data[0][1:]] = data[1]
	
	ciphertext = input("Enter the cypher text : \n")
	spaced_ciphertext = ciphertext[:2]
	i = 2
	while (i < len(ciphertext)):
		spaced_ciphertext = spaced_ciphertext + ' ' + ciphertext[i:i+2]
		i = i+2
	letters = spaced_ciphertext.split(' ')
	letters = sorted(letters, key=Counter(letters).get, reverse=True)
	letters = sorted(set(letters), key=letters.index)
	
	for letter in letters[:int(args['maxi'])]:
		key = ord(letter.decode('hex')) ^ ord(args['char'])
		hex_key = hex(key)[2:]
		print ('\nHexadecimal key : {}\n'.format(hex_key))
		hex_key *=  len(ciphertext)/2
		uncrypted = string_xor(ciphertext, hex_key)
		print('Clear text:\n{}\n'.format(uncrypted))
	print ("Done...")
