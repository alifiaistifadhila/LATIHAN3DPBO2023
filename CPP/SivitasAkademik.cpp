#include <string>
#include <iostream>
#include "Mahasiswa.cpp"

using namespace std;

class SivitasAkademik : public Mahasiswa{
	
	private:
		string univ;
		string email;

	public:
		SivitasAkademik(){
            this->univ = "";
            this->email = "";
		}

		//getter dan setter
        void setUniv(string univ){
			this->univ = univ;
		}

		string getUniv(){
			return this->univ;
		}

		void setEmail(string email){
			this->email = email;
		}

		string getEmail(){
			return this->email;
		}

		~SivitasAkademik(){
		}
};