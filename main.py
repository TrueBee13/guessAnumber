import random 
import sys

tries=0
secret_number=random.randint(1,101)
while True:
	
	print('Guess number or press "q"')
	guess=input()
	if guess=='q':
		print(f'you give up on {tries} tries, your secret number was: {secret_number}')
		sys.exit()

	tries+=1	
	guess=int(guess)
	print(f'your guess is: {guess}')
	if guess==secret_number:
		print('Winner, winner go make Olia a dinner!!!!')
		print(f'it took you  {tries} tries')
		sys.exit()
	else:
		if guess>secret_number:
			print('You are getting close---->HOT ')
		else:
			print("COLD!!!")

		




