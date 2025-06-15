def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# for loop is ranging from 1 (including) and 20(excluding)

# 2. When is the function meant to print "You got it"?
#  When i equals 20,which is never gonna happen considering the range we are providing

# 3. What are your assumptions about the value of i?
#  It will loop from 1 to 19 but never get to 20 , hence the function doesn't print anything
