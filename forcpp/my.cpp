#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

bool readdata(string path,  vector<vector<float> >& data)
{
	ifstream myfile(path, ios::in);
   	if(!myfile)
   	 {
        	cout << "打开文件出错" << endl;
        	return false;
    	}

    // 如何 一行行的 读入 vector 方便进行计算。
	// float index, a , b ,c, d;
	string myn;
	while(getline(myfile, myn))
	{
		vector<float> temp_vector;
		istringstream line(myn);
		// string temp_index;
		string temp_index;
		line >> temp_index;

		string temp;
		while(line >> temp)
		{
		    float temp_float=0.0;
		    stringstream another;
		    another << temp;

		    another >> temp_float;
			temp_vector.push_back(temp_float);
		}
		data.push_back(temp_vector);

	}

//	while(myfile >> index >> a >> b >> c >> d)
//	{
//		vector<float> temp_vec;
//		temp_vec.push_back(a);
//		temp_vec.push_back(b);
//		temp_vec.push_back(c);
//		temp_vec.push_back(d);
//		data.push_back(temp_vec);
//	}
	myfile.close();
	return true;
}


int main()
{
	string path = "iris.txt";
	vector<vector<float> > data;
	readdata(path, data);
	cout << "data " << data[0][0] << endl;
	return 0;
}
