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

class class_2 : protected class_1  //默认是私有继承 private
{
public:
	void func4()
	{
		func1();
		func2();
		func3();
	}
};

class class_3 : protected class_2 // 保护继承 使得 子类的子类可以 继承基类的方法，但是 private是不行的。
{
public:
	void func5()
	{
		func4();
		func1();
	}
};

int main()
{
	//class_2 class_2_obj;
	// class_2_obj.func4();
	// class_2_obj.func3();
	class_3 class_3_obj;
	class_3_obj.func5();
	//class_3_obj.func1();
	return 0;
}