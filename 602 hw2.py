#Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
#The code should return an empty list because numbers[1:-5] doesn't include any elements.



# Can you debug and fix the output? The code should return the entire list
print(numbers[:])
# or just print(numbers)

# Q2. Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result
sales = []
for day in range(7):
    daily_sales = float(input(f"Please input the sales for day {day+1}: "))
    sales.append(daily_sales)

total_sales = sum(sales)
print(total_sales)

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in alphabetical order
wish_list = ["quebec", "montreal", "chengdu", "hawaii", "mexico city"]
# ● Print your list in its original order.
print(wish_list)
# ● Use the sort() function to arrange your list in order and reprint your list.
wish_list.sort()
print(wish_list)
# ● Use the sort(reverse=True) and reprint your list.
wish_list.sort(reverse=True)
print(wish_list)

# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

room_number = {
    "DATA102": "101",
    "DATA103": "102",  
    "DATA104": "103",  
    "DATA105": "104",
}
instructor = {
    "DATA101": "John Smith",
    "DATA102": "John Doe",
    "DATA103": "Bob Davis",
    "DATA104": "David Brown",
}
meeting_time = {
    "DATA101": "9:00 am- 10:30 am",
    "DATA102": "11:00am-12:30pm",
    "DATA103": "2:00pm-3:00pm",
    "DATA104": "3:30pm-5:00pm",
}
course_num = input("Please kindly input a course number (e.g., DATA102): ")
if course_num in room_number and course_num in instructor:
    print(
        f"Course {course_num}; room number :{room_number[course_num]} ; instructor: {instructor[course_num]}; meeting time: {meeting_time[course_num]}"
    )
else:
    print("Course not found.")


# Q5. Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.
# Initialize an empty dictionary to store names and email addresses
contacts = {}

# 1. Function to look up an email address by name
def lookup_email(name):
    if name in contacts:
        return f'Email address for {name}: {contacts[name]}'
    else:
        return f'{name} not found in contacts'


# 2. Function to add a new name and email address
def add_contact(name, email):
    if name in contacts:
        return  f'{name} alreay exists in contacts'
    else:
        contacts[name]= email
        return f'Added {name} with {email} to contact'
    
# 3. Function to change an existing email address
def update_contact(name, new_email):
    if name in contacts:
        contacts[name]=new_email
        return  f'Updated email address for {name} to {new_email}'
    else:
        return f'{name} not found in contacts. Cannot update email'

# 4. Function to delete an existing name and email address
def delete_contact(name):
    if name in contacts:
        del(contacts[name])
        return  f'Deleted {name} and email from contacts'
    else:
        return f'{name} not found in contacts. Cannot delete'
# Demonstrate the options
while True: 
    print('Options:')
    print('1.look up a person’s email address')
    print('2.add a new name and email address')
    print('3.change an existing email address')
    print('4.delete an existing name and email address')
    print('5.exit the program')
    c=input('Please enter your choice (1/2/3/4/5): ')
    if c=='1':
        name=input('Please enter the name to look up: ')
        result=lookup_email(name)
        print(result)
    elif c=='2':
        name=input('Please enter the name to add: ')
        email=input('Please enter the email to add: ')
        result=add_contact(name, email)
        print(result)
    elif c=='3':
        name=input('Please enter the name to change email address: ')
        new_email=input('Please enter the new email: ')
        result=update_contact(name, new_email)
        print(result)
    elif c=='4':
        name=input('Please enter the name to delete: ')
        result=delete_contact(name)
        print(result)
    elif c=='5':
        print('exit program')
        break
    else:
        print('Invalid choice. Please enter a valid option (1/2/3/4/5).')









