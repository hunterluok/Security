# include <iostream>
using namespace std;

inline long DoubleNum(int inputnum)
{
	return inputnum*2;
}

int main()
{
	cout<<"enter an integer"<<endl;
	int inputnum=0;
	cin>> inputnum;
	cout<<"double is:"<<DoubleNum(inputnum)<<endl;
	return 0;

}