#include<iostream>
#include <string>
using namespace std;

class circle
{
private:
	double pi;
	double radius;

public:
	circle( double sradius):radius(sradius),pi(3.14) {}

	double getarea()
	{
		return radius * radius * pi;
	}

};


int main()
{
	cout << "input a diuble :";
	double rad = 0;
	cin >> rad;

	circle yuan(rad);
	cout << yuan.getarea() <<endl;;
	return 0;

}