#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{
	string key;
	string value = "1";

	while(cin >> key)
	{
		cout << key << "\t" << value << endl;
		cerr << "reporter:status:processing......\n";
	}
	return 0;
}

