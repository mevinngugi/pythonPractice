# alarm_clock

'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
indicating if we are on vacation, return a string of the form "7:00" indicating
when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
the weekend it should be "10:00". Unless we are on vacation -- then on weekdays
it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'

'''


def alarm_clock(day, vacation):

    if vacation == False and 1 <= day <= 5:
        return "7:00"

    elif vacation == False and (day == 0 or day == 6):
        return "10:00"

    elif vacation == True and 1 <= day <= 5:
        return "10:00"

    elif vacation == True and (day == 0 or day == 6):
        return "off"


print(alarm_clock(6, True))

# A better sollution

'''def alarm_clock(day, vacation):
  if not vacation:
    if 1 <= day <= 5:
      return '7:00'
    return '10:00'
  
  if 1 <= day <= 5:
    return '10:00'
  return 'off' '''

'''
near_ten

Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
See also: Introduction to Mod

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True

'''
def near_ten(num):
	print (num % 10)
	return (num % 10) <2 or 8 <= (num % 10) <= 10

print (near_ten(17))
