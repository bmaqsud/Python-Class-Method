class Student:
    def __init__(self, name:str):
        self.name=name
        self.grade=[]
        
    def add_grade(self, grade):
        self.grade.append(grade)

    def get_average(self):
        get_average_grade=sum(self.grade)/len(self.grade)
        return get_average_grade
    
student=Student("Ali")

student.add_grade(5)
student.add_grade(3)
student.add_grade(3)
average=student.get_average()

a=f"{student.name} ning o'rtaacha bahosi >> {average}"
print(a)