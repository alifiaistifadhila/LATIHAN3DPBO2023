#include <string>
#include <iostream>

using namespace std;

class Human{
	
	private:
    	string nik;
		string nama;
		string gender;

	public:
		Human(){
            this->nik = "";
            this->nama = "";
            this->gender = "";
		}

		//getter dan setter
        void setNik(string nik){
			this->nik = nik;
		}

		string getNik(){
			return this->nik;
		}

        void setNama(string nama){
			this->nama = nama;
		}

		string getNama(){
			return this->nama;
		}

		void setGender(string gender){
			this->gender = gender;
		}

		string getGender(){
			return this->gender;
		}

		~Human(){
		}
};