#include <iostream>
#include <string>
#include <stdio.h>
#include <map>

#include <sstream>

using namespace std;

//int main()
//{
//	string key;
//	string value = "1";
//
//	while(cin >> key)
//	{
//		cout << key << "\t" << value << endl;
//		cerr << "reporter:status:processing......\n";
//	}
//	return 0;
//}


void showmap(map<string, int> data)
{
    map<string, int>::const_iterator ele = data.begin();
    while(ele != data.end())
    {
        cout << "key is " << ele->first << " value " << ele->second << endl;
        ele++;
    }

}


int main()
{
	string key;
	int value = 1;

	map<string, int> mymap;

	while(cin >> key)
	{
	    //mymap[key]++;
	    //cout << " origin ket is " << key << endl;
	    //istringstream line(key);
//	    string temp_str;
//	    while(line >> temp_str)
//	    {
//
		cout << key << "\t" << value << endl;
//		    mymap[temp_str]++;
//		}
		//cerr << "reporter:status:processing......\n";
	}
	//showmap(mymap);
	return 0;
}
