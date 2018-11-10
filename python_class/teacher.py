from new_module import module_calvin

class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    
    def print_module_calvin(self):
        print(module_calvin.calvin_variable)
    
john = Teacher("john", 40, "CS")

print(john.name == "john")

john.print_module_calvin()