driving = input('Do you drive car before?')
if driving != 'Yes' and driving != 'No':
	print('Only can input Yes or No')
	raise SystemExit

age = input('How old are you?')
age = int(age)

if driving == 'Yes':
	if age >= 18:
		print('you pass the test')
	else:
		print('Weird, how can you drive the car?')
elif driving == 'No':
	if age >= 18:
		print('You can go to get the Car Driver\'s License now.')
	else:
		print('Great! You can get the Car Driver\'s license once you come to age.' )