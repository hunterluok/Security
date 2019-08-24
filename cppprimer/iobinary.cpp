#include<iostream>
#include<string>
#include<iomanip>
#include<fstream>
using namespace std;


struct human
{
	human () {};
	human (const char* name, int inage, const char* indob): age(inage)
	{
		// sname = name;
		// sindob = indob;
		strcpy(sname, name);
		strcpy(sindob, indob);
	}

	char sname[20];
	int age;
	char sindob[20];
	
};

int main()
{
	human input("lk future", 22, "sangfor");

	ofstream fsout("binary.bin", ios_base::out | ios_base::binary | ios_base::in);
	if(fsout.is_open())
	{
		cout << "writing one object :" << endl;
		fsout.write(reinterpret_cast<const char*>(&input), sizeof(input));
		fsout.close();
	}

	ifstream fsin ("binary.bin", ios_base::in | ios_base::binary);
	if(fsin.is_open())
	{
		human somepeople;
		fsin.read((char*)&somepeople, sizeof(somepeople));
		cout << "read data :" << endl;
		cout << " name :" << somepeople.sname << endl;
		cout << "age :" << somepeople.age << endl;
		cout << "out : " << somepeople.sindob << endl;
		fsin.close();

	}

	return 0;
}