#include<iostream>
using namespace std;

const double  pi=3.13;

double area(double radius);
double area(double radius,double height);

int main(){
cout<<"enter z for cylinder, c for cicle:";
char choice ='z';
cin>>choice;

cout<<"enter radius:";
double radius=0;
cin >>radius;

if (choice=='z')
{
cout <<"enter height:";
double  height =0;
cin>>height;
cout<<"area of cylinder is:"<<area(radius,height)<<endl;
}
else
{
cout<<"area of cylinder is:"<<area(radius)<<endl;
}
return 0;
};


double area(double radius){
return pi*radius*radius;
};

double area(double radius,double height)
{
return pi*area(radius)*2 + 2*pi*radius*height; 
};


