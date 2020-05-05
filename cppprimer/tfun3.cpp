
# include <iostream>

using namespace std;

double area(double r,double pi=3.2);

int main()
{
cout << "输入r"<<endl;
double r=0;
cin >> r ;

cout << "输入 控制 字符" <<endl;
char us = 'y';
cin >> us;

if(us=='y'){
cout << area(r)<<endl;

}
else
{
double npi=0;
cout << "shu ru new pi" << endl;
cin >> npi;
cout << area(r,npi) <<endl;
}
return 0;
}


double area(double r, double pi)
{
 return r*pi*2;
}
