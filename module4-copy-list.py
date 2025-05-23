#Copying string
old_name = 'John smith'
new_name = 'Steve smith'

old_name = new_name

print('New name:', new_name, '\nOld name:', old_name)

#Copying list without slice(copying refrence)
old_list = [1,2,3]
new_list = [4,5,6]

old_list = new_list

new_list[0] = -5

print('New name:', new_list, '\nOld name:', old_list)


#Copying list with slice
old_list = [1,2,3]
new_list = [4,5,6]

old_list = new_list[:]

new_list[0] = -5

print('New name:', new_list, '\nOld name:', old_list)
