#Writing lists in python
cities = ['New York', 'London', 'Glasglow', 'Edinburgh', 'Delhi', 'Mumbai']
user_input = int(input('Enter the number of the city to be displayed, between 0 to 5: '))
print('The city you\'ve requested is: ', cities[user_input])

#slicing lists in python
print('The new sliced list is ', cities[0:user_input])

#deleting lists in python
del cities[3:0]
print('The new deleted sliced list is ', cities)

#Adding new elements to the list
user_city = input('Enter the city to be added to your preffrered list :')
cities.append(user_city)
print('The new list of city after append is ',cities)

insert_city = input('Enter the city to be added to your preffrered list :')
cities.insert(0,insert_city)
print('The new list of city after insert is ',cities)
