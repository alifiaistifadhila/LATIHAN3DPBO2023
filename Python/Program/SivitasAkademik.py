from Human import Human

class SivitasAkademik(Human):
	__univ = ''
	__email = ''
	
	def __init__(self, univ = '', email = ''):
		self.__univ = univ
		self.__email = email

	#getter dan setter
	def setUniv(self, univ):
		self.__univ = univ

	def getUniv(self):
		return self.__univ

	def setEmail(self, email):
		self.__email = email

	def getEmail(self):
		return self.__email