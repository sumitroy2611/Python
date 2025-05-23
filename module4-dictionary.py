#dictionary intro
dict_intro = {
    1 : 'Virat Kohli',
    2: 'Surya Kumar Yadav',
    3: 'Rohit Sharma'
}
print(dict_intro[1])


# dictionary fetch keys
for dict1 in dict_intro.keys():
    print('Keys are ', dict1)

# dictionary fetch values
for dict2 in dict_intro.values():
    print('Values are ', dict2)

# dictionary fetch both keys and values
for key, values in dict_intro.items():
    print('Key',key,'has value',values)
