#include<iostream>
#include<string>
using namespace std;

class fist
{
public:
	void get_1()
	{
		cout <<" hello world" << endl;
	}

	void get_1(bool inputs)
	{
		if(inputs)
			cout << "e you know" << endl;
		else
			cout << " let's go,ababa" << endl;
	}


	void get_2(bool inputs)
	{
		//cout << "hello future" << endl;
		if(inputs)
			cout << "hello future! " << endl;
		else
			cout << "hello world. lk" << endl;
	}
};

class newfish : public fist
{
public:
	using fist::get_1;  
	void get_1()
	{
		cout << "lk ,future,xxxx" << endl;
	}
};


int main()
{
	newfish text;
	cout << " ee" << endl;
	text.get_1();
	text.get_2(false);
	text.get_1(false);

	// text.fist::get_1(true); // 隐藏了基类的函数。

	cout << " ok,let's go" << endl;
	return 0;
}