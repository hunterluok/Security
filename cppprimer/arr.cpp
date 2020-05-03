#include <iostream>
#include <vector>
using namespace std;

template<typename T> void show(T& data)
{
	typename T::const_iterator ele = data.begin();
	while(ele != data.end())
	{
		cout << "ele is " << *ele << endl;
		ele++;
	} 

}


int main()
{
	int  my[3] = {1, 2, 3};
	//	vector<int> my={2, 2, 3, 4};
	//my.push_back(2);
	//my.push_back(22);
	//show(my);
	for(size_t i = 0; i < 3; ++i)
	{

		cout << "ele is "<< my[i] << endl;
	}
	
	return 0;

}
