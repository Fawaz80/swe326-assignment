#!/usr/bin/env python
# coding: utf-8

# # ICS 104 - Introduction to Programming in Python and C
# ## Functions 

# # Lab Objectives
# - To be able to implement functions
# - To become familiar with the concept of parameter passing
# - To develop strategies for decomposing complex tasks into simpler ones
# - To be able to determine the scope of a variable

# # Excercises 

# - <font color='blue'>**Excercise # 1**</font> Write a function ```def kfupm_email(ID, level)``` that returns a string containing KFUPM email.
# 
# Two types of email are generated depending on the level:
# * undergraduate (level:s) email example: s202188450@kfupm.edu.sa
# * graduate (level:g) email example g202188650@kfupm.edu.sa
# 
# Write the necessary python statements to test the function.

# In[13]:


def kfupm_email(ID, level) :
    Name = level + ID
    return Name
x = input("Enter your ID: ")
y = input('Enter your level: ')
Name = kfupm_email(x, y)
print(Name+'@kfupm.edu.sa')


# - <font color='blue'>**Excercise # 2**</font> Write a function ```def isPrime(number)``` that returns True or False depending whether the number is prime or not.
# 
# 
# Write the necessary python statements to test the function.

# In[ ]:


# Exercise 2
def isPrime(number):
    flag = False
    for i in range(2, number-1):
        if number % i == 0 :
            flag = True
    return flag
Usernumber = int(input('Enter a whole number: '))
if Usernumber <= 0 :
    print('Out of range')
elif Usernumber == 1 :
    print(Usernumber, 'is not prime')
else :
    x = isPrime(Usernumber)
    if x == True:
        print(Usernumber, 'is not prime')
    else :
        print(Usernumber, 'is prime')
    
    


# In[ ]:





# - <font color='blue'>Exercise # 3:</font> If we know the lengths of two sides ($b$ and $c$) of a triangle and the angle between them in degrees ($\alpha$), we can compute the length of the third side ( $a$ ) using the following formula: 
# $$a^2 = b^2 + c^2 - 2bc \ cos(\alpha)$$
# 
# **a) write a python function that does that (receives two sides length and returns the third side length)**
# 
# ![tri.PNG](attachment:tri.PNG)
# - Heron’s formula to calculate the area of a triangle with sides $a$, $b$, and $c$ is:
# $$ S = \frac{a+b+c}{2}$$  
# 
# $$ Area = \sqrt{S(S-a)(S-b)(S-c)}$$
# 
# **b) write a python function that uses Heron formula to calculate the area of a triangle (receives all 3 sides length and returns the area)**
# 
# **c) write a python function (let us call it area2sa() that  calculates the area using two sides and one angle. (The easiest way to do that is to use the already available functions in a,b)**
# 
# 
# **d) Write some python statements to test the above 3 functions.**
# - Notes: 
#     - $\pi$ radians $=180$ degrees 
#     - The value of $\pi$ (3.141592).
#    - You can use math functions like `sqrt`, `cos`, and `pow`
# 
# Examples to help you check:
# 
# **Triangle 1:**
# 
# * Sides: 10.6, 8.65, 6.19  cm
# * Angle between side1 and side2 : 35.7 degrees
# * Area: 26.75 cm^2 
# 
# 
# 
# **Triangle 2:**                                                                                  
# * Sides: 3.0, 4.0, 5.0  cm
# * Angle between side1 and side2 : 90 degrees
# * Area: 6.0 cm^2 

# In[12]:


# Exercise 3
def aLength(b, c, alpha) :
    from math import cos
    from math import sqrt
    from math import pi
    a = sqrt((b**2) + (c**2) - 2 * b * c * (cos(alpha)/pi))
    return a
         
def Area(a, b, c) :
    from math import sqrt
    S = (a + b + c)/2
    area = sqrt(S * (S-a) * (S-b) * (S-c))
    return area

def area2sa(b, c, alpha) :
    thirdSide = aLength(b, c, alpha)
    area2sa = Area(thirdSide, b, c)
    return area2sa

b = float(input('Enter length of the 1st side: '))
c = float(input('Enter length of the 2nd side: '))
angle = float(input('Enter the angle between the sides in degrees: '))

if b <= 0 or c <= 0 :
    print('ERROR enter a valid number')
elif angle >= 180 or angle <= 0 :
    print('Angle must be a positive between 0 and 180')
else :
    Lengthof_a = aLength(b, c, angle)
    Area = Area(Lengthof_a, b, c)
    print()
    print('Sides:', round(Lengthof_a,2), 'and', b, 'and', c)
    print('Angle between the sides you entered:', angle)
    print('Area:', round(Area,2), 'cm^2')
    



    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




