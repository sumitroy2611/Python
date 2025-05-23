#test unique item method 1
def unique(item=[]):
    final_list = []
    var = set(item)
    for i in var:
        final_list.append(i)
    return sorted(final_list)
    
print(unique([1, 1, 4, 5, 1]))

#test unique item method 2
def unique(item=[]):
    final_list = []
    for i in item:
        if i not in final_list:
            final_list.append(i)
    return final_list
print(unique([1, 1, 4, 5, 1]))


