#class Grandparent:
    #height = 162
    #satiety = 100
    #age = 60

#class Parent(Grandparent):
    #age = 30

#class Student(Parent):
    #satiety = 0
    #age = 13


#class Worker:
    #satiety = 80
    #age = 28


#artem = Student()
#sasha = Worker()
#print(sasha.age)
#print(artem.satiety)
#print(sasha.satiety)
#print(artem.height)


#class Class1:
    #var = 20
    #def __init__(self):
        #self.var = 10

#class Class2(Class1):
    #def __init__(self):
        #print(self.var)
        #super().__init__()
        #print(self.var)
        #print(super().var)

"""""

class Grandparent:

   def about(self):
       print("Im grandparent")

     def about_myself(self):
        print("Im grandparent")

class Parent(Grandparent):
    def about_myself(self):
        print("Im parent")

class Child(Parent):
    def __init__(self):
       super().about()
       super().about_myself()

nick = Child()

"""
'''

class Computer:
    def calculate(self):
        print("Calculating")


class Display:
    def display(self):
        print("I display the image on the screen")

class SmartPhone(Display, Computer):
    pass



iphone = SmartPhone()
iphone.calculate()
iphone.display()


'''















