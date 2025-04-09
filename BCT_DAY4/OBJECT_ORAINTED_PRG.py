#object oriented programming 


class Person:
    def _init_(self,name,age):
        print("in the construtor")
        self.name = name
        self.age = age
    def info(self):
        print(f"name is {self.name}, age is {self.age}")
class Student(Person):
    def _init_(self,name,age,id):
        super()._init_(name,age)
        self.id = id
    
    
# p1 = Person("sanu",19)
# p2 = Person("monisha",29)
# p1.info()
# p2.info()

#encapsulation
#setter and getter methods
class Account:
    def _init_(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance
    #polymorphism
class car:
    def sound():
            print("car is making sound")
class boat:
    def sound():
            print("boat is making sound")
class plane:
    def sound():
            print("plane is making sound")

#closure and decorator
# def outerFunc():
#     def innerFunc():
#         print("inside inner function")
#     return innerFunc
# func = outerFunc()
# func()

# def multiplier(a):
#     def multiply(b):
#         return a*b
#     return multiply
# double = multiplier(3)
# print(double(3))

def greet_decorator (func):
    def wrapper():
        print("Hello")
        func()
        print("Good Bye")
    return wrapper
@greet_decorator
def name():
    print("I am sayantan!!")
name()