#ifndef READDATA_H
#define READDATA_H

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


vector<vector<string> >
readdata(string path, const int fields = 5, const char delimiter = '\t')
{

    ifstream ifs;
	ifs.open(path);
	if(!ifs.is_open())
	{
	    cout << " file is not opend " << endl;
	    exit(1);
	}

	string ss;
	vector<vector<string> > nd;

	while(getline(ifs, ss))
	{
	    stringstream temp_s(ss);
	    string t_s;

	    vector<string> temp_n;
	    temp_n.reserve(fields);

	    while(getline(temp_s, t_s, delimiter))
	    {
	        temp_n.push_back(t_s);

	    }
	    nd.push_back(temp_n);
	}

	return nd;
}

#endif