# Example 1: Write a program to display n natural numbers. (In Horizontal-1,2,3,4,5…….. )
# n=int(input("enter a number"))
# i=1
# while(i<=n):
#     print(i,end =", ")

# Example 2: Write a program to calculate the sum of numbers.

# Example 3: Write a program to find even no. (2,4,6,8,….)
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i=i+1
# Example 4: Write a program find odd no.(1,3,5,7,9,……)
# Example 5: Write a program to find factorial of given no.
# Example 6: Write a program to print your names ten times. 
# Example 7: Write a program to find how many vowels and consonants are present in strings.
# Example 8: Write a program to add 5 in each elements in given list. [10,20,30,40,50]
# Example 9: Write a program to add 5 in each elements in given tuple. (10,20,30,40,50)
# Example 10: Write a program to create a list from given string
# x=int(input("enter a number"))
# n=x
# if x==x[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
# rev=0
# while x>0:
#     lastdigit=x%10
#     rev=rev*10+lastdigit
#     x=x//10
# if n==rev:
#     print("palindrome")
# else :
#     print("not palindrome")
# fibonacci series
n=15
a=0
b=1
while a<=n:
    print(a)
    a,b=b,a+b