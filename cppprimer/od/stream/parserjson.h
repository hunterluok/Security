#ifndef PARSERJSON_H
#define PARSERJSON_H

#include <json/json.h>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

string parsestr(const string&, const char);
vector<Json::Value>  getjson(const vector<vector<string> >, const int position = 2, const char delimiter = '"');


string parsestr(const string& forfun, const char mychar)
{
	string news = "";
	size_t i = 0;

	for(; i < forfun.length(); ++i)
	{
        if(i == 0 && forfun[i]== mychar)
        {
            continue;
        }
        else if(i == forfun.length() - 1)
        {
            continue;
        }
        else
        {
            if(forfun[i] == forfun[i-1] && forfun[i] == mychar)
            {
                continue;
                //++i;
                //i = i+1;
            }
            else
            {
                news += forfun[i];
            }
        }
	}
	//cout << endl;
	//cout << "new string is " << news << endl;
	return news;

}

vector<Json::Value>  getjson(const vector<vector<string> > nd, const int position, const char delimiter)
{
    Json::CharReaderBuilder builder;
	JSONCPP_STRING errs;
	Json::Value root;
	vector<Json::Value> data;
//	cout << "total  case: " << nd.size() << endl;
//	cout << endl;
    for(size_t i = 0; i < nd.size(); ++i)
    {
        // 将特定 的feild 解析为 json, 这里过滤掉了部分数据。
        string news = parsestr(nd[i][position], delimiter);

        stringstream s(news);
		if(parseFromStream(builder, s, &root, &errs))
		{
			data.push_back(root);
		}
		else
		{
			//cout << errs << endl;
			continue;
		}
        //cout << "*** " << parsestr(nd[i][2], '"') << endl;
    }
    return data;
}

#endif