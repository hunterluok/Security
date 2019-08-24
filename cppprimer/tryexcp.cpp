#include <iostream>
using namespace std;


struct StructA
{
	StructA()
	{
		cout << "Constructed a struct  A" <<endl;
	}
	~StructA()
	{
		cout << "destoryed a struct  A" << endl;
	}
};

struct StructB
{
	StructB()
	{
		cout << " Constructed a struct  B" << endl;
	}
	~StructB()
	{
		cout << "destoryed a struct B" << endl;
	}
};

void fb()
{
	cout << "in funce b" << endl;
	StructA sa;
	StructB sb;
	cout << "about to throw up!" << endl;
	throw "thorwing for heck of it";
};


void fa()
{
	try
	{	
		cout << " in func a " << endl;
		StructA sa;
		StructB sb;
		fb();
		cout << "funca : returning ti caller" << endl;
	}
	catch(const char* exp)
	{
		cout << "funcA: caught exception ,it says " << exp << endl;
		cout << "funcA: handled it here, will not throw ti caller" << endl;
		throw ;
	}
};


int main()
{
	cout << "main() : started exception ::";
	try
	{
		fa();
	}
	catch(const char* exp)
	{
		cout << "exception :" << exp << endl;
	}
	cout << "main(): exiting gracefully " << endl;
	return 0;
}