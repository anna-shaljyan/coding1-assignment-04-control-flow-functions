def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: If condition check whether number from list [1,2,3] meets the condition 
# of being greater than 1, and when it it true it moves forward and passes that number to
# add_one function, which itself takes the value and adds 1 to it
# For example here 1, won't meet condition and only 2, 3 from list satisfy, so it will move to
# print statement and print 3, 4

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: add_one(2) will return 3, as add_one function gets value 2 and add 1 to it
# so just like 2 + 1 and returns 3
# If we have return statement, later we can assign some variable the function with its value and print it or use later
# print only displays a value on the screen. In the loop, print displays the
# returned values 3 and 4; it does not store them which is the main difference.