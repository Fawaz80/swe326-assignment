#!/usr/bin/env python
# coding: utf-8

# # ICS 104 - Introduction to Programming in Python and C
# ## Decision Structures - Lab 2 

# # Lab Learning Outcomes
# - To learn how to program simple and complex decisions. 
# - To implement decisions using if statements
# - To write statements using Boolean expressions
# - To validate user input

# - <font color='blue'>Exercise# 1:</font> Write a program that reads a temperature value and the letter C for Celsius or F for Fahrenheit. Print whether water is liquid, solid, or gaseous at the given temperature at sea level. 
# - You can use the following formula to convert from Fahrenheit to Celsius $C= \frac{5\times(F - 32)}{9}$
# 
# | Sample Run | Sample Run | Sample Run|
# | :-- | :-- | :-- |
# |Enter the temperature: 30 <br>Enter the unit (C or F): F <br>At that temperature, the water is solid.| Enter the temperature: 150 <br>Enter the unit (C or F): C<br>At that temperature, the water is gaseous.| Enter the temperature: 70 <br>Enter the unit (C or F): F <br>At that temperature, the water is liquid.|

# In[50]:


# Question 1
length = input('Enter the length of the object: ')
unit = input('Specify the unit, "C" for cm or  "I" for inches: ')
length = float(length)

if unit == 'I' :
    length = length * 2.53
if unit == 'I' or unit == 'C' :
    if length < 30 :
        print('Small')
    elif length >= 30 and length <= 50 :
        print('Medium')
    else :
        print('Large')
else : 
    print('Invalid unit')



# - <font color='blue'>Exercise# 2:</font> A supermarket awards coupons depending on how much a customer spends on groceries. For example, if you spend $50, you will get a coupon worth eight percent of that amount. The following table shows the percent used to calculate the coupon awarded for different amounts spent. Write a program that calculates and prints the value of the coupon a person can receive based on groceries purchased. A sample run is as follows:
# 
# |Sample Run| Sample Run|
# |:--|:--|
# |Please enter the cost of your groceries: 200 <br> You win a discount coupon of \$24.00. (12\% of your purchase)| Please enter the cost of your groceries: 7 <br> You win a discount coupon of \$0.00. (0\% of your purchase)|
# 

# ![ch03-lab-fig1.PNG](attachment:ch03-lab-fig1.PNG)

# In[47]:


# Question 2
spent = input('Please enter the cost of your groceries: ')
spent = float(spent)

if spent < 10 :
    print('No coupon')
elif spent >= 10 and spent <= 60 :
    discount = spent * 0.08
    discount = float(discount)
    discount = round(discount, 2)
    print('You win a discount coupon of $', discount, '.', '(8% of your purchase)')
elif spent > 60 and spent <= 150 :
    discount = spent * 0.1
    discount = float(discount)
    discount = round(discount, 2)
    print('You win a discount coupon of $', discount, '.', '(10% of your purchase)')
elif spent > 150 and spent <= 210 :
    discount = spent * 0.12
    discount = float(discount)
    discount = round(discount, 2)
    print('You win a discount coupon of $', discount, '.', '(12% of your purchase)')
elif spent > 210 :
    discount = spent * 0.14
    discount = float(discount)
    discount = round(discount, 2)
    print('You win a discount coupon of $', discount, '.', '(14% of your purchase)')
else :
    print('Invalid input')


# - <font color='blue'>Exercise# 3:</font> Write a program that asks the user to enter a month (1 for January, 2 for February, and so on) and then prints the number of days in the month. For February, print “28 or 29 days”.
# 
#     - Enter a month:5 30 days
#     - Do not use a separate if/else branch for each month. Use Boolean operators. 
#    
#    
# | Sample Run | Sample Run | Sample Run|
# | :-- | :-- | :-- |
# |Enter a month: 6<br>30 days|Enter a month: 3<br>31 days|Enter a month: 2<br>28 or 29 days|
# 

# In[48]:


# Question 3
month = input('Enter a month: ')
month = int(month)

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    print(31, 'days')
elif month == 4 or month == 6 or month == 9 or month == 11 :
    print(30, 'days')
elif month == 2 :
    print(28, 'or', 29)
else : 
    print('Invalid input')


# - <font color='blue'>Exercise# 4:</font> Write a program that prompts the user to provide a single character from the alphabet.
# Print Vowel or Consonant, depending on the user input. If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error message.  
# 
# | Sample Run | Sample Run | Sample Run|Sample Run|
# | :-- | :-- | :-- |:--|
# |Enter one character: python<br>That input didn't have a valid length.|Enter one character: B<br>Consonant|Enter one character: e<br>Vowel|Enter one character: &<br>That was neither a vowel nor a consonant.|

# In[49]:


# Question 4
letter = input('Enter a single letter from the alphabet: ')
if letter.isalpha() :
    if len(letter) > 1 :
        print('ERROR')
    else :
        if letter in ('GWPUVX') :
            print('There is no arabic equivalent')
        else :
            print('There is an arabic equivalent')
else : 
    print('ERROR')
    


# In[ ]:




