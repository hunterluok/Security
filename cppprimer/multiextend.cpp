#include<iostream>
using namespace std;

class class_1
{
public:
	void func1()
	{
		cout << "hello class_1" << endl;
	}
};

class class_2
{
public:
	void func2()
	{
		cout << "hello class_2" << endl;
	}
};

class class_3
{
public:
	void func3()
	{
		cout << "hello class_3" << endl;
	}
};

class class_4: public class_1,public class_2,class_3  // privated protected 两种方法可以试试。
{
public:
	void func4()
	{
		cout << "hello class_4" << endl;
		func1();
		func3();  //没法 在 class_4的实例中进行访问 但是可以再这里进行访问。
	}
};

int main()
{
	class_4 object_class_4;
	object_class_4.func4();  
	// object_class_4.func3();
	object_class_4.func2();
	// object_class_4.func3();
	return 0;
}


