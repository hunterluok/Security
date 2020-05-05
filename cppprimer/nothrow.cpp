#include<iostream>
using namespace std;

int main()
{
	int *page = new(nothrow) int[0x1fffffffff];

	if(page)
	{
		delete [] page;
	}

	else
		cout<<"memory allocation failed,ending program"<<endl;

	return 0;

}