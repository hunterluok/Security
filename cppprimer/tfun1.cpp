# include <iostream>
using namespace std;

const double pi=3.14;

double zc(double r);
double mj(double r);

int main()
{
double r = 0;
cout << "shu ru shu zi " << endl;
cin >> r;

cout << "zhou chang : "<< zc(r) <<endl;
cout<< "mian ji : "  << mj(r) <<endl;
return 0;

}

double zc(double r){
return pi*r*r;

}

double mj(double r){
return 2*pi*r;
}

