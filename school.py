class Teacher:
    def teach(self):
        print ("преподаватель учит")
class School:
    def __init__(self, new_teacher):
        self.teacher = new_teacher
    def start_lesson(self):
        self.teacher.teach()

my_teacher = Teacher()
my_school = School(my_teacher)