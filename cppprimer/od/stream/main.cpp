#include <iostream>
#include <vector>
#include <json/json.h>

#include "readdata.h"
#include "parserjson.h"
#include "parserdata.h"

using namespace std;


// #理想的方式 是边读取数据编写入数据
int main(int argc, char *argv [])
{
    vector<vector<string> > nd;
    //读取原始数据
    nd = readdata(argv[1]);
    // 获取json数据
	vector<Json::Value> data = getjson(nd);
	//解析数据
	for(size_t i = 0; i < data.size(); ++i)
	{
	    try
	    {
	        cout << "case " << i << "-------------" << endl;
	        procdata(data[i]);
	        cout << endl;
	    }
	    catch(const char* err)
	    {
	        cout << "err " << err << endl;
	    }
	}
	return 0;
}
