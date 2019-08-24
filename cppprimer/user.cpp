#include <iostream>
#include <vector>
using namespace std;


template <typename T>
void display(const T& inputs)
{
	for(typename T::const_iterator iele=inputs.begin();iele != inputs.end(); ++ iele)
	{
		cout << "the element is :" << *iele << endl;
	}
}

int main()
{
	std::vector<int> myve;

	int a =0 ;
	char stop ='a';
	cout << "please enter a char :";
	cin >> stop;
	while (stop !='s')
	{
	cout << " char is not 's' ,enter a number :";
	cin >> a;
	myve.push_back(a);
	cout << "enter a char :";
	cin >> stop;
	}

	cout << "display the values of my vector :";
	display(myve);

	return 0;
}