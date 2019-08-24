#include<iostream>
using namespace std;

class fish
{
protected:
	bool inwater;

public:

	fish(bool isinwater):inwater(isinwater) {}  // 不是默认的 构造函数而已
	void get_res()
	{
		if(inwater)
			cout << "ok" << endl;
		else
			cout << "oh ,no" << endl;
	}

};

class first_fish : public fish
{
public:
	first_fish(): fish(false) {}
	void get_res()
	{
		cout << "first_fish " << endl;
	}
};

class second_fish : public fish
{
public:
	second_fish():fish(false) {}
	void get_res()
	{
		cout << " second_fish" << endl;
 	}
};

int main()
{
	first_fish ff;
	second_fish sf;
	cout << " xx: ";
	sf.get_res();
	cout << "base function :" << endl;
	ff.fish::get_res();
	return 0;
}



