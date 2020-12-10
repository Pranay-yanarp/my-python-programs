
'''
using class concept create vehicle parent class, create car,bike,truck child classes
using inheritence concept. pass model and version argument while initializing objects.
create input methods to pass inputs such as starting speed,acceleration,brake,stop

 '''

class vehicle:
	def __init__(self,model,vers):
		self.model=model
		self.vers=vers
		self.speed=0
		self.engine=False
		self.truck1=False

	def start(self,n):
		self.engine=True
		self.speed=n
	def acc(self,n):
		if self.engine:
			self.speed+=n
		else:
			print('start the vehicle first')	
	def brake(self,n):
		if self.speed-n >=0:
			self.speed-=n
		else:
			self.speed=0
	def stop(self):
		self.speed=0
	def printer(self):
		if self.truck1:

			print(self.model,'\t',self.vers,'\t',self.speed,'km/hr\t',self.load1,'tons')
		else:	
			print(self.model,'\t',self.vers,'\t',self.speed,'km/hr\t')



class car(vehicle):
	
	def __init__(self,model,vers):
		super().__init__(model,vers)
		
	def reverse(self,n):
		if self.speed == 0 and self.engine:
			self.speed=-n	
		else:
			print('first stop the car to reverse')


class bike(vehicle):
	def __init__(self,model,vers):
		super().__init__(model,vers)


class truck(car):
	def __init__(self,model,vers):
		super().__init__(model,vers)
		self.load1=0
		self.truck1=True
	def load(self,x):
		self.load1=x	

t1=truck('ashokleyland','2007')
t1.start(0)
t1.acc(30)
t1.stop()
t1.reverse(40)
t1.load(40)
t1.printer()
