#include<iostream>
using namespace std;

class fist
{
public:
	virtual void mov()  // 使得 
	{
		cout << " hello first" << endl;
	}
};

class second : public fist
{
public:
	void mov()
	{
		cout << "hello second" << endl;
	}
};


//void funct(fist& fist_object)
//{
//	fist_object.mov();
//}

void funct2(fist& second_obj_obj)  // 这里的用法，base的virtual 就不会被调用了。
{
	second_obj_obj.mov();
}


int main()
{
	second second_obj;
	second_obj.mov();
	funct2(second_obj);
	return 0;
}