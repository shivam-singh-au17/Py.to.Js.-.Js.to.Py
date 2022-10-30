# SIMPLE INTEREST
# Given the Principal Amount, Interest Percentage and Time calculate the simple interest amount

# Note - Please write the formula of Simple interest in multi-line comments, and write the explanation of each variable in single line comment.


"""
The siple interest formula is
SI = (p * r * t / 100)
"""

principal = 100000;     # this is the principal amount
rate = 8;               # This is the rate in percent annum
time = 5;               # This is the time in year

sipleIntrest = (principal * rate * time) / 100
print(sipleIntrest)




# NAME-A-THON
# Write the variable names for the following things and assign any relevant value to it.

# Average Age
# Number of Students
# Maximum marks
# The first name
# Number of Students in 12th Class.

averageAge = 26
numberOfStudent = 205
maximumMarks = 100
theFirstName = "Shivam"
numberOfStudentIn12ThClass = 53



# OPERATORS
# Take a variable named a , assign it a value of 10, and perform the following operations on it.

# Add 2 to the same variable
# Subtract 3 from the same variable
# Divide the same variable by 6
# Multiply the same variable by 11
# take a remainder by 7 of the same variable


a = 10
a += 2
a -= 3
a /= 6
a *= 11
a %= 7
print(a)




# THE GAME OF LIES - I
# Suppose there are 4 persons playing a game. The result of a particular match is dependant on various strategies of AND and OR

# Note - First Write your result in comments by calculating it on your own and check it whether it matches by running the code.

# GAME-1

# True && False && !(True) || False
# GAME-2

# True || !(False) && (True || False)
# GAME-3

# False || (True && False) || True 
# GAME-4

# True || (False && True || True)





a = True and False and (not True) or False;
print(a)

b = True or (not False) and (True or False);
print(b)

d = False or (True and False) or True;
print(d)

e = True or (False and True or True);
print(e)