#include <json/json.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <vector>
#include <set>
using namespace std;


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

Json::Value def = []()
{
	Json::Value def;
	Json::CharReaderBuilder::setDefaults(&def);
	def["emitUTF8"] = true;
	return def;
}();


int main(int argc, char *argv[]) {
//	int a[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
//	cout<<"Row:0"<<a[0][0] <<' '<< a[0][1]<<' '<<a[0][2] <<endl;
//	cout<<"Row:0"<<a[2][0] <<' '<< a[2][1]<<' '<<a[2][2] <<endl;
//	cout<<"Row:0"<<a[1][0] <<' '<< a[1][1]<<' '<<a[1][2] <<endl;
//	cout<< a.size()<<endl;
	//string p = R"({""s1"":""p1""})";

//	string p = R"{""s1"":""xx""}";
//	cout << "test : " << p << endl; 
	//const auto rl = static_cast<int>(p.length());
	//cout << " rl is " << rl << endl;
	// Json::CharReaderBuilder builder;
	//unique_ptr<Json::CharReader> reader(builder.newCharReader());
	//JSONCPP_STRING errs;
	//Json::Value tx;
	//reader->parse(p.c_str(),p.c_str() + rl, &tx, &err);
	//cout << tx["s1"] << " -- " << endl;

	ifstream ifs;
	ifs.open(argv[1]);
	cout << " lems" << argc << endl;

	string ss;
	vector<vector<string> > nd;
	int count = 0;
	while(getline(ifs, ss))
	{
	    //cout << "ele " << ss << endl;
//	    count++;
//	    if(count < 4)
//	    {
//	        continue;
//	    }
//	    else if(count > 44)
//	    {
//	        break;
//
//	    }

	    stringstream temp_s(ss);
	    string t_s;

	    vector<string> temp_n;
	    temp_n.reserve(5);

	    while(getline(temp_s, t_s, '\t'))
	    {
	        // cout << t_s << endl;
	        temp_n.push_back(t_s);

	    }
	    nd.push_back(temp_n);


//	    count++;
//	    if(count > 20)
//	    {
//	        break;
//	    }
//		Json::Value root;
//		JSONCPP_STRING errs;
//
//		string news = parsestr(ss, '"');
//
//		stringstream s(news);
//		if(parseFromStream(builder, s, &root, &errs))
//		{
//			data.push_back(root);
//		}
//		else
//		{
//			cout << errs << endl;
//		}
	}

	Json::CharReaderBuilder builder;
	JSONCPP_STRING errs;

	//builder["emitUTF8"] = true;
	//builder.settings_ = def;

	Json::Value root;
	vector<Json::Value> data;


	cout << "total  case: " << nd.size() << endl;
	cout << endl;
    for(size_t i = 0; i < nd.size(); ++i)
    {
        string news = parsestr(nd[i][2], '"');

        //cout << news << endl;

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

    set<string> myset;
    vector<string> sets = {"s1", "s2", "s22", "s23", "s26", "s27", "s28", "s3", "s43", "s45", "s47", "s11", "s17", "relWenshu", "directory"};
    for(size_t i = 0; i < sets.size(); ++i)
    {
        myset.insert(sets[i]);
    }


	for(size_t i = 0 ; i < data.size(); ++i)
	{

	    Json::Value::Members members;
	    members = data[i].getMemberNames();
	    //cout << members[0] << members.size() << endl;

	    cout << " case " << i << "-------------------------------- ::" << endl;
	    cout << endl;

	    for(size_t j=0; j < members.size(); ++j)
	    {
	        string key = members[j];
	        // cout << key << " : " <<  data[i].get(key, "UTF-8").asString << endl;

	        if(key == "qwContent")
	        {
	            string p = data[i].get("qwContent", "UTF-8").asString();
//		        cout << "ele is----"  << i  << endl;
//	            cout << " " << p << endl;


                if(p.substr(0, 14) == "<!DOCTYPE HTML")
	            {
	                //cout << " p is " << p.substr(0, 14) << endl;
	                size_t ap = p.find("<div", 0);
	                size_t end = p.find("</div>", 0);
	                    //if(ap != string::npos && end != string::npos)
		                    //    cout << lks.substr(ap, end) << endl;
                    while(ap != string::npos && end != string::npos)
                    {
                            //cout << "--vi----" << lks.substr(ap, end-1) << endl;

                        string sub_string = p.substr(ap, end-1);

                        size_t ap_s = sub_string.find("'>", 0);
	                    size_t end_s = sub_string.find("</", 0);
	                    size_t dis = end_s - ap_s - 2 ;
	                    if( ap_s != string::npos && end_s != string::npos)
	                    {
	                            //cout << "vi---  " << sub_string.substr(ap_s + 2, string::npos) << endl;
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
	                //cout << endl;
//	                // 这里对部分数据没法使用。
	                while(getline(lk, lks, '\n'))
	                {
	                    size_t ap = lks.find("</div>", 0);
	                    if(ap != string::npos)
	                    cout << lks.replace(ap, 6, "") << endl;
	                }

	            }

//                const char stars = "'>";
//                const char ends = "<div";

//	            while(getline(lk, lks, '\n'))
//	            {
//	                size_t ap = lks.find("<div", 0);
//	                size_t end = lks.find("</div>", 0);
////	                if(ap != string::npos && end != string::npos)
////	                    //cout << lks.replace(ap, 6, "") << endl;
////	                    cout << lks.substr(ap, end) << endl;
//                    while(ap != string::npos && end != string::npos)
//                    {
//                            //cout << "--vi----" << lks.substr(ap, end-1) << endl;
//
//                            string sub_string = lks.substr(ap, end-1);
//
//                            size_t ap_s = sub_string.find("'>", 0);
//	                        size_t end_s = sub_string.find("</", 0);
//	                        size_t dis = end_s - ap_s - 2 ;
//	                        if( ap_s != string::npos && end_s != string::npos)
//	                        {
//	                            //cout << "vi---  " << sub_string.substr(ap_s + 2, string::npos) << endl;
//	                            cout << "vp---  " << sub_string.substr(ap_s + 2, dis) << endl;
//
//	                        }
//                            ap = lks.find("<div", ap + 1);
//                            end = lks.find("</div>", end);
//                    }
//
//	            }
	            cout << endl;
	        }
	        else if(key == "wenshuAy")
	        {
	            //cout << key << " : " << data[i][key].isArray() << endl;
	            //cout << key << " : " << data[i][key][0].get("text", "UTF-8").asString() << endl;
	            string t_k = data[i][key][0].get("text", "UTF-8").asString();
	            cout << "案由  " << t_k << endl;
//	            data[i][key][0]["text"] = t_k;
//	            cout << key << " : " << data[i][key]<< endl;

	        }
	        else if(myset.find(key) != myset.end())
	        {
	            continue;
	        }
	        else
	        {
	            //continue;
	            auto temp = data[i].get(key, "UTF-8");
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

	    cout << endl;

	    //cout << data[i].get() << "----" << endl;
//	    string p = data[i].get("qwContent", "UTF-8").asString();
//		cout << "ele is----"  << i  << endl;
//	    cout << " " << p << endl;
//
//	    stringstream lk(p);
//	    string lks;
//	    while(getline(lk, lks, '\n'))
//	    {
//	        size_t ap = lks.find("</div>", 0);
//	        if(ap != string::npos)
//	            cout << lks.replace(ap, 6, "") << endl;
//	    }
	}

	ifs.close();

	return 0;

}

// g++ json2str.cpp -o json2str -ljsoncpp -std=c++11 && json2str /Users/luokui/sd.txt
// g++ json2str.cpp -o json2str -ljsoncpp -std=c++11 && json2str /Users/luokui/sd.txt > t.log