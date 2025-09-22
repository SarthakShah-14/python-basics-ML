a=5
a='h'
print(a)
a=input("Enter no")

#day 3
n=5
if(n==5):
    print("true")

    n=3
if(n==0):
    print("n is 0")
elif(n<0):
    print("n is negative")

else:
    print("n is positive")

    
n=int(input("Enter n"))
if(n==0):print("n is 0")
else:print("n is positive")

n=int(input("Enter n"))
print("n is +ve") if(n>0) else print("n is -ve")

#for loop
for i in "Python":
    print(i)

for i in range(20,30):
     print(i)

for i in range(20,30,5):
     print(i)

for i in range(20,30):
    if(i==25):
     break
     print(i)

for i in range(20,30):
    if(i==25):
     pass
     print(i)

#while loop
n=1
while n<5:
    print(n)
    n=n+1

#floor division
print(5/2)
print(5//2)


#identity operators is & is not
a=["Hello","Python"]
b=["Hello","Python"]
c=a
print(a is c)
print(b is c)
print(id(a))
print(id(b))#here id is not same so different will come although the text is same

a=5
b=5
c=a
print(a is c)
print(b is c)
print(id(a))
print(id(b))#here id is  same so same will come though the value is same

#membership operator in & not in
a=["Apple","Banana","Mango"]
print("Banana" in a)
print("Banana" not in a)

#imp function-user define function
#without parameter
def show():
    print("Show called")
show()

#udf with parameters
def calc_area(l,b):
    return l*b
res=calc_area(3,5)
print(res)

#positional parameter
def greeting(msg,name):
    print(f"{msg} to {name}")
greeting("welcome","Manish")

#here the position of msg and name is changed in print
def greeting(msg,name):
    print(f"{name} to {msg}")
greeting("welcome","Manish")


def greeting(name,msg="welcome"):
    print(f"{msg} to {name}")
greeting("Manish")

#key parameter
def greeting(name,msg):
    print(f"{msg} to {name}")
greeting(name="manish",msg="welcome")

def greeting(name,msg):
    print(f"{msg} to {name}")
greeting(msg="welcome",name="manish")

#sequences
list=[10,20,30,40]
print(list)

list=[10,20,30,40,"Python"]
print(list)

#indexing
list=[10,20,30,40,"Python"]
print(list[4])

list=[10,20,30,40,"Python"]
print(list[-2])

#slicing
list=[10,20,30,40,"Python"]
print(list[3:5])

list=[10,20,30,40,"Python"]
print(list[:3])

list=[10,20,30,40,"Python"]
print(list[3:])

list=[10,20,30,40,"Python"]
list.append("Welcome")
print(list)


list=[10,20,30,40,"Python"]
list.insert(1,100)
print(list)

list=[10,20,30,40]
print(sum(list))

list=[10,20,30,40]
print(max(list))

list=[10,20,30,40]
print(min(list))

list=[40,20,30,40]
print(sorted(list))

list=[40,20,30,40]
print(sorted(list,reverse=True))

list=[40,20,30,40]
for i in list:
    print(i)

#tuple-immutable-append will not come
t=(2,4,6,8,10)
print(t)
type(t)

#dictionary
di={1:"Manish",2:"Bharat"}
print(di)

di={1:"Manish",2:"Bharat"}
print(di.keys())#for printing keys


di={1:"Manish",2:"Bharat"}
print(di.values())#for printing values

di={1:"Manish",2:"Bharat"}
for keys in di:
    print(keys)

di={1:"Manish",2:"Bharat"}
for keys in di:
    print(keys,"--->",di[keys])

di={1:"Manish",2:"Bharat"} 
di[1]="Rajesh"
print(di)

di={1:"Manish",2:"Bharat"} 
di.app

#set
s1={1,2,3,4}
s2={2,4,6,8}
print(s1)
print(s2)
print("after intersection")
s1.intersection(s2)
print(s1)

#day 4 python with oops
#udf with arguments
def func1(*args):
    result=1
    for i in args:
        result=result*i
    return result
s=func1(2,4,6,8)
print(s)

    #for deleting the function
    # 
del func1
print(func1(2,4,6,8))

#lambda function
add=lambda x,y:x+y
print(add(3,5))


nums=[1,2,3,4,5,6,7,8]
evens=list(filter(lambda x:x%2==0,nums))#filter(eqn,input)
print(evens)

nums=[1,2,3,4,5,6,7,8]
evens=list(map(lambda x:x*2,nums))
print(evens)

#oops in python
class abc:
    pass

class abc:
    def func1(self):#self keyword is used if the function is created in same class
        print("Class abc called")
obj=abc()
obj.func1()

#constructor-also known as "initalizers" in python
class xyz:
    name=''
    def __init__(self,name):
        self.name=name
    def func1(self):
        print(f"My Name is {self.name}")
obj1=xyz("Manish")
obj1.func1()
    
#inheritance
#single-simple inheritance
class parent:
    def func1(self):
        print("This is parent class method")
class child(parent):
    def func2(self):
        print("This is child class method")
obj=child()
obj.func1()
obj.func2()

#multiple inheritance
class parent1:
    def func1(self):
        print("This is parent class method")
class parent2:
    def func2(self):
        print("This is parent 2 class") 
class child(parent1,parent2):
    def func3(self):
        print("This is child class method")
obj=child()
obj.func1()
obj.func2()
obj.func3()


#multilevel inheritance
class grandparent:
    def func1(self):
        print("This is grandparent class method")
class parent1(grandparent):
    def func2(self):
        print("This is parent class method")
class child(parent1):
    def func3(self):
        print("This is child class method")
obj=child()
obj.func1()
obj.func2()
obj.func3()

#hybrid inheritance
class grandparent:
    def func1(self):
        print("This is grandparent class method")
class parent1(grandparent):
    def func2(self):
        print("This is parent class method")
class parent2:
    def func3(self):
        print("This is parent 2 class") 
class child(parent1,parent2):
    def func4(self):
        print("This is child class method")
obj=child()
obj.func1()
obj.func2()
obj.func3()
obj.func4()

#polymorphism
class abc:
    def show(self):
        print("abc class called")
class xyz(abc):
    def show(self):
        print("This is xyz class")
obj
obj=xyz()
obj.show()


#runtime polymorphism-theoretical concept
class abc:
    def show(self):
        print("abc class called")
class xyz(abc):
    def show(self):
        print("This is xyz class")

obj1=abc()
obj=obj1
obj.show()

obj2=xyz()
obj=obj2
obj.show()

#runtime polymorphism-practical concept
class abc:
    def show(self):
        print("abc class called")
class xyz(abc):
    def show(self):
        print("This is xyz class")

n=int(input("enter a value"))
if n==1:
    obj1=abc()
    obj=obj1
    obj.show()
else:
    obj2=xyz()
    obj=obj2
    obj.show()

    