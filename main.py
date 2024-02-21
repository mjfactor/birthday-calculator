import datetime


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


today = datetime.date.today()  # Get the date today
thisYear = today.year
thisMonth = today.month
thisDay = today.day

while True:
    year = int(input("Enter your Birth Year: "))
    if len(str(year)) != 4:
        print("Enter 4 digit number Only")
    elif year < 1900:
        print("Your are Too old")
    elif year > thisYear:
        print("You haven't born yet")
    else:
        break
while True:
    month = int(input("Enter your Birth month: "))
    if month >= 13:
        print("There is only 12 months")
    elif year == thisYear and month > thisMonth:
        print("You haven't born yet")
    else:
        break
while True:
    birthDate = int(input("Enter your Birth Date: "))
    if len(str(birthDate)) != 2:
        print("Enter a 2 digit number")
    elif birthDate >= 32:
        print("There is only 31 days in calendar")
    elif year == thisYear and month == thisMonth and birthDate > thisDay:
        print("You haven't born yet")
    elif month == 2 and birthDate >= 29:
        print("There is only 28 days in February(2)")
    else:
        break

userBirthday = datetime.date(year, month, birthDate)

leap_years = sum(is_leap(y) for y in range(year, thisYear + 1))
x = (today - userBirthday).days - leap_years
age = x // 365  # Divide days in a year / 365 days, use floor division to cut off decimals

print("-------------------------")
print("Today's Date:", today, )
print("Your Birthday:", userBirthday)
print("You're", age, "year old")
