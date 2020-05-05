# include<iostream>
using namespace std;

int main()
{
	int a=200;
	int *p =&a;

	cout<<hex<<p<<endl;

	int b = 10;
	//int *p= &b;

	p = &b;

	cout<<hex<<p<<endl;
	cout<<*p<<endl;

	return 0;
}