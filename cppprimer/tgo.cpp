
#include<iostream>
using namespace std;

int main(){
JumpToPoint:
	int a=0;
	int b=0;
	cin>>a;
	cin>>b;
	
	int c = a+b;
	int d = a*b;

	cout<<"jia: "<<c<<"cheng:"<<d<<"\n"<<endl;
	cout<<"suru y or n"<<endl;
	char repeat='y';
	cin>>repeat;
	if(repeat=='y')
		goto JumpToPoint;

	cout<<"good bye"<<endl;
	
	return 0;
}
