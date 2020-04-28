#include <iostream>
#include <fstream>
#include <vector>
// #include <stdlib.h>
#include <string>
#include <iomanip>
#include <fstream>

using namespace std;

void setcreen();
void setcaption(const char *ptext);

int main()
{
	
	setcreen();
	setcaption("管理系统");


	// cout << "hello world" << endl;
	return 0;
}

void setcreen()
{
	char sysSetBuf[90];
	cout << sysSetBuf << " col 20, line 40 " << endl;
	system(sysSetBuf);
}

void setcaption(const char *ptext)
{
	char syssetbuf[80];
	cout << syssetbuf <<  " title " << ptext;
	system(syssetbuf);
}