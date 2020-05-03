#include<iostream>
#include<thread>
#include<chrono>
#include<stdio.h>
#include<fstream>
#include<string>
#include<stdlib.h>
#include<sstream>
#include<deque>
#include<list>
using namespace std;


struct mystructs
{
public:
	mystructs(int data, const char* chars):a(data),b(chars){};
	~mystructs(){};
	int a;
	const char* b;
};

typedef struct
{
	int a;
	const char* b;

}mystruct;

void str2int(const string& a, int& b)
{
	stringstream temp;
	temp << a;
	temp >> b;
}


void int2str(const int&a, string& b)
{
	stringstream temp;
	temp << a;
	temp >> b;
}


void func(const int& data, mystruct d)
{
	mystruct p =  d;
	deque<string>  mydeque;	


	string temp_str;
	int2str(data, temp_str);
	mydeque.push_back(temp_str);
	
	string t_str;
	int2str(d.a, t_str);
	mydeque.push_back(t_str);

	cout << " data is " << temp_str << " struct data "<< t_str << " " << p.b << endl;
	mydeque.push_back(p.b);

	string nd = "";
	for(size_t i = 0; i < mydeque.size(); ++i)
	{
		nd += mydeque[i];
		nd += " ";
	}

	ofstream wri("data.txt", ios::out|ios::app);
	if(wri.is_open())
	{
		wri << nd << endl;
		cout << "write ..." << endl; 
	}
	else
	{
		exit(1);
	}
	wri.close();
	cout << endl;
}
int main()
{
	thread threads[5];
	for(int i = 0; i < 5; ++i)
	{
	//	mystruct*  my = new mystruct(i, "sx");
		mystruct my;
		my.a = i;
		my.b = "sx";
		//cout << " a is " << my->a << " b is " << my->b << endl;
		threads[i] = thread(func, i, my);
	//	delete my;
	}
	for(auto& th: threads)
	{
		th.join();
	}
	return 0;

}
