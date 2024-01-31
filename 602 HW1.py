
#Q1
# This program gets three test scores and displays their average. It congratulates the user if the
# average is a high score. The high score variable holds the value that is considered a high score.


HIGH_SCORE = 95

# Get the test scores
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
# Added missing input for test3
test3 = int(input('Enter the score for test 3: '))  

# Calculate the average test score.
# Add parenthesis to ensure correct order of the operation
average = (test1 + test2 + test3) / 3 

# Print the average.
print('The average score is', average)

# If the average is a high score,
# congratulate the user.
# Update the ensure the correct variable name (HIGH_SCORE)
if average >= HIGH_SCORE:  
    print('Congratulations!')
    print('That is a great average!')


#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
L1=float(input('Enter the length of rectangle 1: '))
W1=float(input('Enter the width of rectangle 1: '))

L2=float(input('Enter the length of rectangle 2: '))
W2=float(input('Enter the width of rectangle 2: '))

Area1=L1*W1
Area2=L2*W2

print('The area of the 1st rectangle', Area1)
print('The area of the 2nd rectangle', Area2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

Name=input('Hi! Please enter your name: ')
Age=int(input('Please enter your age: '))
print(f'Happy birthday, {Name}! You are {Age} years old today')