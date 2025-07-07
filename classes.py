class Dog:
    is_Animal=True

    def __init__(self):
        self.color="white"

    def bark(self):#self can be named anything
        print("woof!")

d=Dog()
a=Dog()
a.is_Animal=False
print(a.is_Animal)
print(d.is_Animal)
d.is_Animal=True
a.is_Animal=False
print(a.is_Animal)
print(d.is_Animal)
d.bark()
Dog.is_Animal=False

print(a.is_Animal)
print(d.is_Animal)

c=Dog()
print(c.is_Animal)#became false by default
c.is_Animal=True
print(Dog.is_Animal)
# print(Dog.color) does not work now as it not a class level attribute
print(c.is_Animal)
print(c.color)

from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    grade: int

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name==other.name and \
            self.age==other.age \
                and self.grade==other.grade
        return False
    def __call__(self):
        return self.name

#dataclass gives many boiler plate methods line init, eq, hash etc

s1=Student(name="Alice", age=16, grade=10)
s2=Student(name="Alice", age=16, grade=10)
s3=Student(name="Alice", age=16, grade=11)
print("s1.__eq__(s2)",s1.__eq__(s2))
print("s1.__eq__(s3)",s1.__eq__(s3))
print(s1.__str__())
print(s1.__call__())
print(s1())# can call object like a function, calls __call__ 

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
r=Reverse("river")
for c in r:
    print(c)

print(r.__dict__)

class Base:
    def __init__(self):
        self.__method1()
    def method1(self):
        print("base method1")

    __method1=method1#name mangling
class SubClass(Base):
    def method1(self):
        print("subclass method1")

a1=Base()
a2=SubClass()
a1.method1()
a2.method1()


class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        super().greet()
        print("B")

class C(A):
    def greet(self):
        super().greet()
        print("C")

class D(B):
    def greet(self):
        super().greet()
        print("D")

class E(D, C):
    def greet(self):
        super().greet()
        print("E")


E().greet()
print(E.mro())#C3 Linearization

from pydantic import BaseModel
class Person(BaseModel):
    name:str
    age:int

    model_config={"frozen":True}

p=Person(name="Alicia", age="20")
# p.name="John" does not work, gives validation error
print(type(p.age))

