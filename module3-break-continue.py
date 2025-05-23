#continue statement
for i in range(1,21):
    if ( i % 5 == 0):
        continue
    print(i)
print('Finished')


#break statement
while True:
    user_input = input('Enter the name or type EXIT to terminate: ')

    if (user_input == 'EXIT'):
        break
    
    print('Hello', user_input)

print('You\'re now exiting')
