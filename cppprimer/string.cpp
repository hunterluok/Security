#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	// const char*
	string  conststring = "hello world";
//	conststring.erase(4, 6);
//	cout << "constant string is: " << conststring << endl;
//	//指针是第一个字符
//	cout << "xx : " << *conststring << endl;
	
	string test = "irld, hehe wo";
	//string::const_iterator ele = find("w", 0);
//	size_t ap = test.find("j", 0);
//	if(ap != string::npos)
//	{
//		cout << "pos is " << ap << endl;
//		cout << string::npos << endl;
//		cout << "___" << endl;
//	}
	string::iterator iter = find(test.begin(), test.end(), 'w');
	if(iter != test.end())
	{
		cout << *iter << " iter " << endl;
		test.erase(iter);
		cout << "new test is " << test << endl;
	}

//	string strFromconst (conststring);
//	cout << " strFromconst is : " << strFromconst << endl;
//
//	string str2 ("hello world");
//	string copystring (str2);
//	cout << "copystring is :" <<  copystring << endl;
//
//	string strsplit (conststring,5);
//	cout << "strsplit is :" << strsplit << endl;
//
//	string strrepat (10, 'a');
//	cout << "strrepat is :" << strrepat << endl;
//
//	string s (10,'a');
//	cout << "strrepat is :" << s << endl;
//
//	string a = "a";
//	string b = "c";
//	string c = a.append(b);
//	cout << "c is " << c << endl;



	return 0;
}
