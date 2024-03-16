
# 1. Create a list called animals
animals = ["cat", "dog", "manta ray", "horse", "crouching tiger"]

# 2. Iterate through the animals list using range()
len_animals = len(animals)
for i in range(len_animals):
    print(animals[i])

# 3. Sort countdown list in descending order and find the 5th element
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
countdown.sort(reverse=True)  
the_fifth_element = countdown[4]

# 4. Add item 7000 after 6000 in the nested list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

# 5. Remove all occurrences of item 20 from the list
list2 = [5, 20, 30, 15, 20, 30, 20]
list2 = [x for x in list2 if x != 20]

# 6. Manipulate the dictionary
dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}
print(dict["Course"])
dict["Course"] = "DATA 602" 
dict["Professor"] = "Schettini"
num_keys = len(dict)  

# 7. Change Brad's salary in the dictionary
sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}
sample_dict['emp3']['salary'] = 7500
