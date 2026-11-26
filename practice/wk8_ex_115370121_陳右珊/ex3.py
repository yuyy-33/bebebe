class Student: 
    count = 0  # 類別屬性 (class attribute)

    def __init__(self, name, score, advisor="None"):
        self.name = name 
        self.score = score
        self.advisor = advisor  # 修正 3：加入 advisor
        Student.count += 1
        self.__private_attr = "ABC University"  
        self.__school = "Not Set"  # 修正 4：初始化私有屬性

    def is_pass(self):
        return self.score >= 60

    def report(self):
        return f"{self.name} : {self.score}, pass:{self.is_pass()}, advisor: {self.advisor}"

    def __str__(self): 
        return f"{self.name} : {self.score}, pass:{self.is_pass()}, advisor: {self.advisor}, school: {self.__school}"

    @classmethod
    def get_count(cls):
        return cls.count

    def set_school(self, school):
        self.__school = school  

    def get_school(self):
        return self.__school  

    @staticmethod
    def info():
        return "This is a Student class"

    @staticmethod
    def check_gpa(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
s1 = Student("John", 90, "Dr. Smith") 
s2 = Student("Bob", 80, "Dr. Lee")

print(Student.info())         # 輸出: This is a Student class
print(Student.check_gpa(95))  # 輸出: A
print(Student.get_count())    # 修正 1：改用 get_count()，輸出: 2
print(s1)                     # 測試 __str__