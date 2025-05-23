#print the length of string
print(len('hello'))

#python adds /n by default after each print fxn
print('Hello John')
print('How are you!')

#default end line can be amended with end statement
print('Hello John', end='.')
print('How are you!')

#adding separator to separate out the two statements
lastname = input('Enter your lastname: ')
print('Hello John', lastname, 'How are you!',  sep='-', end='.')
