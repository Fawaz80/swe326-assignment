#!/usr/bin/env python
# coding: utf-8

# # ICS 104 - Introduction to Programming in Python and C
# ## Loops - Lab 1

# # Lab Objectives
# - To implement while and for loop
# - To become familiar with common loop algorithms

# # Worked Example

# - <font color='blue'>Problem Statement:</font> Read twelve temperature values (one for each month), and display the number of the month with the highest temperature. For example, according to http://worldclimate.com, the average maximum temperatures for Death Valley are (in order by month, in degrees Celsius):  
# > 18.2 &nbsp; 22.6 &nbsp; 26.4 &nbsp; 31.1 &nbsp; 36.6 &nbsp; 42.2 &nbsp; 45.7 &nbsp; 44.5 &nbsp; 40.2 &nbsp; 33.1 &nbsp; 24.2 &nbsp; 17.6
# - In this case, the month with the highest temperature (45.7 degrees Celsius) is July, and the program should display 7.

# ![ch04figw00.PNG](attachment:ch04figw00.PNG)

# - <font color='blue'>**Step 1:**</font> Decide what work must be done inside the loop.
#     - If you can’t figure out what needs to go inside the loop, start by writing down the steps that you would take if you solved the problem by hand. 
# ![ch04figw01.PNG](attachment:ch04figw01.PNG)

# - Now look at these steps and reduce them to a set of uniform actions that can be placed into the loop body. The first action is easy:
# ![ch04figw02.PNG](attachment:ch04figw02.PNG)

# - The next action is trickier. In our description, we used tests “higher than the first”, “higher than the first and second”, and “higher than the highest temperature seen so far”. 
# - We need to settle on one test that works for all iterations. The last formulation is the most general.
# - Similarly, we must find a general way of setting the highest month. We need a variable that stores the current month, running from 1 to 12. Then we can formulate the second loop action:
# ![ch04figw03.PNG](attachment:ch04figw03.PNG)

# - Now the loop becomes
# ![ch04figw04.PNG](attachment:ch04figw04.PNG)

# - <font color='blue'>**Step 2:**</font> Specify the loop condition. What is the condition of the loop?

# - `current month <= 12`

# - <font color='blue'>**Step 3:**</font> Determine the loop type. Which is more suitable, a `while` loop or a `for` loop?

# - A `for` loop is more suitable, since we know exactly how many iterations to perform.

# - <font color='blue'>**Step 4:**</font> Set up variables for entering the loop for the first time.
# 

# ![ch04figw05.PNG](attachment:ch04figw05.PNG)

# - <font color='blue'>**Step 5:**</font> Process the result after the loop has finished.

# - In our case, the result is the highest month.

# - The complete pseudo code is as follows:
# ![ch04figw06.PNG](attachment:ch04figw06.PNG)

# - <font color='blue'>**Step 6:**</font> Trace the loop with typical examples.
# ![ch04figw07.PNG](attachment:ch04figw07.PNG)
# - Note that there is no need to scratch the values out, as the textbook suggests, if you follow the convention that the last value of each column/variable in the table is the current value of that variable, you won't need to scratch anything out. 

# - <font color='blue'>**Step 7:**</font> Translate the pseudo code into Python.

# In[ ]:


#%%writefile lab06Example1.py
## Uncomment the above line after you finish your code and want to save it in a file.

# YOUR CODE HERE

## This program reads 12 temperature values corresponding to the 12 months of the year (starting at 1), 
#  and then prints the month with the highest temperature.
#
highestValue = float(input("Enter a value: "))  # Read the temperatrue for January
highestMonth = 1                                # This indicates January
for currentMonth in range(2, 13) :              # Iterate for months 2, 3, 4, ..., 12 (December)
    nextValue = float(input("Enter a value: ")) # Read the temperature of the next month.
    if nextValue > highestValue :               # Check whether it is higher than the highest
        highestValue = nextValue                # It is higher, so update the highest value
        highestMonth = currentMonth             # Correspondingly, update the highest month

# Print the highest month
print(str(highestMonth) + " was the highest month, with record temperature of "+ str(highestValue) + " degrees Celsius")


# # Side Note Regarding the `print` Function
# - The `print` function displays an end of line by default.
# - If we want to change this behavior, we can set the `end` parameter to another string.
#     - The default value of the `end` parameter is \n.
# - Consider the following example

# In[ ]:


course = "ICS 104"
University = "KFUPM"
print(course,end="@")  
print(University)  
print("First","second",sep="-")


# # Exercises 

# - <font color='blue'>Exercise # 1:</font> Write a while loop that prints all squares less than an input integer value **n**. For example, if the user enters 100, the program shall print 
# > 0 1 4 9 16 25 36 49 64 81.
# - The following are sample runs of the program.

