### Import Libraries
from random import randrange
import numpy as np
import string

### Read Text File
with open('input.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

### Covert text to lowercase
data =  ''.join(x for x in data if x in string.printable)
data = data.lower()
print "Plain Text: "
print data
print ""

### Defines all letters
all_letters = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print "Let: ", all_letters

### Create key
key = list(np.random.permutation(all_letters))
print "Key: ", key
print ""

### Encrypt the text
data = list(data)
for i in range(len(data)):
	if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%','#','=','@','&'] or data[i].isdigit():
		continue
	index = all_letters.index(data[i])
	data[i] = key[index]

data  = ''.join(data)


### Print the ciphertext
print "Cipher Text: "
print data

### Save the cipher text to a file
text_file = open("ciphertext.txt", "w")
text_file.write("%s" % data)
text_file.close()

### Decrypt the text
data = list(data)
for i in range(len(data)):
	if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%','#','=','@','&'] or data[i].isdigit():
		continue
	index = key.index(data[i])
	data[i] = all_letters[index]

data  = ''.join(data)

### Print the ciphertext
print "Plain Text: "
print data

print key

