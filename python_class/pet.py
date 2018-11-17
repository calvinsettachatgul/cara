class Pet:
    def __init__(self,name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        

def say_something():
    print("this is something")
    
say_something()

cal = Pet("cal", 5, "poodle" )

print(cal.name == "cal")
print(cal.age == 5)
print(cal.breed == 'poodle')