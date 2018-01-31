### Import Libraries
from random import randrange, randint
import numpy as np
import operator
import enchant

DNA_SIZE = 26  
DIRECTION_BOUND = [0, 1]       
CROSS_RATE = 0.8
MUTATE_RATE = 0.01
POP_SIZE = 100
N_GENERATIONS = 1000

class GA(object):
    def __init__(self, DNA_size, DNA_bound, cross_rate, mutation_rate, pop_size, init_pop):
        self.DNA_size = DNA_size
        DNA_bound[1] += 1
        self.DNA_bound = DNA_bound
        self.cross_rate = cross_rate
        self.mutate_rate = mutation_rate
        self.pop_size = pop_size

        self.pop = init_pop

    def DNA2product(self, DNA):                 # convert to readable string
        return DNA

    def get_fitness(self, pop, letters,cipher):
	fitness = np.zeros(POP_SIZE)
	for index,member in enumerate(pop):
		### Decrypt the text
		cipher_temp = list(cipher)
		all_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		key = member.tolist()
		for i in range(len(cipher_temp)):
			if cipher_temp[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%'] or cipher_temp[i].isdigit():
				continue
			index_temp = key.index(cipher_temp[i])
			cipher_temp[i] = all_letters[index_temp]

		cipher_temp  = ''.join(cipher_temp)

		### Check if any words exist
		words = cipher_temp.split(" ")
		count = 0
		correct = 0
		for word in words:
			if len(word) > 0:
				if d.check(word) == True:
					correct += 1
				count += 1
		fitness[index] = float(correct)/count
		
        return fitness

    def select(self, fitness):
	idx = np.arange(int(0.1*self.pop_size))
	for i in range(int(0.1*self.pop_size)-1):
        	idx = np.append(idx,np.arange(int(0.1*self.pop_size)))
	print idx
        return self.pop[idx]

    def crossover(self, parent, pop):
	if np.random.rand() < self.cross_rate:
		i_ = np.random.choice(np.arange(self.pop_size), size=1, replace=True, p=fitness/fitness.sum())
		parent2 = pop[i_][0]
		cross_point1 = np.random.randint(0, 25)   # choose crossover points
		cross_point2 = np.random.randint(0, 25)   # choose crossover point
		temp = parent[cross_point1]
		parent[cross_point1] = parent2[cross_point2]
		temp_index = np.where(parent == parent[cross_point1])
		for ind in temp_index[0]:
			if ind != cross_point1:
				parent[ind] = temp
	return parent

    def mutate(self, child):
        for point in range(self.DNA_size):
            if np.random.rand() < self.mutate_rate:
		i = np.random.randint(0, len(child), size=1)
		j =  np.random.randint(0, len(child), size=1)
		child[i], child[j] = child[j], child[i]
        return child

    def evolve(self, fitness):
        pop = self.select(fitness)
        pop_copy = pop.copy()
        for parent in pop:  # for every parent
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.pop = pop


### Create dicitionary
d = enchant.Dict("en_US")

### Read Text File
with open('ciphertext.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

### Covert text to lowercase
data = data.lower()
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
	if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%'] or data[i].isdigit():
		continue
	let_freq_cipher[data[i]] += 1

total = sum(let_freq_cipher.itervalues(), 0.0)
let_freq_cipher = {k: v / total for k, v in let_freq_cipher.iteritems()}
print "Frequency of each letter in the Ciphertext: ", let_freq_cipher
print ""

### Sort normal and cipher freq. from max to min
sorted_let_freq = sorted(let_freq.items(), key=operator.itemgetter(1))
sorted_let_freq_cipher = sorted(let_freq_cipher.items(), key=operator.itemgetter(1))

### Genetic Algorithm
init_pop = []
init_pop.append(np.array(sorted_let_freq_cipher)[:,0])
#init_pop.append(['m', 'e', 'l', 'g', 'd', 'w', 'h', 'q', 'f', 'y', 'n', 'p', 'a', 'o', 'v', 'k', 'x', 'r', 'b', 'z', 'c', 'u', 't', 's', 'i', 'j'])
for i in range(POP_SIZE-1):
	#init_pop.append(np.random.permutation(np.array(sorted_let_freq_cipher)[:,0]))
	init_pop.append(['m', 'e', 'l', 'g', 'd', 'w', 'h', 'q', 'f', 'y', 'n', 'p', 'a', 'o', 'v', 'k', 'x', 'r', 'b', 'z', 'c', 'u', 't', 's', 'i', 'j'])

ga = GA(DNA_size=DNA_SIZE, DNA_bound=DIRECTION_BOUND,
cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE, init_pop=np.array(init_pop))
letter_temp = np.array(sorted_let_freq)[:,0].tolist()

for generation in range(N_GENERATIONS):
	pop = ga.DNA2product(ga.pop)
	fitness = ga.get_fitness(pop,letter_temp,data)
	ga.evolve(fitness)
	print('Gen:', generation, '| best fit:', fitness.max(), '| best_pop:', pop[0])



### Decrypt the text
data = list(data)
all_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key = pop[0].tolist()
for i in range(len(data)):
	if data[i] in [' ', ',', '.',"'",'"','-',':',';','?','(',')','!','[',']','$','{','}','/','*','~','_','%'] or data[i].isdigit():
		continue
	index = key.index(data[i])
	data[i] = all_letters[index]

data  = ''.join(data)
	

print data
	






