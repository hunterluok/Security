#include<iostream>
#include<string>
using namespace std;

class human
{
private:
	string name;
	int age;
	friend void displayage(const human& person);

public:
	human(int sage, string mystring)
	: age(sage), name(mystring){}
};

void displayage(const human& person)
{
	cout << person.age << endl;
};

int main()
{
	human fri(22, "szs");
	cout << displayage(fri) << endl;
	return 0;
}