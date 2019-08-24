#include <iostream>
#include <string>
#include <sstream>
#include <memory>
using namespace std;


class date
{
private:
	int year;
	int month;
	int day;
	string ds;


public:
	const static int test=33 ; // 注意是 const static 
	// int test;
	date (int years, int months, int days): year(years), month(months), day(days){}
// 单目 运算符
	date& operator ++ ()
	{
		++ day;
		return *this;
	}

	date& operator --()
	{
		--day;
		return *this;
	}

	date operator ++ (int)
	{
		date Copy (year, month, day);
		++day;
		return Copy;
	}

// 双目运算符号；
	date  operator + (int dtadd)
	{
		date newdata(year, month, day + dtadd);
		return newdata;
	}

	operator const char* ()
	{
		ostringstream fd;
		fd << year << month << day << "ok" << endl;
		// ds = fd.str();
		// return ds.c_str();
		return fd.str().c_str(); //也是可行的
	}

	int  get_day()
	{
		// cout << "day :" << day << endl;
		return day;
	}

	void get_day_2()
	{
		cout << "day : " << day << endl;
	}


// += -+:
	void operator +=(int adds)
	{
		day += adds;
	}
	void operator -= (int reds)
	{
		day -= reds;
	}
// == ！=：
	bool operator == (const date& compare)
	{
		return ((day == compare.day) && (month == compare.month) && (year == compare.year));
	}

	bool operator !=(const date& compare)
	{
		return !(this->operator==(compare)); // this 是什么意思？
	}


// <
	bool operator <(const date& compare)
	{
		if(year < compare.year)
		{
			return true;
		}
		else if (month < compare.month)
		{
			return true;
		}
		else if (day < compare.day)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	bool operator <= (const date& compare)
	{
		if(this->operator == (compare))
			return true;
		else if (this->operator < (compare)) //注意 this的用法 需要注意的。
			return true;
		else
			return false;
	}

	bool operator >= (const date& compare)
	{
		//if(this->operator == (compare))
		//	return true
		//else 
		return !(this->operator < (compare));
	}



	void display()
	{
		cout << "Y M D :" << year <<" month : " << month << " day : " <<  day << endl;
	}
};

int main()
{
	date mydate(2015 , 11, 4);
	date mydatecomapre(2018, 11, 3);
	if(mydate  >= mydatecomapre)
	{
		cout << "equal" << endl;
	}
	else
	{
		cout << "not equal" << endl;
	}


	mydate.display();

	++ mydate;
	mydate.display();

	//--mydate;
	//--mydate;
	//mydate.display();
	cout << mydate.get_day() << ":day" << mydate.test << endl;
	mydate.get_day_2();


	mydate++;
	mydate.display();
	cout << mydate << endl;

	cout << " ------------" << endl;
	// 双目；

	date newmydates(mydate + 10);
	// cout< newmydates << endl;
	newmydates += 3;
	newmydates -= 3;
	newmydates.display();


	cout << "------------" << endl;

	unique_ptr<date> md( new date(2011, 3, 3));
	// date md (2018,1,33);
	// cout << md->display() << " :: ok" << endl;
	md->display();
	md->get_day_2();
	// cout << md.test << endl; //有问题
	// md->year;

	cout << "-----" << endl;
	cout << endl;

	unique_ptr<int> myint(new int);
	*myint = 43;
	cout << myint << " -- " << endl;


	return 0;
};