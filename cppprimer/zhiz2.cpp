#include<iostream>

using namespace std;

int main(){
	int age=30;
	int dog = 10;

	cout<<"interge age ="<<age<<endl;
	cout<<"integer dog ="<<dog<<endl;

	int *p=&age;
	cout<<"point to age=0x"<<hex<<p<<endl;

	cout<<"zhi zhen:"<<*p<<endl;

	p =&dog;
	cout<<p<<endl;
	cout<<*p<<endl;

	return 0;


}