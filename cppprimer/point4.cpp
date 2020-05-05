#include <iostream>
using namespace std;

int main()
{
	cout<<"how many integers you wish to enter?";
	int inputnums = 0;
	cin >> inputnums;

	int *pnumber = new int [inputnums];
	int *pcopy =pnumber;

	cout<< "successfully allodcate memory for"<<inputnums<<"integers"<<endl;

	for (int index=0;index<inputnums;++index)
	{
		cout<<"enter  number"<<index<<":"<<endl;
		cin>>*(pnumber+index);
	}

	cout<<"display all numbers input"<<endl;

	for (int index=0;index<inputnums; ++index)
	{
		cout<<*(pcopy++)<<" ";
	}

	cout<< endl;
	delete[] pnumber;
	return 0;

}