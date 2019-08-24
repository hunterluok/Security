#include<iostream>
using namespace std;

class class_1
{
public:
	class_1()
	{
		cout << " hello class_1" << endl;
	}
	~class_1()
	{
		cout << "bye class_1" << endl;
	}
};

class class_2
{
protected:
	class_1 object_class_1;

public:
	class_2()
	{
		cout << "hello class_2" << endl;
	}
	~class_2()
	{
		cout << " good bye class_2" << endl;
	}

};

class class_3
{
public:
	class_3()
	{
		cout << " hello class_3" << endl;
	}
	~class_3()
	{
		cout << "bye class_3" << endl;
	}

};


class class_4 : public class_2 // 继承了 所以先实例化 base 类的。
{
private:
	class_3 object_class_3;

public:
	class_4()
	{
		cout << " hello class_4" << endl;
	}
	~class_4()
	{
		cout << "bye class_4" << endl;
	}
};

int main()
{
	class_4 object_class_4;
}


