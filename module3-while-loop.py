#While loop example

print('''
++++++++++++++++++++++++++++++
======Secret Number Game======
++++++++++++++++++++++++++++++
''')

secret_number = 12
user_input = int(input('Please enter your secret number between 0 and 20: '))
while secret_number != user_input:
    print('That\'s incorrect')
    user_input = int(input('Please enter your secret number between 0 and 20: '))
print('You\'ve entered correct number %s' %user_input)
