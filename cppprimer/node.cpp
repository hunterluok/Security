#include <iostream>

using namespace std;


struct single
{
	int data;
	single* nexts;
};


int main()
{
	single a(int data=1);

	cout << a.data << " data " << endl;
	return 0;
}