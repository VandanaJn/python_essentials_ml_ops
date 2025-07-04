def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

counter=1
for n in fib():
    if counter>10:
        break
    print(n)
    counter+=1
print("list comprehension")
even=[n for n in range(1,10) if n%2==0 ]# list comprehension, eagerly creates list in memory
print (even)
print("lazy generation")
even=(n for n in range(1,10) if n%2==0 )# lazy generation, more memory efficient
for i in even:
    print(i)
    break

def reverse(iterator):
    for i in range(len(iterator)-1,-1,-1):
        yield iterator[i] 
print("reverse")        
items=reverse([1,2,3,4])
for item in items:
    print(item)

print(sum([8,9]))

def produce_1_10():
    for i in range(1,11):
        yield i

print("produce_1_10")
r=produce_1_10()
for i in r:
    print(i)

def fib1():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fb=fib1()
print("fib1")
for i in range(1,11):
    print(next(fb))
print("sumofsquares")
print(sum((n**2 for n in range(1,3))))
print("random")
import random
r=(random.random() for _ in range(100))
print(next(r))
r=(random.randint(1,100) for _ in range(100))
print(next(r))
r=(random.randrange(2,100,2) for _ in range(100))
print(next(r))
print(next(r))
print(next(r))
names=["a","b","c","d"]
print("choice")
print(random.choice(names))
print(random.choices(names,k=2))#can have duplicate
print(random.sample(names, k=2))





