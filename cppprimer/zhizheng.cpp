# include <iostream>

using namespace std;

int main()
{
	int age=20;
	int *p = &age;

	cout<<hex<<p<<endl;
	cout<<hex<<&age<<endl;
	return 0;
}