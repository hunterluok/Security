#include <iostream>
#include <exception>

using namespace std;

float sub(float a, float b)
{

	if(b==0.0)
	{
		throw "division 0";
		exit(1);

	}
	return a / b;
}


int main()
{

	float a = 10.0;
	int  b = 0;
	float c = 0.0;
	try
	{
		c = a / b;
		cout << "c is " << c << endl;
	}
	catch(exception& exep)
	{
		cout << "wrong is " << exep.what() << endl;
	}
	//cout << "c is " << c << endl;
	return 0;
}
