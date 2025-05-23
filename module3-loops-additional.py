#for loop and if statement necessarily needs a statement
for i in range(11):
    pass

#for loop and if statement necessarily needs a statement
for i in range(1,6):
    for x in range(1,6):
        print(i,'x',x,'=',i*x)

#else in case of while loop
i = int(input('Enter the number: '))
while i<6:
    print(i)
else:
    print('else:',i)
