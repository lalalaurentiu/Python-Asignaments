# Creați o clasă care se va utiliza pentru instanţierea obiectelor în formă de cub. Definiți o metodă pentru calcularea volumului unui cub și o altă metodă pentru calcularea lungimii totale a tuturor laturilor unui cub.
# Plasați aceste metode în fire, executați mai întâi a doua metodă cu fire și, după finalizarea cu succes, executați-o pe prima. În timpul acestui proces, firul principal trebuie oprit.
# Creați două obiecte peste care se vor apela fiecare din metodele create.
# Afișați rezultatele acestor metode cu comanda print.
import threading

class Cube:
	def __init__(self, radius):
		self.radius = radius
		self.volume = 0
		self.totalLeghtSides = 0
		
	def getVolume(self):
		self.volume = self.radius ** 3
		return self.volume
		
	def getTotalLeghtSides(self):
		self.totalLeghtSides = 12 * self.radius
		return self.totalLeghtSides
		
if __name__ == '__main__':
	c1 = Cube(10)
	c2 = Cube(13)
	for cube in c1, c2:
		t1 = threading.Thread(target=cube.getTotalLeghtSides)
		t2 = threading.Thread(target=cube.getVolume)
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		
		print(f'Volume is: {cube.volume}')
		print(f'Total leght of all sides is: {cube.totalLeghtSides}')


