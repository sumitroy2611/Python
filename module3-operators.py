#Combined operators
var1 = int(input('Enter the age: '))
var2 = input('Enter the country: ')

if (var2 != 'Germany' and var1 < 26) or (var2 == 'Germany' and var1 >= 26):
    print('You qualify')
else:
    print('You do not quality')
