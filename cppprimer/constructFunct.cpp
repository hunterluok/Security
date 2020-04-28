#include<iostream>
using namespace std;


class human
{
private:
	int age;

public:
	human()
	{
		int age=0;
	}

	human(int sage) :age(sage)  // 附带初始化列表。
	{
	}

	void setage(int data)
	{
		age = data;
		cout << "ee " << age <<endl;
	}

	int getage()
	{
		cout << "human age :" << endl;
		return age;
	}

};


int main()
{
	human first(12);

	human second;
	second.setage(233);

	cout << "hello" << first.getage() << endl;

	cout << "hello age" << second.getage() << endl;
	return 0;
}