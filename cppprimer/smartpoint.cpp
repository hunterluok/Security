#include<iostream>
using namespace std;

template<typename T>
class smart_point
{
private:
	T* m_pointer;
public:
	smart_point(T* pdata):m_pointer(pdata){}
	~smart_point() { delete m_pointer;}

	T& operator * () const
	{
		return *(m_pointer);
	}
	T* operator -> () const
	{
		return m_pointer;
	}
};

class date
{
private:
	int year;
	int month;

public:
	date(int years, int months): year(years), month(months){}

	void display()
	{
		cout << "date :" << year << " : " << month << " end" << endl;
	}
};


int main()
{
	// date md(2018, 11);
	smart_point<int> mdata(new int(33));
	cout << "data is : " <<  "mdata" << " test : " << *mdata << endl;

	smart_point<date> mdate(new date(2012, 33));
	mdate->display();

	return 0;

}
