class Student: 
    count = 0 ##class attribute
    def __init__(self, name, score):
        self.name = name ##屬性
        self.score = score
        self.__private_attr = "This is a private attribute"
        Student.count += 1
        self.__private_attr = "ABC University"  ##private attribute
        

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

    # def __init__(self, name, score, advisor):
    #     super().__init__(name, score)
    #     self.advisor = advisor

    def report(self):
        return super().report() + f", advisor: {self.advisor}"
   
    def set_school(self, school):
        self.__school = school  ##private attribute

    def get_school(self):
        return self.__school  ##private attribute
    def __str__(self):
        return super().__str__() + f", advisor: {self.advisor}, school: {self.__school}"
    


s1=Student("John", 90) 
s2=Student("Bob", 80)
s1.set_school("NTUT")
s2.set_school("NTU")
# print(s1.__school)  ##print the attributes of the object

print(s1.get_school())  ##print the attributes of the object
print(s2.get_school())  ##print the attributes of the object




