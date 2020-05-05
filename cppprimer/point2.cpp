# include<iostream>
using namespace std;

int main()
{

	int *pint = new int;

	cout<<"shuru :";
	cin>> *pint;

	cout<<pint<<endl;
	cout<< *pint<<endl;

	delete pint;

	return 0;
}