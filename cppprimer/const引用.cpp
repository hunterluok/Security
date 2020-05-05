#include<iostream>
using namespace std;

void cal(const int& num,int& result)
{
	result = num*num;
}

int main()
{
	cout <<"shuru a"<<endl;
	int a = 0;
	cin>>a;

	int re = 0;
	cal(a,re);
	cout<<re<<endl;

	return 0;
}