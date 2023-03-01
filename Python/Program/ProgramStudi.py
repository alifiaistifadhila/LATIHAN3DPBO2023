from Course import Course
from Mahasiswa import Mahasiswa

class ProgramStudi(Course, Mahasiswa):

	__nama_prodi = ''
	__kode = 0
	Course = Course()
	Mahasiswa = Mahasiswa()
	
	def __init__(self, nama_prodi = '', kode = 0, Course = Course, Mahasiswa = Mahasiswa):
		self.__nama_prodi = nama_prodi
		self.__kode = kode
		self.__Course = Course
		self.__Mahasiswa = Mahasiswa
  
	#getter dan setter
	def setNama_prodi(self, nama_prodi):
		self.__nama_prodi = nama_prodi

	def getNama_prodi(self):
		return self.__nama_prodi

	def setKode(self, kode):
		self.__kode = kode

	def getKode(self):
		return self.__kode

	def setCourse(self, Course):
		self.__Course = Course

	def getCourse(self):
		return self.__Course

	def setMahasiswa(self, Mahasiswa):
		self.__Mahasiswa = Mahasiswa

	def getMahasiswa(self):
		return self.__Mahasiswa