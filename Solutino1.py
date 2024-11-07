# Take input from user:
marks = int(input('Enter your marks: '))

# Condition Check

if marks  <= 100 and marks >= 80:
    print('Your Grade : (A+)')
elif marks < 80 and marks >= 70:
    print('your Grade : (A)')
elif marks < 70 and marks >= 60:
    print('your Grade : (A-)')
elif marks < 60 and marks >= 50:
    print('your Grade : B')
elif marks < 50 and marks >= 40:
    print('your Grade : (C)')
elif marks < 40 and marks >= 33:
    print('your Grade : (D)')
elif marks < 33:
    print('You are Faill')
else
    print('You can use as input (0-100)') 