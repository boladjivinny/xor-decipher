# xor-decipher

This is a piece of program that deciphers an encoded message using **XOR**. 
Currently the script only works with keys of only one alphanumerical number.

The method used in this code is based on the fact that some letters (usually vowels) are more frequent in some languages (e or a in French and English).
Based on this information, the current sript is built and delivers best possible solutions for the key along the uncrypted message.

# Usage
`python xor_decipher.py [-char=CHARACTER] [-maxi=NUMBER_OF_RESULTS]`

1.  CHARACTER is the most used character in your language. (Defaults to e).
2.  NUMBER_OF_RESULTS represents the number of solutions you want to look for (Defaults to 5).

I keep myself available for further needs