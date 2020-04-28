#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	const char * state = "mynameislk";
	const char * state1 = "foreverlove";
	int len = strlen(state);
	cout<<"increasing loop index:\n";

	//int i;
	for(int i = 1;i <= len; i++)
	{
		cout.write(state,i);
		cout << endl;
	}

	cout <<"decreasing loop index:\n";
	for (int i=len;i>0;i--)
	{
		cout.write(state,i)<<endl;
	}

	//return 0;
	cout<<"exceding string len:\n"<<endl;
	cout.write(state,len+5)<<endl;

	long val = 1231323;
	cout<<sizeof(val)<<endl;
	cout.write((char *) & val,sizeof(long));

	return 0;

}