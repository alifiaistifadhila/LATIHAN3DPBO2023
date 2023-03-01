from Human import Human
from Course import Course
from Dosen import Dosen
from Mahasiswa import Mahasiswa
from ProgramStudi import ProgramStudi
from SivitasAkademik import SivitasAkademik

class main():
    data = Human()
    data.setNik(32091485589373)
    data.setNama("Alifia Isti Fadhila")
    data.setGender("Perempuan")
        
    mhs = Mahasiswa()
    # Inputan Data
    mhs.setNim(2904857)
    mhs.setFakultas("FPMIPA")
    
    dsn = Dosen()
    dsn.setNip(1748675436)
    dsn.setPend_terakhir("S3")
    dsn.setKeahlian("Pemrograman")
    
    sivitas = SivitasAkademik()
    sivitas.setUniv("Universitas Pendidikan Indonesia")
    sivitas.setEmail("alifia@upi.edu")
    
    course = Course()
    course.setNama_matkul("Desweb")
    
    prodi = ProgramStudi()
    prodi.setCourse(course)
    prodi.setMahasiswa(mhs)
    
    # Menampilkan Data
    print("DATA MAHASISWA")
    print("========================================")
    print("NIK              : " + str(data.getNik()))
    print("Nama             : " + str(data.getNama()))
    print("Jenis Kelamin    : " + str(data.getGender()))
    print("NIM              : " + str(mhs.getNim()))
    print("Fakultas         : " + str(mhs.getFakultas()))
    print("Asal Universitas : " + str(sivitas.getUniv()))
    print("Email Edu        : " + str(sivitas.getEmail()))
    
    print("\nDATA DOSEN")
    print("========================================")
    print("NIP                  : " + str(dsn.getNip()))
    print("Pendidikan Terakhir  : " + str(dsn.getPend_terakhir()))
    print("Keahlian             : " + str(dsn.getKeahlian()))
    print("Mata Kuliah          : " + str(prodi.getNama_matkul()))
    print("Program Studi        : " + str(prodi.getProdi()))
    print("Kode Program Studi   : " + str(prodi.getKode()))

#     print("Data PC\n")

#     print("Nama Processor : " + PC_in.getProcessor().getNama())
#     print("Harga          : " + str(PC_in.getProcessor().getPrice()))
#     print("Tipe disk      : " + PC_in.getDisk().getType())
#     print("Kapasitas disk : " + PC_in.getDisk().getCapacity())
#     print("Harga disk     : " + str(PC_in.getDisk().getPrice()))
#     print("Size RAM       : " + PC_in.getRam().getCapacity())
#     print("Harga RAM      : " + str(PC_in.getRam().getPrice()))
#     print("Harga Total    : " + str(PC_in.getTotalPrice()))

