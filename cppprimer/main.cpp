#include<iostream>
#include <unistd.h>

using namespace std;

int main()
{
	execl("/Users/luokui/Desktop/Security/cppprimer/pid",NULL);
	cout << "-----" <<endl;
	return 0;

}
