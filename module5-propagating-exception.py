#propagating exception

def enter_bday(user_info):
    bday = int(input('Enter your birth day: '))
    user_info.append(bday)

def enter_bday_month(user_info):
    month = int(input('Enter the month(0-12) of your birthday: '))
    user_info.append(month)

def enter_bday_year(user_info):
    year = int(input('Enter the year of your birthday: '))
    user_info.append(year)

def get_user_bday(user_info):
    try:
        enter_bday(user_info)
        enter_bday_month(user_info)
        enter_bday_year(user_info)

        print('Your birthday is on:',user_info)
    except ValueError:
        print('You\'ve entered unsupported value. Can\'t calculate your DOB')

print('Hi ! I like to know your birth date')
user_info = []

get_user_bday(user_info)
