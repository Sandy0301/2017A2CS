#27.08 Sandy
class Assessment:
    def __init__(self,t,m):
        self.__Title=t
        self.__MaxMarks=m
    def OutputAssessment(self):
        print(self.__Title,'Mark:',self.__MaxMarks)

class Course:
    def __init__(self,t,m):
        self.__CourseTitle=t
        self.__MaxStudents=m
        self.__NumberOfLessons=0
        self.__CourseLesson=[]
        self.__CourseAssessment=Assessment
    def AddL(self,t,d,r):
        self.__NumberOfLessons=self.__NumberOfLessons+1
        self.__CourseLesson.append(Lesson(t,d,r))
    def AddA(self,t,m):
        self.__CourseAssessment=Assessment(t,m)
    def OutputCourse(self):
        print(self.__CourseTitle, end='')
        print("Maximum number of students: ",self.__MaxStudents)
        for i in range (self.__NumberOfLessons):
            self.__CourseLesson[i].OutputLesson()
        self.__CourseAssessment.OutputAssessment()
class Lesson:
    def __init__(self,t,d,r):
        self.__LessonTitle=t
        self.__Duration=d
        self.__RequireLab=r
    def OutputLesson(self):
        print(self.__LessonTitle,self.__Duration,self.__RequireLab)
    
def main():
    MyCourse=Course('Economics',39)
    MyCourse.AddA('bussiness cycle',100)
    MyCourse.AddL('tax',71,True)
    MyCourse.AddL('money supply',86,False)
    MyCourse.AddL('inflation',61,False)
    MyCourse.OutputCourse()
main()



