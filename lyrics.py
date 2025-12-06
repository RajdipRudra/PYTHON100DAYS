
'''
import time, sys

def type_out(text, delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

lyrics = [
    "Lock me up and throw away the key",
    "He knows how to get the best out of me",
    "I'm no force for the world to see",
    "Trade my whole life just to be",
    "Top of the world but I'm still not free",
    "It's such a secret that I keep",
    "Until it's gone, I can never find peace",
    "Brace my whole life just to be"
]

for line in lyrics:
    type_out("\n"+line)

print("\n")'''


def is_leapyear(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year=year) and month==1:
        return 29
    else:
        return days_in_month[month]




year = int(input("enter ur year : "))
month = int(input("enter a month: "))
dats = days_in_month(year,(month-1))
print(dats)


def is_leapyear(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year=year) and month==1:
        return 29
    else:
        return days_in_month[month]




year = int(input("enter ur year : "))
month = int(input("enter a month: "))
dats = days_in_month(year,(month-1))
print(dats)
def is_leapyear(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year=year) and month==1:
        return 29
    else:
        return days_in_month[month]




year = int(input("enter ur year : "))
month = int(input("enter a month: "))
dats = days_in_month(year,(month-1))
print(dats)