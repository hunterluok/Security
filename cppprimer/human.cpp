#include<iostream>
#include<string>
using namespace std;

class human
{
private:
	int age;
	string name;

public:
	human()
	{
		age = 0;
	}

	human(string init_name)
	{
		name =  init_name;
	}

	human(int sage, string xxname)
	{
		age = sage;
		name = xxname;
	}

	void setage(int sage)
	{
		age = sage;
	}

	void setname(string sname)
	{
		name = sname;
	}
	
	int get()
	{
		if(age>30)
			return (age-2);
		else
			return age;
	}

	string getname()
	{
		return name;
	}

};


int main()
{
	human firman;
	// firman.setage(22);
	firman.setname("lk_test");

	human secondman("xxxx");
	secondman.setage(44);
	// secondman.setname("heheda");
	
	cout<< "Age of firman" << firman.get()<< endl;
	cout << "Name of first " << firman.getname() << endl;

	cout<< "age of second" << secondman.get() << endl;
	cout << "name of seocnd" << secondman.getname() << endl;

	human third(22,"haha");
	third.setage(444);  //在初始化之后 依然可以利用 set 进行赋新值。
	cout<< "third" << third.get() << endl;
	cout << " third anme "  << third.getname() << endl;

	return 0;
}
