
#include <iostream>
using namespace std;

int main()
{
enum dayofweek{
sunday=0,
zhou2,
zhou3
};
cout<<"shuru zhi "<<endl;
int day = sunday;
cin >> day;

switch(day)
{
case sunday:
	cout<<"over"<<endl;
	break;
case zhou2:
	cout<<"2b"<<endl;
	break;
default:
	cout<<"hehe"<<endl;
	break;
}
return 0;


}
