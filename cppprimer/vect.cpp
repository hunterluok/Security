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

	// for(size_t i=0; i < v.size(); ++i)
	// {
	//	cout << v.at(i) << " ::" << endl;  // at 的用法需要注意的。
 	// }

 	v.insert(v.begin(),22222);
 	v.insert(v.end(),33333);
 	std::vector<int> vs (2);  
 	v.insert(v.begin() + 1, vs.begin(), vs.end()-1); // 注意这里的变化。

 	// isplay(v);

 	// v.reverse();
 	display(v);

 	return 0;
}