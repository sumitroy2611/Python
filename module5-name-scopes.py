#Differentiate global and local variable
# def return_value():
#     username = 'abc123'
#     print(username)

# username = 'xyz456'
# print(username)
# return_value()
# print(username)


#Differentiate with global variable
def return_value():
    global username
    username = 'abc123'
    print(username)

username = 'xyz456'
print(username)
return_value()
print(username)

#Differentiate with global variable list type
def return_value():
    username1.append('efg123')
    print(username1)

username1 = ['xyz456']
print(username1)
return_value()
print(username1)
