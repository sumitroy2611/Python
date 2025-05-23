#Iterative factorial
def iterative_factorial(number):
    final_number = 1
    for i in range(1, number+1):
        final_number *=i
    return final_number

print('Factorial using the first method is ',iterative_factorial(6))

#recursive factorial
def recursive_factorial(number):
    if number <= 1:
        return 1
    return number * recursive_factorial(number - 1)

print('Factorial using the second method is ',recursive_factorial(6))
