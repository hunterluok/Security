#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
	std::vector<int> myarray;

	myarray.push_back (50);
	myarray.push_back (100);
	myarray.push_back(44);
	myarray.push_back (33);
	myarray.push_back (44);

	cout << " find the element :" << endl;
	std::vector<int> :: iterator ielement = find(myarray.begin(), myarray.end(), 44);
	while(ielement != myarray.end())
	{
		int position = distance(myarray.begin(), ielement);
		cout << "value " << *ielement ;
		cout << "found in the vector at position:" << position << endl;
		// 循环终止的条件
		//ielement++ ;
		// 这里注意利用循环 去寻找下一个迭代器。
		ielement = find(++ielement, myarray.end(), 44);
	}

	return 0;
} 