#include <iostream>
#include <cstdlib>

using namespace std;

void printmax(char* number, int length, int indexs);
void printnumber(char* number);

void printdigit(int n)
{
	if(n <= 0)
	{
		return;
	}
	char* number = new char[n+1];
	number[n] = '\0';

	for(int i=0; i<10; ++i)
	{
		number[0] = i+'0';
		printmax(number, n, 0);
	}
	delete[] number;
}

void printmax(char* number, int length, int indexs)
{
	if(indexs == length - 1)
	{
		printnumber(number);
		return;
	}
	for(int i=0; i<10; ++i)
	{
		number[indexs + 1] = i + '0';
		printmax(number, length, indexs+1);
	}
}


void printnumber(char* number)
{
	int lens = strlen(number);
	int flag = 0;
	// 注意 这里的 
	for(int i=0; i< lens; ++i)
	{
		if(number[i] != '0' && flag==0)
			flag = 1;

		if(flag == 1)
		{
			cout << number[i];
		}
	}
	cout << endl;
}


int main()
{	
	char* nm = new char[3];
    cout << "result is :" << endl;
	// printdigit(2);
	nm[0] = 0 + '0';
	nm[1] = 9 + '0';
	cout << nm[0] << endl;
	cout << "count 2 is " << nm[1] << endl;

	return -1;
}