#include <iostream>
#include <vector>
#include <json/json.h>
#include <sstream>
#include <string>
#include <set>
#include <time.h>

#include <sys/stat.h>
#include <sys/types.h>
#include <stdio.h>
#include <thread>
#include <mutex>

#include "mlpack/core.hpp"

#include "parserjson.h"
#include "parserdata.h"
#include "util.h"

using namespace std;

void etl_data(string path, string batch_num);
void thread_func(string path, string batch_num);

mutex mtx;


int main(int argc, char *argv [])
{
    if(argc != 4)
    {
        exit(EXIT_FAILURE);
    }

//    const string mydirs = "/Users/luokui/oddata/";
//    const string flag = "new";
    const string mydirs = argv[1];
    const string flag = argv[2];

    set<string> dirs = showdir(mydirs, flag);
    vector<string> full_dirs;
    for(auto ele = dirs.begin(); ele != dirs.end(); ++ele)
    {
        string temp = mydirs + *ele;
        // cout << "temp is " << temp << endl;
        full_dirs.push_back(temp);
    }

    const string batch_num1 = argv[3];

    clock_t start, finish;
    start = clock();

    const int num_thread = 2;
    std::thread mythreads[num_thread];
    for(size_t i = 0; i < num_thread; ++i)
    {
        mythreads[i] = std::thread(thread_func, full_dirs[i], batch_num1);
    }
    for(auto& single_thread : mythreads)
    {
        single_thread.join();
    }
    //cout << " all threads joined " << endl;

    finish = clock();
    double t = (finish - start ) / CLOCKS_PER_SEC;
    cout << "total consum time is " <<  t << endl;


    return 0;
}


void thread_func(string path, string batch_num)
{
    if(mtx.try_lock())
    {
        etl_data(path, batch_num);
        mtx.unlock();
    }
    else
    {
        cout << " try lock failed" << endl;
    }

}


void etl_data(string path, string batch_num)
{
    //首先检查文件是否存在；
    get_attr(path);
    // 打开文件进行读取。
	ifstream ifs;
	ifs.open(path, ios::in);
	if(!ifs.is_open())
	{
	    cout << " file is not opend " << endl;
	    exit(EXIT_FAILURE);
	}
	//获取文件的大小；
//	ifs.seekg(0, ifs.end);
//	int length = ifs.tellg();
//	ifs.seekg(0, ifs.beg);

    stringstream batc(batch_num);
	int batch_size = 0;
	batc >> batch_size;
	int count = 0;
	int batch_index = 0;

	string ss;
	vector<vector<string> > nd;

    // 这个地方处理batch 数据还有点问题，没法处理最后结尾的数据，这是一个问题啊。
	while(getline(ifs, ss))
	{
	    stringstream temp_s(ss);
	    string t_s;

	    vector<string> temp_n;
	    //这里注意数据的 维度为5；
	    // temp_n.reserve(5);

        // 切分数据的方法。
	    while(getline(temp_s, t_s, '\t'))
	    {
	        temp_n.push_back(t_s);

	    }
	    nd.push_back(temp_n);

	    count++;
	    if(count == batch_size)
	    {
	        // 获取json格式的数据。
	        vector<Json::Value> data = getjson(nd);
	        for(size_t i = 0; i < data.size(); ++i)
	        {
	            try
	            {
	                cout << "case " << i << endl;
	                //对数据进行清洗。
	                procdata(data[i], omit_sets);
	                cout << endl;
	            }
	            catch(const char* err)
	            {
	                cout << "err ---- " << err << endl;

	            }
	        }
	        // 初始化batch.得到新的结果。
	        count = 0;
	        nd.clear();
//	        cout << "batch idx " << batch_index << endl;
	        batch_index++;
	        if(batch_index > 1)
	            break;
	    }
	}
	ifs.close();
}
