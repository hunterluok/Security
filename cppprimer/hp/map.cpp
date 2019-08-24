#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{
	string key;
	string value = "1";
	std::vector<int> v;
	v.push_back(2);
	while(cin >> key)
	{
		cout << key << "\t" << value << endl;
		cerr << "reporter:status:processing......\n";
	}
	return 0;
}

