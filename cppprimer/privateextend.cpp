#include<iostream>
using namespace std;

class class_1
{
public:
	void func1()
	{
		cout << "hello func1" << endl;
	}
	void func2()
	{
		cout << "hello func2" << endl;
	}
	void func3()
	{
		cout << "hello func3" << endl;
	}
};

class class_2 : private class_1  //默认是私有继承 private
{
public:
	void func4()
	{
		func1();
		func2();
		func3();
	}
};


int main()
{
	class_2 class_2_obj;
	class_2_obj.func4();
	// class_2_obj.func3();
	return 0;
}