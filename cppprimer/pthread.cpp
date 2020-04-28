#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

volatile int counter(0);
mutex mtx;

void func()
{
	for(int i=0; i < 100000; ++i)
	{
		mtx.lock();
		++counter;
		mtx.unlock();
	}
}

int main()
{
	thread  mythreads[10];
	for(int i = 0; i < 10; ++i)
	{
		mythreads[i] = thread(func);
	}

	for(auto& th: mythreads)
	{
		th.join();
	}

	cout << " count : " << counter << endl;
	return 0;
}
