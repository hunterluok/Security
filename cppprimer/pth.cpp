#include <iostream> 
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <string>


using namespace std;

typedef struct 
{
	int a;
	string s;
}mystruct;


void *func(void *arg)
{
	// int *pn = (int *) (arg);
	// int n = *pn;
	// const char *my = (char *)(arg);
	mystruct* old = (mystruct *) (arg);
	cout << "hello pthread " << old->s <<  endl;
	return (void*) 0;
}

int main()
{
	pthread_t tidp;
	int ret;
	const char* n = "hello pthread_create";

	mystruct ms;
	ms.a = 10;
	ms.s = "hehe";

	ret = pthread_create(&tidp, NULL, func, (void *) &ms);
	if(ret)
	{
		cout << "pthread_create failed " << endl;
		return -1;
	}

	pthread_join(tidp, NULL);
	cout << "in main thread is created" << endl;
	return 1;
}