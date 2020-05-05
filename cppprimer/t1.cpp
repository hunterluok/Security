#include <json/json.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

int main() {
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


	Json::Value root;
	ifstream ifs;
	ifs.open("json.txt");
	
	vector<Json::Value> data;
	string ss;
	while(getline(ifs, ss))
	{
		Json::Value root;
		JSONCPP_STRING errs;
		stringstream s(ss);
		if(parseFromStream(builder, s, &root, &errs))
		{
			data.push_back(root);
		}
		else
		{
			count << errs << endl;
		} 
	}


	for(size_t i = 0 ; i < data.size(); ++i)
	{
		cout << "ele is " << data[i] << endl;
	}

	ifs.close();
	return 0;

}

