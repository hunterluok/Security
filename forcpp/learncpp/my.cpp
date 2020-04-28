#include "util.h"
#include "bayes.h"

#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <iomanip>
#include <cmath>


using namespace std;


vector<map<int, float> > get_pris(vector<int> label)
{
	map<int, int> mymap;
	for(int i=0; i < label.size(); ++i)
	{
		mymap[label[i]]++;
	}

	float sums = 0.0;
	for(map<int, int>::iterator iter=mymap.begin(); iter != mymap.end(); ++iter)
	{
		sums += iter -> second;
	}
	// cout << " ------" << endl;
	// showmap(mymap);
	// // cout << "-------" << endl;
	// cout << "sums is " << sums << endl;

	vector<map<int, float> > pri;
	for(map<int, int>::iterator iter=mymap.begin(); iter != mymap.end(); ++iter)
	{
		// sums += iter -> second;
		map<int, float> temp_map;
		int key = iter -> first;
		float temp_pri = mymap[key] / sums;
		temp_map[key] = temp_pri;
		pri.push_back(temp_map);

	}
	//vector<float> pri;

	return pri;
}



int main()
{
	// string path = "iris.txt";
	// vector<vector<float> > data;
	// testreaddata(path, data);
	// cout << "data " << data[0][0] << endl;
	//showdata(data[0]);
	cout << setiosflags(ios::fixed) << setprecision(2);

	mybaye mys(2);

	cout << mys.get_a() << endl;

	vector<int> sumt1(4, 5);

	float s = 0.0;
	s = sumdata(sumt1);
	cout << "s is " << s << endl;

	std::vector<int> myv;
	myv.push_back(1);
	myv.push_back(3);
	myv.push_back(2);
	myv.push_back(2);

	map<int, int> mymap;
	for(int i = 0; i < myv.size(); ++i)
	{
		mymap[myv[i]]++;
	}

	map<int, int>::iterator iter = mymap.begin();
	for(; iter != mymap.end(); ++iter)
	{
		cout << "key is " << iter->first << "value is " << iter->second << endl;
	}

	cout << "--" << endl;

	vector<map<int, float> > pri;
	pri = get_pris(myv);

	for(int i = 0; i < pri.size(); ++i)
	{
		showmap(pri[i]);
		cout << endl;
	}

	cout << log(10) << " log vaue" << endl;

	return 0;
}

// bool testreaddata(string path,  vector<vector<float> >& data)
// {
// 	ifstream myfile(path, ios::in);
//    	if(!myfile)
//    	 {
//         	cout << "打开文件出错" << endl;
//         	return false;
//     	}

//     // 如何 一行行的 读入 vector 方便进行计算。
// 	// float index, a , b ,c, d;
// 	string myn;
// 	while(getline(myfile, myn))
// 	{
// 		vector<float> temp_vector;
// 		// 这里在一定程度上可以 优化性能。
// 		temp_vector.reserve(4);

// 		istringstream line(myn);
// 		// string temp_index;
// 		string temp_index;
// 		line >> temp_index;

// 		string temp;
// 		while(line >> temp)
// 		{
// 		    float temp_float=0.0;
// 		    stringstream another;
// 		    another << temp;

// 		    another >> temp_float;
// 			temp_vector.push_back(temp_float);
// 			// cout << "temp_veser capacity " << temp_vector.capacity() << endl;
// 		}
// 		data.push_back(temp_vector);

// 	}

// //	while(myfile >> index >> a >> b >> c >> d)
// //	{
// //		vector<float> temp_vec;
// //		temp_vec.push_back(a);
// //		temp_vec.push_back(b);
// //		temp_vec.push_back(c);
// //		temp_vec.push_back(d);
// //		data.push_back(temp_vec);
// //	}
// 	myfile.close();
// 	return true;
// }


// int main()
// {
// 	string path = "iris.txt";
// 	vector<vector<float> > data;
// 	testreaddata(path, data);
// 	// cout << "data " << data[0][0] << endl;
// 	showdata(data[0]);
// 	return 0;
// }
