# include<iostream>
using namespace std;
const double pi=3.1415;

void queryandcalculate()
{
cout<<"enter radius";
double radius =0;
cin>> radius;

cout<<"area:"<<pi*radius*radius<<endl;

cout<<"do you wish to calculate (y/n)";
char cal='n';
cin>>cal;

if(cal=='n')
	return;

cout<<"cir"<<2*pi*radius<<endl;
return;

}

int main(){
queryandcalculate();
return 0;
}
