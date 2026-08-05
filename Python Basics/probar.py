class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        #esto genera un error de tipo 

x = []

def f(a = x):
    a.append(1)
    print(a)
f()
f()

print(x)