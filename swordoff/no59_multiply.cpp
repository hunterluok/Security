#include <iostream>
#include <vector> 

using namespace std;

bool multi(const std::vector<int>& v1, vector<int>& v2)
{
	int lens1 = v1.size();
	int lens2 = v2.capacity();

	if(lens1 != lens2 || lens1 < 1)
	{
		cout << "wrong" << endl;
		return false;
	}

	v2[0] = 1;
	for(int i = 1; i < lens1; ++i)
	{
		v2[i] = v2[i-1] * v1[i-1];
	}

	int temp=1;
	for(int i = lens1 - 2; i >= 0; --i)
	{
		temp *= v1[i + 1];
		v2[i] *= temp;
	}
	return true;
}


int main()
{	
	int lens= 4;
	std::vector<int> v1;
	for(int i = 1; i < lens+1; ++i)
	{
		v1.push_back(i);
	}
	std::vector<int> v2;
	v2.reserve(lens);

	multi(v1, v2);

	for(int i = 0; i < lens; ++i)
	{
		cout << "v2 is " << v2[i] << endl;
	}
	return 0;
}