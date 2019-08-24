#include<iostream>
#include<string>
using namespace std;


class human
{
private:
	int age;
	string name;

	friend class use;

public:
	human(int sage, string sname):age(sage),name(sname){};
};


class use
{
public:
	static void  disage(human& input)
	{
		cout << input.age << endl;
		cout <<  "eee " << endl;;
	}
};

int main()
{
	human first(3232,"xxxss");
	use::disage(first); //注意这里的用法。
	// use test;
	// cout << test.disage(first) << endl;
	return 0;


}