#include<iostream>
using namespace std;

class fish
{
public:
	fish()
	{
		cout << "fist_1" << endl;
	}
	virtual ~fish()
	{
		cout << "destory fist_1" << endl;
	}
};

class fist_2 : public fish
{
public:
	fist_2()
	{
		cout << "fist_2 " << endl;
	}
	~fist_2()
	{
		cout << "destory fist_2" << endl;
	}
};

void func1(fish* inputs)
{
	delete inputs;   // 初始化了 fish的 构造器。
}

int main()
{
	cout << " allocating a fist_2 on the free" << endl;
	fist_2* pfist_2 = new fist_2;

	cout << " deleting fist_2 new object" << endl;
 	func1(pfist_2);

	cout << "instanting a fist_2 on the stack" << endl;
	fist_2 fist_2_object;
	return 0;
}

