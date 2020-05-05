#include <iostream>
using namespace std;

int main()
{
	int a = 11;
	int *p = &a;

	double b=12.0;
	double *bb =&b;

	

	cout<< a<<endl;
	cout<< p<<endl;
	cout<<*p<<endl;

	cout<< sizeof(a)<<endl;
	cout<<sizeof(p) <<endl;
	cout<<sizeof(b)<<endl;
	cout<< sizeof(bb)<<endl;
	return 0;
}