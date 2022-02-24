from datetime import datetime
from datetime import date

def what_weekday():
    today = date.today()
    wday = today.weekday()
    english = today.strftime('%A')
    print(f"Today is {english}")

def get_user_birthday():
    """Requests user input from stdinput

    returns: a date object
    """
    # TODO: Error check input
    year = input('What year were you born? >')
    month = input('What month were you born? >')
    day = input('What day of the month were you born? >')
    bdstring = '-'.join([year, month, day])
    bday = datetime.strptime(bdstring, '%Y-%m-%d' )
    return bday

def user_age(bday):
    """Given a user's birthday, prints their age to stdout
    bday: a datetime 

    returns: void. prints to stdout
    """
    today = datetime.today()
    age = abs(today - bday)
    yearsold = age.days // 365
    return yearsold

def main():
    what_weekday()
    bd = get_user_birthday()
    print(user_age(bd))
    pass

if __name__ == "__main__":
    main()
