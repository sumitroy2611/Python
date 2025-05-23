#generator example
def get_val(item):
    for i in range(item):
        yield i

generator = get_val(3)
print(next(generator))
print(next(generator))
print(next(generator))

#Get the generator value in a loop
for x in get_val(4):
    print(x)

#Get the generator value in a list
final_list = list(get_val(5))
print(final_list)
