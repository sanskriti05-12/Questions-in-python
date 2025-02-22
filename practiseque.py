# wap to check given number is postive
x=eval(input("enter a number"))
if(x>=0):
    print("number is positive")


# wap to check given number is positive or negative

x=eval(input("enter a number"))
if(x>=0):
    print("number is positive")
else:
    print("number is negative")

# Example 9:Write a program to find squre root of given no
x=int(input("enter a number"))
sqareroot=x**(0.5)
print(sqareroot)

# Example 4:Write a program to swap two variables without using third variable.
# Example 5:Write a program to swap two variables using third variable.
# x=eval(input("enter a number"))
# y=eval(input("enter a second variable"))
# temp=x
# x=y
# y=temp
# print(x)
# print(y)
# Example 6:Write a program to swap two variables using using Addition and Subtraction. 
x=eval(input("enter a number"))
y=eval(input("enter a second variable"))
x=x+y-x

print(x)
print(y)

# Example 10:Write a program to find largest no among the three inputs numbers.
x=eval(input("enter a number"))
y=eval(input("enter a number"))
z=eval(input("enter a number"))
if(x>y and x>z):
    print("x is big")
elif(y>z and y>x):
    print("y is big")
else:
    print("z is big")

# Example 11: Write a program to find area of triangle. (1/2* hight*base)
x=eval(input("enter a height"))
y=eval(input("enter a base"))
z=1/2*(x*y)
print(z)



# Example 12: Write a program to find area of square.
x=eval(input("enter a number"))
square=x*x
print(square)


# Example 13: Write a program to find given year is leep year or not
x=int(input("enter a year"))
if((x%4==0 or x%400==0) and x%100!=0):
   print("its a leap year")
else:
   print("its not a leap year")