#include <iostream>
using namespace std;


template <typename T>
T& fus(T&a, T& b)
{
	if(a > b)
		return a;
	else
		return b;
}

template<typename T>
void show(const T& a, const T& b)
{
	cout << "a :" << fus(a, b) << endl;
}


template<typename T>
void shows(const T& a)
{
	cout << "xx :" << a << endl;
}


int main()
{
	// typename T x = 0;
	show(4, 3);
	// int x =  fus<int>(2, 3);  // 这里不能直接调用。
	// cout << fus<int>(2,3) << endl;
	// shows(x);
	// cout << "T X : " <<  x << endl;
	return 0;
}