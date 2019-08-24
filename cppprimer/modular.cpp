#include<iostream>
using namespace std;

template<typename T>

class custom
{
public:
	void setage(const T& newvalue)
	{
		age = newvalue;
	}

	const T& getage() const 
	{
		return age;
	}

private:
	T age;
};

int main()
{
	custom<int> normal;
	normal.setage(10);
	cout <<  normal.getage() << endl;

	custom<long long> long_date;
	long_date.setage(1232424);
	cout << long_date.getage() << endl;

	return 0;
}