
# %%
# 1. What are the similarities and differences between pandas and numpy?   Include some type of example with code.
# They are both handle data effectively.
# Pandas is ideal for structured data like tables, offering more features for data manipulation. 
# NumPy shines in numerical computations with its powerful array operations. 
# I like to consider Pandas as a versatile toolkit for data wrangling and NumPy as a high-performance math engine.
# eg. compute mean of a column
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
mean_value_np = np.mean(arr)
print(mean_value_np)


import pandas as pd
data = {'A': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
mean_value_pd = df['A'].mean()
print(mean_value_pd)

#%%
# 2. What is the ndarray in numPy?
# ndarray is like dealing with a powerful math wizard who handles heavy numerical lifting with ease!
# eg.
import numpy as np
arr2d=np.array([[1,2,3],[4,5,6]])
# Adding 10 to every element
new_arr=arr2d+10

# %%
# 3. Create a 1D array of numbers from 0 to 9 
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
import numpy as np
arr=np.arange(10)
arr


# %%
# 4. Extract all odd numbers from array1 

array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_number=array1[array1%2!=0]
print(odd_number)


# %%
# 5. Get the common items between a and b  

#input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
#Desired Output:
#array([2, 4])

print(np.intersect1d(a,b))



# %%
#6. From array a remove all items present in array b 

#Input:

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

#Desired Output:
#array([1,2,3,4])

print(np.setdiff1d(a, b))

# %%
#7. Find out if iris has any missing values. 



import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(np.isnan(iris).any())


# %%
