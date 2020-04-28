//
//  util.cpp
//  learncpp
//
//  Created by 罗奎 on 2020/4/26.
//  Copyright © 2020 罗奎. All rights reserved.
//

#ifndef UTIL_H
#define UTIL_H

#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;



vector<vector<int> > readtarget(string path="t.txt")
{
    // string path = argv[1];
    // cout << " " << argv[0]  << " " << argc << endl;
    ifstream myfile(path, ios::in);

    if (!myfile)
    {
        cout << "file is bad" << endl;
        throw "file is wrong";
    }

    vector<vector<int> > newdata;
    string line;
    while(getline(myfile, line))
    {
        istringstream nline(line);
        vector<int> temp_line;
        string s;
        while(nline >> s)
        {
            int temp = 0;
            stringstream ano;
            ano << s;
            ano >> temp;
            temp_line.push_back(temp);
        }
        newdata.push_back(temp_line);
    }
    return newdata;
}



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
    myfile.close();
    return true;
}



bool myreaddata(string path,  vector<vector<int> >& data)
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
        vector<int> temp_vector;
        istringstream line(myn);

        string temp_index;
        line >> temp_index;

        string temp;
        while(line >> temp)
        {
            int temp_float=0;
            // 注意这里 是如何将 string 转化为 float的，很有用处/。
            stringstream another;
            another << temp;
            another >> temp_float;

            temp_vector.push_back(temp_float);
        }
        data.push_back(temp_vector);

    }
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


bool read_label(string path, vector<int>& data)
{
    ifstream myfile(path, ios::in);
    if(!myfile)
    {
        cout << "打开文件出错" << endl;
        return false;
    }

    int myn;
    while(myfile >> myn)
    {
        data.push_back(myn);
    }
    myfile.close();
    return true;
}


template<typename T>
void showdata(const T& data)
{
    // 这里的 const_iterator 不能换成 iterator；
   typename T::const_iterator iter = data.begin();
   while(iter != data.end())
   {
        cout << *iter << ' ';
        iter ++;
   }
   cout << endl;
}

template<typename T>
float sumdata(const T& data)
{
    float sums = 0.0;
    for(int i=0; i < data.size(); ++i)
    {
        sums += data[i];
    }
    return sums;
}

template<typename T>
void showmap(const T& data)
{
    typename T::const_iterator iter = data.begin();
    while(iter != data.end())
    {
        cout << "key is " << iter -> first << " value is " << iter -> second;
        iter ++;
    }
}

template <typename T>
void showvector(const T& data)
{
    long int m = data.size();
    long int n = data[0].size();
    for(long int i = 0; i < m; ++i)
    {
        for(long int j = 0; j < n; ++j)
        {
            cout << data[i][j] << " ";
        }
        cout << endl;
    }
    cout << " " << endl;
}


#endif
