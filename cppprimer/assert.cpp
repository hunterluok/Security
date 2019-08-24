#include<iostream>
#include<assert.h>
using namespace std;


template<typename T1=int, typename T2=double>
class holdpair
{
private:
	T1 value11;
	T2 value22;
public:
	holdpair (const T1& value1, const T2& value2)
	{
		value11 = value1;
		value22 = value2;
	};

	const T1& getfirstvalue() const
	{
		return value11;
	};

	const T2& getsecondvalue() const
	{
		return value22;
	};

	void pair()
	{
		if(value22 > value11)
			cout << "max :" << value22 << endl;
		else
			cout << "max :" << value11 << endl;
	};
};

int main()
{
	// char * sayhello = new char[25];
	// assert(sayhello!=NULL);
	// cout << "he he " << endl;
	// delete [] sayhello;
	//return 0;
	holdpair  <> first(2,3.4);
	// holdpair <short,char*> mshortstringpair(25,"learn template ,love c++");

	cout<< "the first objection contains" << endl;
	cout<< "value1 : " << first.getsecondvalue() << endl;
	cout<< "value2 : " << first.getfirstvalue() << endl;

	holdpair <double,double> second(3.111,2.2);
	cout << second.getfirstvalue() << "xxxx" << endl;
	second.pair(); 


	first.pair();
	return 0;
}