#include <iostream>
using namespace std;


int square(int num)
{
	int s= 0;
	s =num*num;
	return s;
}

int main()
{
	int a =0;
	cin>>a;

	square(a);
	cout<<square(a)<<endl;

	return 0;
}


void sqr(int &num)
{
	num *=num
}
int main()
{
	int a=0
	cin>>a;
	sqr(a);
	cout<<a<<endl;
	return 0;
}