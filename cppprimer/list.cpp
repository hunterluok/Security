#include<iostream>
#include <deque>
using namespace std;


template<typename T>
void display(const T& inputs)
{
	for(typename T::const_iterator iele = inputs.begin(); iele != inputs.end(); ++iele)
	{
		cout << "ielement is :" << *iele << endl;
	}
}


int main()
{
	deque <int> myde (3); // 默认初始化为0 了；
	myde.push_back (22);
	myde.push_front (2);
	display(myde);
	cout << "------" << endl;
	myde.pop_back();
	myde.pop_front();
	display(myde);
	cout << "------" << endl;

	myde.push_front(222);
	myde.push_back(333);

	for(size_t i=0; i<myde.size(); ++i)  // size_t == int 
	{
		cout << " const + :" << myde[i] << endl;
	}
	return 0;
}