# ![Ex1Sample1.PNG](attachment:Ex1Sample1.PNG)

# ![Ex1Sample2.PNG](attachment:Ex1Sample2.PNG)

# In[5]:


#Exercise 1
x = input('Enter an integer number please: ')
x = int(x)
y = 0 
if x <= 0 :
    print('No squares are less than', x)
else :
    while y**2 < x :
        print(y**2)
        y = y + 1


# - <font color='blue'>Exercise # 2:</font> Write a loop that reads numbers from the user and sum them. The loop continues till a negative number is entered. Your program then prints the result.
# 
# - The following are sample runs of the program.<br>
# 
# **Sample run 1:** <br>
# Enter a positive number: (or a negative value to finish):5<br>
# Enter a positive number: (or a negative value to finish):2<br>
# Enter a positive number: (or a negative value to finish):4<br>
# Enter a positive number: (or a negative value to finish):-5<br>
# Sum = 11.0
# 
# **Sample run 2:**<br>
# Enter a positive number: (or a negative value to finish):-8<br>
# No positive number was entered.

# In[4]:


#Exercise 2
x = input('Enter a positive number, and a negative value to finish: ')
x = float(x)
if x > 0 :
    sumx = 0
    while x > 0 :
        sumx = sumx + x
        x = input('Enter a positive number, and a negative value to finish: ')
        x = float(x)
    print('Sum =', sumx)
else :
    print('no positive value was entered')
        
    
    


# - <font color='blue'>Exercise # 3:</font> Write a python program that reads an integer from the user and prints back the number of the digits in that integer and the sum of them. For example, if the input was 2308 , the output would be: Your integer has 4 digits and their sum is 13.
# 
# - Hints:
#     - N%10 will always generate the rightmost digit of the integer N.
#     - N//10 will always generate the same integer WITHOUT its rightmost digit.
#     - When you have on digit (any of 0 to 9) and you divide it by 10 (integer division), the result is always 0. You can use this idea to stop the loop.
# 
# - The following are sample runs of the program:<br><br>
# **Sample run 1:**<br>
# Enter a positive integer value: **2308**<br>
# Your integer has **4** digits and their sum is **13**<br><br>
# **Sample run 2:**<br>
# Enter a positive integer value: **714702**<br>
# Your integer has **6** digits and their sum is **21**

# In[2]:


#Exercise 3

x = int(input('Enter: '))
digits = len(str(x))
dignum = len(str(x))
digtotal = 0
x = int(x)
while dignum > 0 :
    xremain = x % 10
    digtotal = xremain + digtotal
    x = x // 10
    dignum = dignum - 1
print('Your integer has', digits, 'digits and their sum is', digtotal)
    
    


# - <font color='blue'>Exercise # 4:</font> Write a program that prompts for and reads the number $n$ of spheres to be processed. If $n \le 0$ your program must display an error message and terminate; otherwise it does the following for $n$ times:
#     - Prompts for and reads the volume of a sphere, it then displays the surface area of the sphere with that volume. Assume that each volume is in cubic centimeters.
# - The program finally displays the average of the surface areas of the $n$ spheres.
# - Please note that
#     - $\pi = 3.14159$.
#     - volume $= \frac{4}{3}\pi r^3$.
#     - surface area $= 4\pi r^2$.
# - The following are sample runs of the program.

# ![Ex4Sample1.PNG](attachment:Ex4Sample1.PNG)

# ![Ex4Sample2.PNG](attachment:Ex4Sample2.PNG)

# In[1]:


#Exercise 4
processTimes = int(input('Enter number of sphere to be processed: '))
if not processTimes > 0 :
    print('Number of spheres must be bigger than zero')
else :
    processnumber = processTimes
    sphereNum = 0
    surfaceSum = 0
    while processTimes > 0 :
        processTimes = processTimes - 1
        sphereNum = int(sphereNum) + 1
        sphereNum = str(sphereNum)
        sphereVolume = input('Enter volume of sphere '+sphereNum+' :')
        sphereVolume = float(sphereVolume)
        from math import pi
        radius = (sphereVolume * 3/4 * 1/pi )**(1/3)
        surfaceArea = 4 * pi * radius**2
        surfaceArea = round(surfaceArea, 2)
        print('Sphere #' + str(sphereNum) + ' surface area = '+ str(surfaceArea))
        surfaceSum = surfaceArea + surfaceSum
    average = float(surfaceSum) / float(processnumber)
    average = round(average, 2)
    print('the average surface area =', average)


# ## WARNNING:
# Some students submitted codes that they did not write!.
# It is OK to discuss the tasks and seek help from anybody but eventually  **WRITE YOUR OWN CODE!**
# 

# # End of the  Loops - Lab 1
# Good luck...
