#include<iostream>
#include<string>
using namespace std;

struct human
{
	human(int sage,string sname)
	:age(sage),name(sname) {}

	int getage()
	{
		return age;
	}

private:
	int age;
	string name;
};

int main()
{
	human myhuamn(22,"xxx");
	cout << myhuamn.getage() << endl;
	return 0;
}