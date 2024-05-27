

class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.code = code

    def greet_student(self):
        greeting = f"Hello {self.first_name}, Welcome to {self.school}. Your code is {self.code}"
        return greeting
    
    def year_of_birth(self):
        return f"{self.first_name} was born in {2024 - self.age}"
    

    def student_fullname(self):
        return f"Your fullname is {self.first_name} {self.last_name}"
    

    # show a student initials, enroll a student -> increases enrollment by 1.
    
s1 = Student("Deborah","Cherotich",20,51)
s2 = Student("Jane","Wango",21,11)


print(s1.greet_student())
print(s2.greet_student())
print(s2.year_of_birth())
print(s1.student_fullname())


