class Course:

	__nama_matkul = ''
	
	def __init__(self, nama_matkul = ''):
		self.__nama_matkul = nama_matkul
  
	#getter dan setter
	def setNama_matkul(self, nama_matkul):
		self.__nama_matkul = nama_matkul

	def getNama_matkul(self):
		return self.__nama_matkul