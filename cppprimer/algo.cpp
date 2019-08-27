#include<iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
	std::vector<int> myarray;

	myarray.push_back (50);
	myarray.push_back (100);
	myarray.push_back (33);
	myarray.push_back (44);

	cout << " find the element :" << endl;
	std::vector<int> :: iterator ielement = find(myarray.begin(), myarray.end(), 44);
	while(ielement != myarray.end())
	{
		int position = distance(myarray.begin(), ielement);
		cout << "value " << *ielement ;
		cout << "found in the vector at position:" << position << endl;
	}

	return 0;
} 