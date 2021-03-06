class Person:
  species = "homosapiens"
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
  def say_hello(self):
    return "hello my name is {} {}".format(self.firstname, self.lastname)

calvin = Person("calvin", "settachatgul")
ramsey = Person("ramsey", "darling")
person3 = Person("person3", "person3last")
person4 = Person("person4", "person4last")

people = [calvin, ramsey, person3, person4]

print("describe Person new a person has a first name and last name")
print(calvin.firstname == "calvin")
print(calvin.lastname == "settachatgul")
print(ramsey.firstname == "ramsey")
print(ramsey.lastname == "darling") 

print("describe Person say_hello expect a person to say hello and return 'hello my name is firstname lastname'")
print(calvin.say_hello() == 'hello my name is calvin settachatgul')
print(ramsey.say_hello() == 'hello my name is ramsey darling')

# iterate through these people and print the first name and last name
# execute the say_hello function
# arr =[];
# for( var i=0; i< arr.length; i++){
# do some stuff
# }

for person in people:
  print(person.firstname)
  print(person.lastname)
  print(person.say_hello())
  print(person.species)