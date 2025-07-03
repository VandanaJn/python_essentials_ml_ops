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

even=[n for n in range(1,10) if n%2==0 ]# list comprehension, eagerly creates list in memory
print (even)
even=(n for n in range(1,10) if n%2==0 )# lazy generation, more memory efficient
for i in even:
    print(i)
    break
