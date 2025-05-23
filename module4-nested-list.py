#Nested list
lists = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for i in lists:
    for x in i:
        print(i,x)

#Nested list
table = [[i for i in range(1,6)] for j in range(4)]
print(table)
