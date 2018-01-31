### Import Libraries
from random import randrange, randint
import numpy as np
import operator
import enchant

### Create dicitionary
d = enchant.Dict("en_US")

### Read Text File
with open('ciphertext.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    data = data.replace("--", " ")

### Covert text to lowercase
data = data.lower()
cipher_org = data
print "Cipher Text: "
print data
print ""

### Define normal freq. of letters
let_freq = {}
let_freq['a'] = 0.08167
let_freq['b'] = 0.01492
let_freq['c'] = 0.02782
let_freq['d'] = 0.04253
let_freq['e'] = 0.12702
let_freq['f'] = 0.02228
let_freq['g'] = 0.02015
let_freq['h'] = 0.06094
let_freq['i'] = 0.06966
let_freq['j'] = 0.00153
let_freq['k'] = 0.00772
let_freq['l'] = 0.04025
let_freq['m'] = 0.02406
let_freq['n'] = 0.06749
let_freq['o'] = 0.07507
let_freq['p'] = 0.01929
let_freq['q'] = 0.00095
let_freq['r'] = 0.05987
let_freq['s'] = 0.06327
let_freq['t'] = 0.09056
let_freq['u'] = 0.02758
let_freq['v'] = 0.00978
let_freq['w'] = 0.02360
let_freq['x'] = 0.00150
let_freq['y'] = 0.01974
let_freq['z'] = 0.00074

print "Normal Frequency of each letter: ", let_freq
print ""

### Calculate letter freq in ciphertext
let_freq_cipher = {}
let_freq_cipher['a'] = 0.
let_freq_cipher['b'] = 0.
let_freq_cipher['c'] = 0.
let_freq_cipher['d'] = 0.
let_freq_cipher['e'] = 0.
let_freq_cipher['f'] = 0.
let_freq_cipher['g'] = 0.
let_freq_cipher['h'] = 0.
let_freq_cipher['i'] = 0.
let_freq_cipher['j'] = 0.
let_freq_cipher['k'] = 0.
let_freq_cipher['l'] = 0.
let_freq_cipher['m'] = 0.
let_freq_cipher['n'] = 0.
let_freq_cipher['o'] = 0.
let_freq_cipher['p'] = 0.
let_freq_cipher['q'] = 0.
let_freq_cipher['r'] = 0.
let_freq_cipher['s'] = 0.
let_freq_cipher['t'] = 0.
let_freq_cipher['u'] = 0.
let_freq_cipher['v'] = 0.
let_freq_cipher['w'] = 0.
let_freq_cipher['x'] = 0.
let_freq_cipher['y'] = 0.
let_freq_cipher['z'] = 0.

data = list(data)
for i in range(len(data)):
	if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%','#','=','@','&'] or data[i].isdigit():
		continue
	let_freq_cipher[data[i]] += 1

total = sum(let_freq_cipher.itervalues(), 0.0)
let_freq_cipher = {k: v / total for k, v in let_freq_cipher.iteritems()}
print "Frequency of each letter in the Ciphertext: ", let_freq_cipher
print ""

### Sort normal and cipher freq. from max to min
sorted_let_freq = sorted(let_freq.items(), key=operator.itemgetter(1))
sorted_let_freq_cipher = sorted(let_freq_cipher.items(), key=operator.itemgetter(1))



### Decrypt the text
data = list(data)
key = np.array(sorted_let_freq_cipher)[:,0]
all_letters = np.array(sorted_let_freq)[:,0]
for i in range(len(data)):
	if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%','#','=','@','&'] or data[i].isdigit():
		continue
	index = np.where(key == data[i])
	data[i] = all_letters[index][0]

data  = ''.join(data)
print data
key_correct = []
checked_words = []
visual_correct = []
all_letters = np.array(sorted_let_freq)[:,0]
while(1):
	word_flag = False
	for wordi,word in enumerate(data.split(" ")):
		flag = False
		for char in word:
			if char not in visual_correct:
				flag = True
		if len(word) > 8 and d.check(word) == True and flag == True and word not in checked_words:
			try:
				print data.split(" ")[wordi-3]
			except:
				pass
			try:
				print data.split(" ")[wordi-2]
			except:
				pass
			try:
				print data.split(" ")[wordi-1]
			except:
				pass
			try:
				print data.split(" ")[wordi-0]
			except:
				pass
			try:
				print data.split(" ")[wordi+1]
			except:
				pass
			try:
				print data.split(" ")[wordi+2]
			except:
				pass
			
	
			string = "Is " + word + " a word?, type 'check' to see the new ciphertext"
			word_flag = True
			checked_words.append(word)
			user_check = raw_input(string)
			if user_check in ['y','Y','Yes','yes']:
				for let in word:
					if let in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%','#','=','@','&'] or let.isdigit():
						continue
					index1 = np.where(np.array(all_letters) == let)[0][0]
					let2 = key[index1]
					visual_correct.append(let)
					key_correct.append(let2)
			elif user_check in ['check']:
				### Decrypt the text
				data = list(cipher_org)
				for i in range(len(data)):
					if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%','#','=','@','&'] or data[i].isdigit():
						continue
					index = np.where(key == data[i])
					data[i] = all_letters[index][0]

				data  = ''.join(data)
				print data
			elif user_check in ['swap']:
				let1 = raw_input("Enter the first letter to swap")
				let2 = raw_input("Enter the second letter to swap")
				index1 = np.where(np.array(all_letters) == let1)[0][0]
				index2 = np.where(np.array(all_letters) == let2)[0][0]
				print key[index1],key[index2]
				temp = key[index1]
				key[index1] = key[index2]
				key[index2] = temp
			
	for i in range(13):
		ind1 = randint(0,25)
		while(key[ind1] in key_correct):
			ind1 = randint(0,25)
		ind2 = randint(0,25)
		while(key[ind2] in key_correct):
			ind2 = randint(0,25)
		temp = key[ind1]
		key[ind1] = key[ind2]
		key[ind2] = temp

	### Decrypt the text
	data = list(cipher_org)
	for i in range(len(data)):
		if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%','#','=','@','&'] or data[i].isdigit():
			continue
		index = np.where(key == data[i])
		data[i] = all_letters[index][0]

	data  = ''.join(data)
	print data
	print key
	if word_flag == True:
		user_check = raw_input("Does the cipher look correct")
	



	






