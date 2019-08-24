#include <iostream>
using namespace std;


double dips(double d1, double d2)
{
	if (d2==0)
		throw "dividinf by 0 is a divisor";
	return (d1 / d2);
}



int main()
{
	cout << "enter a number :" << endl;

	try
	{
		double inputs = 0, inputs1 = 0;
		cin >> inputs;
		cin >> inputs1;
		cout << "result :" << dips(inputs, inputs1);
		// int *pr = new int [inputs];
		// delete [] pr;
	}
	catch(std::bad_alloc & exp)
	{
		cout << "exception ,go to end," << exp.what() << endl;
	}
	catch(char* exp)
	{
		cout << " result is " << exp << endl;
	}
	catch(...)
	{
		cout << " exception is ,go to end !" << endl;
	}

	return 0;
}
