#ifndef PARSERDATA_H
#define PARSERDATA_H


#include <json/json.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <vector>
#include <set>

#include "readdata.h"
#include "parserjson.h"

using namespace std;

const vector<string> sets = {"relWenshu", "directory", "s17", "s11", "s47", "s45", "s1", "s2", "s22"};
//vector<string> sets = {"s1", "s2", "s22", "s23", "s26", "s27", "s28", "s3", "s43", "s45", "s47", "s11", "s17", "relWenshu", "directory"};


void procdata(Json::Value data)
{
    // 过滤掉部分不需要的数据
    set<string> myset;
    for(size_t i = 0; i < sets.size(); ++i)
    {
        myset.insert(sets[i]);
    }

    // 解析数据
	Json::Value::Members members;
	members = data.getMemberNames();

	for(size_t j=0; j < members.size(); ++j)
	{
	    string key = members[j];
	    // cout << key << " : " <<  data[i].get(key, "UTF-8").asString << endl;

	    if(key == "qwContent")
	    {
	        string p = data.get("qwContent", "UTF-8").asString();

            if(p.substr(0, 14) == "<!DOCTYPE HTML")
	        {
	            //cout << " p is " << p.substr(0, 14) << endl;
	            size_t ap = p.find("<div", 0);
	            size_t end = p.find("</div>", 0);
                while(ap != string::npos && end != string::npos)
                {
                    string sub_string = p.substr(ap, end-1);
                    size_t ap_s = sub_string.find("'>", 0);
	                size_t end_s = sub_string.find("</", 0);
	                size_t dis = end_s - ap_s - 2 ;
	                if( ap_s != string::npos && end_s != string::npos)
	                {
	                    cout << sub_string.substr(ap_s + 2, dis) << endl;

	                }
                    ap = p.find("<div", ap + 1);
                    end = p.find("</div>", end);
                }

	        }
	        else
	        {
	            stringstream lk(p);
	            string lks;
	            // 这里对部分数据没法使用。
	            while(getline(lk, lks, '\n'))
	            {
	                size_t ap = lks.find("</div>", 0);
	                if(ap != string::npos)
	                    cout << lks.replace(ap, 6, "") << endl;
	            }

	        }
	        cout << endl;
	    }
	    else if(key == "wenshuAy")
	    {
	        //cout << key << " : " << data[i][key].isArray() << endl;
	        //cout << key << " : " << data[i][key][0].get("text", "UTF-8").asString() << endl;
	        string t_k = data[key][0].get("text", "UTF-8").asString();
	        cout << "案由  " << t_k << endl;
	    }
	    else if(myset.find(key) != myset.end())
	    {
	        continue;
	    }
	    else
	    {
	        auto temp = data.get(key, "UTF-8");
	        if(temp.isString())
	        {
	            cout << key << " : " << temp.asString() << endl;
	        }
	        else
	        {
	            cout << key << " : " << temp.toStyledString() << endl;
	        }
	    }
	}
}


#endif