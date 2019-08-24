#include<iostream>
#include<vector>
using namespace std;

char disoptions()
{
	cout << "enter 'n' to enter a number" << endl;
	cout << "enter 'q' to query a number" << endl;
	cout << "enter 's' to quit current function" << endl;
	cout << "enter 'd to display the vector" << endl;
	char s ='0';
	cin >> s;
	return s; // 这里返回一个 char 值，才有用的
}


template<typename T>
void display(const T& inputs)
{
	for(typename T::const_iterator iele=inputs.begin(); iele!= inputs.end(); ++iele)
	{
		cout << "the ielement is :" << * iele << endl;
	}
}


int main()
{
	std::vector<int> myv;
	char xx = '\0';

	while((xx = disoptions())!='s')
	{
		if (xx=='n')
		{
			cout << " enter a number : " ;
			int number =0;
			cin >> number;
			myv.push_back(number);
		}
		else if (xx=='q')
		{
			cout << "enter a query number between 0~" << myv.size()-1 << " please ";
			int query_number = 0;
			cin >> query_number;
			if(query_number<myv.size())
			{
				cout << "the " << query_number <<"th data is :" << myv[query_number] << endl;
			}
			else
			{
				cout << "Out of the index" << endl;
			}
		}
		else if (xx=='d')
		{
			cout << "display tht function" << endl;
			display(myv);
		}
	}

	return 0;
}