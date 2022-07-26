import re
import string


# https://www.hackerrank.com/challenges/time-conversion/problem?h_r=profile

def timeConversion(s):
    hours = int(s.split(":")[0])
    am_pm = s[-2:]
        
    if am_pm == 'AM':
        if hours == 12:
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        if hours == 12:
            return "12" + s[2:-2]
        else:
            return str(hours + 12) + s[2:-2]
    

# print(timeConversion('07:05:45PM'))
# print(timeConversion('07:05:45AM'))
# print(timeConversion('12:40:22AM'))
print(timeConversion('12:40:22PM'))