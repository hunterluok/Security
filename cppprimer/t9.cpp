
#include<iostream>

using namespace std;

int main(){

cout<<"enter two integers"<<endl;
int num1=0;
int num2=0;
cin>>num1;
cin>>num2;

cout<<"enter \'m\' to multiy,anything else ti add:";
char useselect = '\0';
cin >> useselect;

int result = 0 ;
if(useselect=='m')
	result = num1 * num2;
else
	result = num1 + num2;
cout<<"result = "<<result<<endl;
return 0;


}
