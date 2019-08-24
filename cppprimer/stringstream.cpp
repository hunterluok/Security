#include<iostream>
#include<sstream>
#include<fstream>
using namespace std;

int main()
{
	int age = 0;
	cout << "cout a age : " << endl;
	cin >> age;

	cout << "age : " << age << "size of :" << sizeof(age) << endl;

	stringstream mstr;
	mstr <<  age;

	string myage;
	mstr >> myage;

	cout << "myage :" << myage << "size of :  " <<sizeof(myage) << endl;

	return 0;
}
