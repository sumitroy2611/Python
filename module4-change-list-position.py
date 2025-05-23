#Sorting list without changing the actual list
cities = ['New York', 'London', 'Glasglow', 'Edinburgh', 'Delhi', 'Mumbai']
print('The sorted list of cities are: ',sorted(cities))
print('The list of cities are: ', cities)


#Sorting list that changes the actual list
cities.sort()
print('The list of cities are: ', cities)

#Reverse sorting list that changes the actual list
cities.sort(reverse=True)
print('The reverse list of cities are: ', cities)

#swapping two integers
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
print('Both the numbers before swapping', first_number, second_number)

first_number, second_number = second_number, first_number 

print('Both the numbers after swapping', first_number, second_number)
