#include<iostream>
using namespace std;

template<typename Type>
const Type& getmax(const Type& value1 ,const Type& value2)
{
	if(value1 > value2)
		return value1;
	else
		return value2;
}

template<typename Type>
void display(const Type& value1, const Type& value2)
{
	cout << "getmax (" << value1  << "," << value2 << ")=";
	cout << getmax(value1, value2);
}

int main()
{
	int int1 = -100, int2 = 200;
	display(int1, int2);

	double b1 = 0.3 , b2 =0.9;
	display(b1, b2);
	return 0;
}