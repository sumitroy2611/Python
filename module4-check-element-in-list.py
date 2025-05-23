#Check element present in list
cities = ['New York', 'London', 'Glasglow', 'Edinburgh', 'Delhi', 'Mumbai']
user_input = input('Enter the name of the city to be searched: ')

if user_input in cities:
    print('City %s is present' %user_input)
else:
    print('Not found')
