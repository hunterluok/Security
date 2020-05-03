#include <iostream>
#include <string>
using namespace std;

int main()
{
	char* my = new char[3];
	string s = "ss";
	strcpy(my, s.c_str());
	cout << "s is " << my << endl;
	delete [] my;
	return 0;
}
