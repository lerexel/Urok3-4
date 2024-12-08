import random


class Human:

   def __init__(self, name='Human', job=None, car=None):
       self.name = name
       self.money = 100
       self.job = job
       self.car = car

   def work(self):
       self.money+= self.job.salary
       print(f'{self.name} worked for 8 hours and get {self.job.salary}$')



job_list = {
"Java developer":
{"salary":50, "gladness_less": 10 },
"Python developer":
{"salary":40, "gladness_less": 3 },
"C++ developer":
{"salary":45, "gladness_less": 25 },
"Content creator":
{"salary":70, "gladness_less": 1 },
}

class Job:

    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]



class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        print(f"Names of {self.brand} passengers: ")
        for passenger in self.passengers:
            print(passenger.name)

sasha = Human('Sasha', Job(job_list))
sasha.work()
print(sasha.money)






