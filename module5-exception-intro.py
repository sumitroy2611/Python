#Exception example
def provide_inverse():
    try:
        number = int(input('Enter the number: '))
        print('The inverse of the number', number,'is',1/number)
    except ValueError:
        print('You\'ve entered un-supported value. Hence, can\'t calculate the inverse')
    except ZeroDivisionError:
        print('Sorry, diving by zero isn\'t allowed')
    except:
        print('Something unexpected happened. Sorry')

provide_inverse()
