import random

def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return (list_to_return, random.choice(list_to_return))

if __name__ == '__main__':
    print(generate_tickets(5,10))

# random.seed(0)
# print(random.random())
# print(random.random())
# print(random.random())


# choice
# integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(random.choice(integer))

# print(random.choice('Helloworld'))

# for i in range(10):
#     print(random.choice(integer))

# print(random.sample(integer, 3))
