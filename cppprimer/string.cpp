#include<iostream>
#include <string>
using namespace std;

int main()
{
	const char* conststring = "hello world";
	cout << "constant string is: " << conststring << endl;
	cout << "xx : " << *conststring << endl;

	string strFromconst (conststring);
	cout << " strFromconst is : " << strFromconst << endl;

	string str2 ("hello world");
	string copystring (str2);
	cout << "copystring is :" <<  copystring << endl;

	string strsplit (conststring,5);
	cout << "strsplit is :" << strsplit << endl;

	string strrepat (10, 'a');
	cout << "strrepat is :" << strrepat << endl;

	string s (10,'a');
	cout << "strrepat is :" << s << endl;

}