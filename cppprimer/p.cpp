#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int a[10] = {1, 2, 3};
	for(int i = 0; i < a.size(); ++i) 
		cout << a[i] << " : ok" << endl;
	return 0;
}
