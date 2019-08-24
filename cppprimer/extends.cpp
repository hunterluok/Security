#include<iostream>
using namespace std;

class fish
{
protected:
	bool inwater;

public:
	void swin()
	{
		if(inwater)
		{
			// return "ok";
			cout << "ok" << endl;
		}
		else
		{
			// return "on!.no";
			cout << "on.no!" << endl;
		}
	}
};

class liyu : public fish
{
public:
	liyu()
	{
		inwater =  true;
	}
};

class heyu : public fish
{
public:
	heyu()
	{
		inwater = false;
	}
};

int main()
{
	liyu x_liyu;
	heyu x_heyu;
	cout << "z_liyu : ";
	x_liyu.swin();

	cout << "x_heyu : ";
	 x_heyu.swin();
	return 0;
}