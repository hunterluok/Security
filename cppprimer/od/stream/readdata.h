#ifndef READDATA_H
#define READDATA_H

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <chrono>
#include <thread>
#include <sstream>

using namespace std;


vector<vector<string> >
readdata(string path, const int fields = 5, const char delimiter = '\t')
{

    ifstream ifs;
	ifs.open(path);
	if(!ifs.is_open())
	{
	    cout << " file is not opend " << endl;
	    exit(EXIT_FAILURE);
	}
//  不太好用，最好是多线程读取不同的文件夹、
//	if(positon != 0)
//	{
//	    ifs.seekg(positon, ios::beg);
//	}

    int count = 0;

	string ss;
	vector<vector<string> > nd;

	while(getline(ifs, ss))
	{
	    stringstream temp_s(ss);
	    string t_s;

	    vector<string> temp_n;
	    //这里注意数据的 维度为5；
	    temp_n.reserve(fields);

        // 切分数据的方法。
	    while(getline(temp_s, t_s, delimiter))
	    {
	        temp_n.push_back(t_s);

	    }
	    nd.push_back(temp_n);

	    count++;
	    if(count > 2)
	        break;
	}
	ifs.close();

	return nd;
}

#endif