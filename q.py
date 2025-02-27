# x=4
# x=lambda p:[[j for j in range(1,p)] for k in range (p)]
# print(x(x))

# for i in range (4):
#     print("hello")

# for _ in range (4):
#     print("hello")


#lambda with map
# l1=[1,2,3,4]
# def my_sqr(n):
#     return n**2
# x=list(map(my_sqr,l1))
# print(x)

# l1=[1,2,3,4]
# x=list(map(lambda x:x**2,l1))
# print(x)

# l1=[1,2,3,4]
# x=list(map(lambda x:"even" if x%2==0 else "odd",l1))
# print(x)
# l1=[1,2,3,4]
# x=list(filter(lambda x:x if x%2==0 else None ,l1))
# print(x)
from functools import reduce
# l1=[1,2,3,4]
# x=reduce(lambda x,y:x if x>y else y,l1)
# print(x)
l1=[1,2,3,4]
x=reduce(lambda x,y:x if x<y else y,l1)
print(x)