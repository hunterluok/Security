#include<iostream>

using namespace std;

int main()
{
	int a = 0;
	cout << " a : " << ++a << endl;
	cout << -a++ << endl;
	cout << a << endl;

	// a = 2;
	int b = 1;

	a ^= b;
	b ^= a;
	a ^= b;
	cout << a << endl;
	cout << b << endl;
	return 0;

	6eebdad34fe48a72e353d4a837bbc2c5
}