#include <string>
#include <iostream>
#include "Human.cpp"

using namespace std;

class Mahasiswa : public Human{
	
	private:
        string nim;
		string prodi;
		string fakultas;

	public:
		Mahasiswa(){
            this->nim = "";
            this->prodi = "";
            this->fakultas = "";
		}

		//getter dan setter
        void setNim(string nim){
			this->nim = nim;
		}

		string getNim(){
			return this->nim;
		}
        
		void setProdi(string prodi){
			this->prodi = prodi;
		}

		string getProdi(){
			return this->prodi;
		}

		void setFakultas(string fakultas){
			this->fakultas = fakultas;
		}

		string getFakultas(){
			return this->fakultas;
		}

		~Mahasiswa(){
		}
};