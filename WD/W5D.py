
# %%
class ReverseString:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

# %%
# Testing
input_string = 'hello .py'
reverser = ReverseString()
reversed_string = reverser.reverse_words(input_string)
print(reversed_string) 



# %%
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# %%
# Testing
circle = Circle(5)  
print("Area:", circle.area())         
print("Perimeter:", circle.perimeter())
# %%
