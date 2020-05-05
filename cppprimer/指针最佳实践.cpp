#include<iostream>
using namespace std;

int main()
{
	cout << "is it summy(y/n)?";
	char uinput = 'y';

	cin >> uinput;

	if(uinput=='y')
	{
		int *pin = new int;
		*pin =30;

		cout<<"zhi is "<<*pin<<endl;

		delete pin;
	}
	else
	{
		cout<<"hello c++"<<endl;
	}

	return 0;
}