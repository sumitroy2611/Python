#A tuple can has list in it
user_data = ('Mark', 'Washington', [12.5, 13, 15])
print(user_data)


#A list can have tuple in it
user_data1 = ['Mark', 'Washington', (12.5, 13, 15)]
print(user_data1)


#List in a tuble can be appended
user_data[2].append(17)
print(user_data)

#tuple in a list can't still be appended
user_data1[2].append(17) #This throws an error
