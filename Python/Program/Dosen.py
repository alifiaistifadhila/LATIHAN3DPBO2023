from SivitasAkademik import SivitasAkademik

class Dosen(SivitasAkademik):
	__nip = 0
	__pend_terakhir = ''
	__keahlian = ''
	
	def __init__(self, nip = 0, pend_terakhir = '', keahlian = ''):
		self.__nip = nip
		self.__pend_terakhir = pend_terakhir
		self.__keahlian = keahlian

	#getter dan setter
	def setNip(self, nip):
		self.__nip = nip

	def getNip(self):
		return self.__nip

	def setPend_terakhir(self, pend_terakhir):
		self.__pend_terakhir = pend_terakhir

	def getPend_terakhir(self):
		return self.__pend_terakhir

	def setKeahlian(self, keahlian):
		self.__keahlian = keahlian

	def getKeahlian(self):
		return self.__keahlian