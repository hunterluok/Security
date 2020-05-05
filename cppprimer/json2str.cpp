#include <json/json.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;


string parsestr(const string& forfun, const char mychar)
{
    // string forfun = "hheesdas ";
	string news = "";
	for(size_t i = 0; i < forfun.length(); ++i)
	{
	    //cout  << forfun[i];
        if(i == 0 && forfun[i]== mychar)
        {
            continue;
        }
        else
        {
            if(forfun[i] == forfun[i-1] && forfun[i] == mychar)
            {
                continue;
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
	Json::CharReaderBuilder builder;
	//unique_ptr<Json::CharReader> reader(builder.newCharReader());
	//JSONCPP_STRING errs;
	//Json::Value tx;
	//reader->parse(p.c_str(),p.c_str() + rl, &tx, &err);
	//cout << tx["s1"] << " -- " << endl;

	ifstream ifs;
	ifs.open(argv[1]);
	cout << " lems" << argc << endl;
	
	vector<Json::Value> data;
	string ss;
	while(getline(ifs, ss))
	{
		Json::Value root;
		JSONCPP_STRING errs;

		string news = parsestr(ss, '"');

		stringstream s(news);
		if(parseFromStream(builder, s, &root, &errs))
		{
			data.push_back(root);
		}
		else
		{
			cout << errs << endl;
		} 
	}


	for(size_t i = 0 ; i < data.size(); ++i)
	{
		cout << "ele is " << data[i] << endl;
	}

	ifs.close();
	return 0;

}

// g++ t1.cpp -o t1 -ljsoncpp -std=c++11 && t1 json.txt