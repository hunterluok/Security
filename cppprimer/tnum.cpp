
# include<iostream>

using namespace std;

int main()
{
enum dayofweek{
sunday=0,
monday,
wenthday
};

int day=sunday;
cin >> day;

if(day==sunday)
	cout<<"a"<<day<<endl;
else
	cout<<day<<"xx"<<endl;

return 0;
}
