name1=input('please input student name:')
major1=input('please input student major BMS or BMI:')
self_homework_score1=input('please input student self homwork score:')
group_project_score1=input('please input student group project score:')
self_exam_score1=input('please input student self exam score:')
#collect the student information
class Student:
    def __init__(self,name,major,self_homework_score,group_project_score,self_exam_score):
        self.name = name
        self.major = major
        self.self_homework_score = self_homework_score
        self.group_project_score = group_project_score
        self.self_exam_score =self_exam_score
    #try to define a function that can collect the student information
    def print_student(self):
        print(f'student name:{self.name},major:{self.major},self_homework_score:{self.self_homework_score},group project score:{self.group_project_score}/100,self exam score:{self.self_exam_score}/100')
#try to print it
student1=Student(name=name1,major=major1,self_homework_score=self_homework_score1,group_project_score=group_project_score1,self_exam_score=self_exam_score1)
student1.print_student()
