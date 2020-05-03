#include<iostream>

#include<stdio.h>
#include<sys/sem.h>
#include<string>
#include<sstream>

using namespace std;


int main()
{	
	string a("hehe");
	string b("sss");
	a += b;
	cout << "a append b is " << a << endl;
	key_t semkey;
	if((semkey = ftok("./read", 123)) < 0)
	{
		printf("ftok failed \n");
		exit(EXIT_FAILURE);
	}
	printf("ftok ok, semey = %d\n", semkey);
	return 0;
}
