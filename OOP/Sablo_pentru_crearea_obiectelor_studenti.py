import datetime
class Student:
	__number = 1
	date_index = datetime.datetime.now()
	students = []
	
	def __init__(self, name, address, phone, course):
		self.name = name
		self.address = address
		self.phone = phone
		self.course = course
		self.index_number = str(self.__number + len(self.students))+'/'+ str(self.date_index.year)
		self.students.append(self.name)
		
	def getInfo(self):
		return f'Name: {self.name}'+','+f'address: {self.address}'+','+f'Phone: {self.phone}'+','+f'Course: {self.course}'+','+f'Index Number: {self.index_number}'
			
std1 = Student('Laurentiu Baluta', 'Catanesti 21', '07905709191', 'Python')
std2 = Student('Alina Baluta', 'Livezilor 12', '0746281846', 'Java')
std3 = Student('Damian Baluta', 'Logofat Stanciu Mihoveanu', '0727825225', 'HTML & CSS')

print(std1.getInfo())
print(std2.getInfo())
print(std3.getInfo())


