# Este necesar să creați un șablon pentru crearea obiectelor de tip Student. Fiecare Student trebuie să aibă următoarele proprietăți: 
# name
# address
# phone
# course
# index_number
# Fiecare obiect care reprezintă un student trebuie să aibă următorul comportament (metodă):
# getInfo()
# Metoda getInfo () trebuie să returneze informații cumulative despre un student ca valoare de returnare (de exemplu, Name: John Benson, address: High Park 36, Phone: (507) 833-3567, Course: Geography, Index number: 123/007).
# Ca să realizați șablonul pentru crearea obiectelor, utilizați o clasă.
# În final, pe baza șablonului realizat, creați trei obiecte care să reprezinte trei studenţi cu datele dorite. Peste cele trei obiecte create, apelați metoda de imprimare a datelor - getInfo() și afișați informațiile cu comanda print.
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


