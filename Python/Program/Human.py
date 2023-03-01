class Human:

	__nama = ''
	__nik = 0
	__gender = ''
	
	def __init__(self, nama = '', nik = 0, gender = ''):
		self.__nama = nama
		self.__nik = nik
		self.__gender = gender
  
	#getter dan setter
	def setNama(self, nama):
		self.__nama = nama

	def getNama(self):
		return self.__nama

	def setNik(self, nik):
		self.__nik = nik

	def getNik(self):
		return self.__nik

	def setGender(self, gender):
		self.__gender = gender

	def getGender(self):
		return self.__gender