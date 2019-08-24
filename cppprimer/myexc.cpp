#include<iostream>
#include<string>
#include<exception>
using namespace std;

class customexcep: public exception
{
	string Reason;

public:
	customexcep (const char* why):Reason(why){}

	virtual const char* what() const throw()
	{
		return Reason.c_str();
	}
};


double div(double in1, double in2)
{
	if (in2 ==0 )
		throw customexcep("dib by 0;");
	return (in1 / in2);
};

int main()
{
	cout << "enter div";
	double in1 = 0.0;
	cin >> in1 ;
	cout << "enter in2";
	double in2 = 0.0;
	cin >> in2;

	try
	{
		cout << "result if division us " << div(in1, in2) << endl;
	}
	catch(exception& exp)
	{
		cout << exp.what() << endl;
		cout << "sorry can't continue" << endl;
	}
	return 0;
}
