extern void printage(int age);

#include<iostream>
#include <vector>
using namespace std;


template<typename T>
void display(const T& inputs)
{
	// const_iterator 不能为 iterator;
	typename T::const_iterator iele = inputs.begin();
	while(iele != inputs.end())
	{
		cout << " --- :" << *iele << endl;
		++ iele;
	}
}



int main()
{
	std::vector<int> v;

	v.push_back(11);
	v.push_back(22);
	v.push_back(33);


 	v.insert(v.begin(),22222);
 	v.insert(v.end(),33333);
 	std::vector<int> vs (2);  
 	v.insert(v.begin() + 1, vs.begin(), vs.end()-1); // 注意这里的变化。


 	display(v);
	cout << " test age " << endl;
	printage(22);
 	return 0;
}
