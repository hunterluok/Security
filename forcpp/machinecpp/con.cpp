#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <typeinfo>
#include "conv_util.h"

using namespace std;

// template <typename T>
// bool cal_conv(T& data, )

int main(int argc, char* argv[])
{
	// string path = argv[1];
	// cout << " " << argv[0]  << " " << argc << endl;
	string path = "t.txt";
	ifstream myfile(path, ios::in);

	if (!myfile)
	{
		cout << "file is bad" << endl;
		return 0;
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
	showvec(newdata);
	// vector<vector<int> > result;
	// result = dot_multiply(newdata, newdata);
	// showvec(result);
	vector<vector<int > > kernel;
	for(int i = 0; i < 2; ++i)
	{
		vector<int > v;
		if( i % 2 == 0)
		{
			v.push_back(1);
			v.push_back(0);
		}
		else
		{
			v.push_back(0);
			v.push_back(1);
		}
		kernel.push_back(v);
	}
	cout << " kernel is : " << endl;
	showvec(kernel);

	cout << " cal con v " << endl;
	vector<vector<int > > conv;
	conv = cal_conv(newdata, kernel);
	showvec(conv);
	// cout << typeid(conv).name() << endl;

	cout << " max polling is "  << conv.size() << endl;
	vector<vector<int> > pool_data;
	string flag = "max";
	vector<int> pool_kernel(2, 2);
	//vector<int> pool_kernel(2, 2);
	cout << pool_kernel[0] << " -- " <<  pool_kernel.size() << endl;
	pool_data = cal_pool(conv, pool_kernel, flag);
	showvec(pool_data);

	// cout << "row is " << rows << " cols is " << cols << endl;
	return 0;
}