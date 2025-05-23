#Write a function to count the number of specific letters in a string
def count_char(string = 'Learn Python from scratch and pass the PCEP exam (Certified Entry-Level Python Programmer)', char = 'a'):
    counter = 0
    for i in string:
        if (i == char):
            counter += 1
    print('The number of appear of letter',char,'in the given string is',counter)

count_char('Hello', 'e')


