#include <iostream>
using namespace std;

template<typename T> class mystacks
{
public:
	mystacks(int size)
	{
		maxsize = size;
		top = -1;
		elements = new T[maxsize];
	}
	~mystacks()
	{
		delete [] elements;
	}
	bool pushs(T value);
	T pops();

	int show()
	{
		return top;
	}

private:
	int top;
	T *elements;
	int maxsize;
	
};

template<typename T> bool mystacks<T>::pushs(T value)
{
	if(top == maxsize)
	{
		cout << " man le " << endl;
		return false;
	}
	elements[++top] = value;
	return true;
}

template<typename T> T mystacks<T>:: pops()
{
	if(top == -1)
		exit(-1);
	return elements[top--];
}

int main()
{
	mystacks<int> mystack = mystacks<int>(2);

	// mystack.pushs(23);
	// mystack.pushs(56);
	// mystack.pushs(11);
	// mystack.pushs(23);
	// mystack.pushs(56);
	// mystack.pushs(11);

	mystack.pushs(23);
	mystack.pushs(56);
	mystack.pushs(11);

	cout << " top : " << mystack.show() << endl;

	cout << mystack.pops() << " --pop" << endl;
	mystack.pushs(4);
	cout << mystack.pops() << " --pop" << endl;
	cout << mystack.pops() << " --pop" << endl;
	mystack.pushs(87);
	mystack.pushs(98);
	cout << mystack.pops() << " --pop" << endl;
	cout << mystack.pops() << " --pop" << endl;
	cout << mystack.pops() << " --pop" << endl;

}