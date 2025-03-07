# def first():
#     yield("hello")
# x=first()
# print(x)
#generator object ko create krne k liye use krte he
def first():
    yield 1
    yield 2
    yield 3
x=first()
# print(x)
# print(list(x))
# print(next(x))
# print("hi")
# print("hello")
# print("welcome")
# print(next(x))
# print(next(x))
#advantages of generator:
#natural numbers
def natural(x):
    i=1
    while i<=x:
        yield i
        i=i+1
n=int(input("enter any number"))
p=natural(n)
# print(p)
# print(list (p))
print(next(p))
print(next(p))
for i in p:
    print(i)