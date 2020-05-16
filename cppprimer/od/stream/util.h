#ifndef UTIL_H
#define UTIL_H

#include <string>
#include <vector>
#include <set>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <iostream>

using namespace std;


const vector<string> sets = {"relWenshu", "directory", "s17", "s11", "s47", "s45", "s1", "s2", "s22", "s28", "s3","s43", "s6","viewCount", "globalNet"};
//vector<string> sets = {"s1", "s2", "s22", "s23", "s26", "s27", "s28", "s3", "s43", "s45", "s47", "s11", "s17", "relWenshu", "directory"};


set<string> get_omit(vector<string> sets)
{
    set<string> myset;
    for(size_t i = 0; i < sets.size(); ++i)
    {
        myset.insert(sets[i]);
    }
    return myset;
}


void showvec(const vector<vector<string> > data)
{
    size_t nums = data.size();
    for(int i = 0; i < nums; ++i)
    {
        for(size_t j = 0; j < data[0].size(); ++j)
        {
            cout << data[i][j] << endl;
        }
        cout << endl;
    }
}

set<string> showdir(string path, string flag)
{
    struct dirent *dirp;
    set<string> dir_vec;
    DIR *dp;
    // 转化为C风格的字符串 才行的。
    dp = opendir(path.c_str());
    while((dirp = readdir(dp)) != NULL)
    {
        //cout << dirp -> d_name << endl;
        string name = dirp -> d_name;
        size_t charpos = name.find(flag, 0);
        if(charpos != string::npos)
        {
            dir_vec.insert(name);
        }
    }
    return dir_vec;
}

void get_attr(string path)
{
    struct stat st;
    // 注意检查 文件路径是否真的存在，否则出现问题。
    if(-1 == stat(path.c_str(), &st))
    {
        cout << "stat failed " << endl;
        exit(EXIT_FAILURE);
    }
    else
    {
        cout << st.st_size / (1024 * 1024) << "M " << endl;
        // st.st_blocks << " " << st.st_nlink << endl;
    }
}


const set<string> omit_sets = get_omit(sets);
#endif