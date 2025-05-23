#Iterating lists in python(Method1)
cities = ['New York', 'London', 'Glasglow', 'Edinburgh', 'Delhi', 'Mumbai']
for city in cities:
    print('Current city: ',city)

#Iterating lists in python(Method2)
for city_index in range(len(cities)):
    print('city index: ',city_index, 'is', cities[city_index])

#Adding items of the list
salary = [2.5, 12.5, 33.0, 35.0]
sum = 0
for item in salary:
    sum += item
print('The salary sum is: ',sum)
