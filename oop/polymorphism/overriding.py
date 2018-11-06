class Student:
	def set_study_hours(self):
		self.study_hours = 40

	def display_study_hours(self):
		print(self.study_hours)

class Training(Student):
	# How to override base class
	def set_study_hours(self):
		self.study_hours = 60
		
	# How to override to base class
	def reset_study(self):
		super().set_study_hours()


student = Student()
student.set_study_hours()
print("Number of study hours: ", end ='')
student.display_study_hours()

newStudent = Training()
newStudent.set_study_hours()
print("The study hours for new: ", end='')
newStudent.display_study_hours()
# Overriding Call
newStudent.reset_study()
print("New study hours after reset: ", end='')
newStudent.display_study_hours()


