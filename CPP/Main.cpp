#include <bits/stdc++.h>
#include "SivitasAkademik.cpp"

using namespace std;

int main(){
	SivitasAkademik data;

    //Input Data
    data.setNik("32091485589373");
    data.setNama("Alifia Isti Fadhila");
    data.setGender("Perempuan");
    data.setNim("2904857");
    data.setFakultas("FPMIPA");
    data.setProdi("Ilmu Komputer");
    data.setUniv("Universitas Pendidikan Indonesia");
    data.setEmail("alifia@upi.edu");

    //Menampilkan Data
    cout << '\n' << "DATA MAHASISWA " << '\n';
    cout << "==============" << '\n';
    cout <<"NIK              : " << data.getNik()<<endl;
    cout <<"Nama             : " << data.getNama()<<endl;
    cout <<"Jenis Kelamin    : " << data.getGender()<<endl;
    cout <<"NIM              : " << data.getNim()<<endl;
    cout <<"Fakultas         : " << data.getFakultas()<<endl;
    cout <<"Program Studi    : " << data.getProdi()<<endl;
    cout <<"Asal Universitas : " << data.getUniv()<<endl;
    cout <<"Email Edu        : " << data.getEmail()<<endl;
    
	return 0;	
}