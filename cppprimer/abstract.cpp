#include<iostream>
using namespace std;


class class_1
{
public:
	// virtual void swim() = 0;
	void swim()
	{
		cout << "xxxx" << endl;  
	}   
};

class class_2: public class_1
{
public:
	void swim()
	{
		cout << "hello 1" << endl;
	}
};

class class_3: public class_1
{
public:
	void swim()
	{
		cout << "hello future" << endl;
	}
};


void funct_1(class_1& inputs)  // 如果是 class_1 中的swim是虚函数 则调用对应的子类的函数。
{
	inputs.swim();   // 如果class_1 的swim不是虚函数 ，则调用基类的 swim()函数。
}

int main()
{
	// class_1 class_1_obj;
	class_2 class_2_obj;
	class_3 class_3_obj;

	class_2_obj.swim();
	class_3_obj.swim();

	funct_1(class_3_obj);


	return 0;
}