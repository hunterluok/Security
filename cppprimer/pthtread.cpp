#include <iostream>
#include <thread>
#include <mutex>

using namespace std;


volatile int counter(0);
mutex mtx;

void fun()
{
	for(int i = 0; i < 1000; ++i)
	{
		mtx.lock();
		++counter;
		mtx.unlock();
	}
}



int mian()
{
	thread mythred[10];
	for(int i = 0; i < 10; ++i)
	{
		mythred[i] = thread(fun);
	}

	for(int i = 0; i < 10; ++i)
	{
		mythred[i].join();
	}

	cout << "result is " << counter << endl;
	return 0;
}