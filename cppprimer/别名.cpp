#include<iostream>
using namespace std;

int main()
{
	int a = 10;

	cout<<"a is "<<a<<endl;
	cout<<"address of a is"<<&a<<endl;


	int &p = a;

	cout<<"p is "<<p<<endl;
	cout<<"p may be is"<<&p<<endl;
	return 0;

}