#ifndef UTIL_H
#define UTIL_H

#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

bool readdata(string path,  vector<vector<float> >& data)
{
	ifstream myfile(path, ios::in);
	if(!myfile)
    {
        cout << "打开文件出错" << endl;
        return false;
    }

    string myn;
    while(getline(myfile, myn))
    {
        vector<float> temp_vector;
        istringstream line(myn);

        string temp_index;
        line >> temp_index;

        string temp;
        while(line >> temp)
        {
            float temp_float=0.0;
            // 注意这里 是如何将 string 转化为 float的，很有用处/。
            stringstream another;
            another << temp;
            another >> temp_float;

            temp_vector.push_back(temp_float);
        }
        data.push_back(temp_vector);

    }

    // 如何 一行行的 读入 vector 方便进行计算。
//	float index, a , b ,c, d;
//	while(myfile >> index >> a >> b >> c >> d)
//	{
//		vector<float> temp_vec;
//		temp_vec.push_back(a);
//		temp_vec.push_back(b);
//		temp_vec.push_back(c);
//		temp_vec.push_back(d);
//		data.push_back(temp_vec);
//	}
	myfile.close();
	return true;
}

bool writedata(string path,  vector<vector<float> > data)
{
	ofstream myfile(path, ios::out);
	if(!myfile)
    {
        cout << "打开文件出错" << endl;
        return false;
    }

	for(int i=0; i<data.size(); ++i)
	{
		// 如何一行行的写入数据，
		myfile << data[i][0] << " " << data[i][1] << endl;
	}
	myfile.close();
	return true;
}


void showvector(vector<vector<float> > data)
{
	for(int i=0; i<data.size(); ++i)
	{
		for(int j=0; j<data[i].size(); ++j)
			cout << data[i][j] << " ";
		cout << endl;
	}
}

#endif