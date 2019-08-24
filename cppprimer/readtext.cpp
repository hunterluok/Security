#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <regex>
#include <vector>
using namespace std;


float fsing(float x)
{
	float temp = exp(-x);
	return 1 / ( 1 + temp);
}


int main()
{
	ofstream myfile;
	myfile.open("hello.txt", ios_base::out); // | ios_base::app);

	if(myfile.is_open())
	{
		cout << "out data" << endl;
		myfile << "1" << endl;
		cout << "ovee" << endl;
		myfile.close();
	}


	vector<int> temp_line;
	vector< vector<int> > Vec_Dti;

	regex pat_regex("[[:digit:]]+"); 


	ifstream myfile_old;
	myfile_old.open("t.txt", ios_base::in);

	if(myfile_old.is_open())
	{
		string line;

		while(myfile_old.good())
		{
			getline(myfile_old, line);
			// cout << line <<  line.size() <<  endl;

			for (sregex_iterator it(line.begin(), line.end(), pat_regex), end_it; it != end_it; ++it) 
			{  //表达式匹配，匹配一行中所有满足条件的字符
            // cout << it->str() << " ";  //输出匹配成功的数据
				temp_line.push_back(stoi(it->str()));  
				//temp_line.push_back((it->str()).toDouble());
            //将数据转化为int型并存入一维vector中
        	}
        	Vec_Dti.push_back(temp_line);  //保存所有数据
        	temp_line.clear();
		}
		myfile_old.close();
	}
	else
	{
		cout <<"open failed () " << endl;
	}




	for(int i=0; i <Vec_Dti.size(); i++) 
	{  //输出存入vector后的数据
        for(int j=0; j<Vec_Dti[0].size(); j++) 
        {
            cout << Vec_Dti[i][j] << " ";
        }
        cout << endl;
    }
    
    cout << Vec_Dti[0].size() << endl;

	float resut = fsing(0);
	cout << "result : " << resut << endl;

	return 0;
}