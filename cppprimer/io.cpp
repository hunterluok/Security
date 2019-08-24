#include<iostream>
#include<iomanip>
using namespace std;


int main()
{
	cout << " pi :" ;
	// int a = 0;
	// cin >> a;

	double pi = double(22.0) / 7 ;
	double a = pi;
	cout << setprecision(3) << endl;  // 4位有效数字 不包含 小数点
	// cout << scientific << endl;   // 科学计数法的 有效数字 与 上面的 不同 增加了一位。

    cout << setw(10);
    // cout << setfill("*") ;

	cout << "aaa :" << oct << a << endl;
	cout << "bbb :" << hex << a << endl;

	cout << setw(20) << setfill('*') << endl;   // setfill 只适合于 字符串，不适合其他的东西。
	cout << "Integers " << endl;

	// cout << setiosflags(ios_base::hex | ios_base::showbase | ios_base::uppercase) << endl;
	// cout << a << endl;

	string myn;
	// cin >> myn;
	getline(cin, myn); //这里的区别
	cout << "myn :  --" << myn << endl;

	return 0;
}