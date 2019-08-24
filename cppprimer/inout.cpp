#include<iostream>
#include<fstream>
#include<string>
// #include "std_lib_facilities.h"
#include <vector>
using namespace std;

#include "tt.h"

void show(vector< vector<int> > x);

struct  reading
{
	reading(int ahour, float atemp, float aage):hour(ahour), temp(atemp), age(aage) {}

//private:
	int hour;
	float temp;
	float age;
};

int main()
{
	ofstream myf;
	// myf.open("test.txt",ios_base::out|ios_base::app|ios_base::in);
	myf.open("test.txt", ios_base::out);

	if(myf.is_open())
	{
		cout << "open succeed :" << endl;
		myf << "hello wordl" << endl;
		myf << "hello future" << endl;

		cout << "ok " << endl;
		myf.close(); // 读取完数据 就关闭。

	}


	ifstream myfs;
	myfs.open("test.txt", ios_base::in);
	if (myfs.is_open())
	{
		cout << " 读取数据 :" << endl;
		string filecontent;

		while(myfs.good())
		{
			getline(myfs, filecontent);
			cout << "line :" << filecontent << endl;
		}
		myfs.close();

	}


	// vector<reading> v;
	vector<vector <int> > v;
	int hour;
	float temp;
	float age;

	ifstream myread;
	myread.open("t.txt", ios_base::in);
	if (myread)
		cout << " ok open it" << endl;

	// 相当于可以 按照字段的顺序读取数据的。
	while(myread >> hour >> temp >> age)
	{
		//v.push_back(reading(hour, temp, age));
		vector<int> tsp;
		tsp.push_back(hour);
		tsp.push_back(temp);
		tsp.push_back(age);
		v.push_back(tsp);
	}

	myread.close();

	for(int i=0; i < v.size(); ++i)
	{
		//cout << "(" << v[i].hour << "," << v[i].temp  << "," << v[i].age<< ")\n";
		// cout << "ok" << endl;;
		for (int j=0; j<v[i].size(); j++)
			cout << v[i][j] * 2 << " ";
		cout << endl;
	}

	ofstream mywrite;
	mywrite.open("w.txt", ios_base::out);
	if (mywrite)
		cout << "ok , write" << endl;

	for(int i=0; i<v.size(); i++)
	{
		for(int j=0; j!=v[i].size(); j++)
		{
			mywrite<< v[i][j]<< " ";
		}
		mywrite << endl;
	}
	cout << "show function : " << endl;
	// showdata(v);
	show(v);

	cout << endl;
	cout << rand() % 10 << "  a test" << endl;

	return 0;
}


void show(vector<vector<int> > x)
{
	for(int i=0; i<x.size(); i++)
	{
		//for(int j=0; j<x[i].size(); j++)
		//{
		//	cout<< x[i][j]<< " ";
		//}
		vector<int>::iterator it = x[i].begin();
		for(; it!= x[i].end(); it++)
		{
			cout << *it << " ";
		}


	cout << endl;
	}
}