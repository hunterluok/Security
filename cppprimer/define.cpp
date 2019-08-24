#include<iostream>
#include<string>
using namespace std;

#define pi 3.14
#define array_length 5
#define my_raduye double
#define funt(x) ((x) * (x))
#define fav_with "jack_daniel"  // 定义了一个 字符串。


int main()
{
	int myarray[array_length] = {20};

	cout << "array length " << sizeof(myarray) << "xxx" << sizeof(int) << endl;

	cout << "raidu ";
	my_raduye radious = 0;
	// cin >> radious;

	cout << funt(array_length) << endl;
	cout << "double :" << radious << endl ;

	// string FavoriteWhisky(FavoriteWhisky);
	cout << "my FavoriteWhisky is :" << fav_with << endl << myarray << endl;

	for(int i=0; i<array_length; ++i)
		cout << "ok :" << myarray[i] << endl;

	return 0;
}
