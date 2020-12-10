'''
create a car class which has model and version as inputs
will have to start,accelerate,stop,brake
'''

class car:
	def __init__(self,model,vers):
		self.model=model
		self.vers=vers
		self.speed=0
		self.engine=False

	def start(self,n):
		self.engine=True
		self.speed=n
	def acc(self,n):
		if self.engine:
			self.speed+=n
		else:
			print('start the vehicle first')
	def printer(self):
		print(self.model,'\t',self.vers,'\t',self.speed)		
	def brake(self,n):
		if self.speed-n >=0:
			self.speed-=n
		else:
			self.speed=0
	def stop(self):
		self.speed=0
				
c1=car('honda','2018')	
# c1.start(30)
c1.acc(20)
c1.printer()					

