#list comprehension to generate list
num = [i for i in range(1,101)]
print('List of 100 numbers are', num)

#list comprehension to generate list eliminating all even numbers
num = [i for i in range(1,101) if i % 2 != 0]
print('\nList of odd numbers', num)


#list comprehension to generate list eliminating all odd numbers
num = [i for i in range(1,101) if i % 2 == 0]
print('\nList of even numbers', num)
