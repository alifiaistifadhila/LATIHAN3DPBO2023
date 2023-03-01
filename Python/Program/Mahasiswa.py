from SivitasAkademik import SivitasAkademik

class Mahasiswa(SivitasAkademik):
	__nim = 0
	__prodi = ''
	__fakultas = ''
	
	def __init__(self, nim = 0, prodi = '', fakultas = ''):
		self.__nim = nim
		self.__prodi = prodi
		self.__fakultas = fakultas

	#getter dan setter
	def setNim(self, nim):
		self.__nim = nim

	def getNim(self):
		return self.__nim

	def setProdi(self, prodi):
		self.__prodi = prodi

	def getProdi(self):
		return self.__prodi

	def setFakultas(self, fakultas):
		self.__fakultas = fakultas

	def getFakultas(self):
		return self.__fakultas