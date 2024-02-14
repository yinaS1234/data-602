#Q1
#%%
while True:
    meal = input("Hi there, please enter the meal (breakfast, lunch, dinner), or 'quit' to exit: ").lower()
    if meal=='quit':
        print('Exit! Have a nice day!')
        break

    if meal == "breakfast":
        print("How about some bacon and eggs?")
    elif meal == "lunch":
        print("How about a chicken sandwich?")
    elif meal == "dinner":
        print("How about some orange chicken with brown rice?")
    else:
        print("Sorry, I can only recommend meals for breakfast, lunch, or dinner.")

#Q2
#%%

hours_worked = float(input("Hi, please enter the number of hours worked: "))
pay_rate = float(input("Hi, please enter your hourly pay rate: "))
overtime_hours = hours_worked - 20
gross_pay = (20 * pay_rate) + (overtime_hours * pay_rate * 1.5)
print(f"Your gross pay is ${gross_pay:.1f}")

#Q3
# %%
def times_ten(num):
    print(num*10)

times_ten(20)


#Q4
# %%
#fix the variable names for consistency
def main():
    calories1 = float(input("How many calories are in the first food? ")) #added space after ? to take input
    calories2 = float(input("How many calories are in the second food? ")) #added space after ? to take input
    showCalories(calories1, calories2)

def showCalories(calories1, calories2):
    # Corrected syntax errors for formatting total calories as 2 decimals float number.
    print(f"The total calories you ate today: {(calories1 + calories2):.2f}") 

showCalories(15.2,200)

#Q5
# %%
total = 0
for i in range(1, 31):
    total += i / (31 - i)
print(f"The total of the series is: {total}")

#Q6
# %%
def triangle_area(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.0f}")
triangle_area(5,4)



