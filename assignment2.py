import random

if __name__ == '__main__':
	rand = random.randint(1,10)
	while True:	
		in_num = input('Guess the number: ')
		if in_num == rand:
			print('Correct!')
			exit()
		else:
			print('Wrong, try again!')
