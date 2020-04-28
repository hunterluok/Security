#include <iostream>
#include <pthread.h>
#include <string>
#include <fstream>
#include <vector>



using namespace std;


volatile int counter(0);


void *func(void *arg)
{
	cout << " int func "  << endl;
	++counter;
	return (void *) 0;
}



int main(int argc, char *argv [])
{
	pthread_t tdip[10];

	for(int i = 0; i < 10; ++i)
	{
		int ret = pthread_create(&tdip[i], NULL, func, NULL);
		if(ret)
		{
			cout << "pthread failed " << endl;
			return -1;
		}
	}
	//pthread_join(tdip, NULL);
	pthread_exit(NULL);
	cout << "main thread is created " << counter << endl;

	return 0;
}



