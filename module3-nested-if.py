#Nested if statement
var1 = input('Do you have a children? y/n ')
if (var1 == 'y'):
    var2 = input('Is it a girl or boy? y/n ')
    if (var2 == 'girl'):
        print('Excellent! You\'re eligible for girl child benefits')
    else:
        print('Wonderful!')
else:
    print('Thanks for providing the information')
