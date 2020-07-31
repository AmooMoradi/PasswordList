from itertools import product
from random import randint

def Check():
	answer = input("Do you want to create a password with length x to y? (Y/n) ")
	if (answer == 'y' or answer == 'Y'):
		first = int(input("Enter first number: "))
		seconde = int(input("Enter seconde number: "))
		return [1,first,seconde]
	first = int(input("Enter number: "))
	return [0, first]


characters = input("Please Enter Your Characters: ")
func = Check()
file = open("/home/behshad/Desktop/" + str(randint(0,10000000)) + ".txt", 'a')
if (func[0] == 1):
	for length in range(func[1], func[2]+1):
		print(length)
		for _pass in product(characters, repeat=length):
			file.write(''.join(_pass)+ " \n")
else:
	for _pass in product(characters, repeat=func[1]):
		file.write(''.join(_pass)+ " \n")
		
file.close()
