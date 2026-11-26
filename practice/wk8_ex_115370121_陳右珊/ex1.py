##class of student

# Windsurf:Refactor |Explain

class Student: 
    count = 0 ##class attribute
    def __init__(self, name, score):
        self.name = name ##屬性
        self.score = score
        Student.count += 1

    def is_pass(self):
        if self.score>=60:
            return True
        else:
            return False
    def report(self):
        # stauts =self.is_pass
        return f"{self.name} : {self.score},pass:{self.is_pass()}"

    def __str__(self): ##print the object 
        return f"{self.name} : {self.score},pass:{self.is_pass()}"

class GradStudent(Student):
    def __init__(self, name, score, advisor):
        super().__init__(name, score)
        self.advisor = advisor

    def report(self):
        return super().report() + f", advisor: {self.advisor}"

# g1=GradStudent("Alice", 95, "Dr. Smith")
# g2=GradStudent("Eve", 85, "Dr. Johnson")

s1=Student("John", 90)
s2=Student("Bob", 80)
s3=Student("Alice", 70)
print("number of student:", Student.count)

# print(s1.report())
# print(s2.report())

# print(s1.name, s1.score)
# print(s2.name, s2.score)

# list =[s1, s2]
# print(s1.name, s1.score)
# print(s2.name, s2.score)

# students = [Student("John", 90), Student("Bob", 80)]

# for s in students:
#     print(s.report())
#     print(s)
