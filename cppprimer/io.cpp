#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<fstream>
#include<sstream>

using namespace std;


void showdata(vector<string> data)
{
    vector<string>::iterator iter = data.begin();
    for(;iter!=data.end(); ++iter)
    {
        cout << *iter;
    }
    cout << " line " << endl;
}

//vector<string> spilt(string data)
//{
//    vector<string> newdata;
//    for(int i=0; i<data.size(); ++i)
//    {
//        if(data[i] == ' ')
//        {
//            continue;
//        }
//        else
//        {
//            newdata.push_back(data[i]);
//        }
//    }
//    return newdata;
//}


int main()
{
//	cout << " pi :" ;
	// int a = 0;
	// cin >> a;

//	double pi = double(22.0) / 7 ;
//	double a = pi;
//	cout << setprecision(3) << endl;  // 4位有效数字 不包含 小数点
//	// cout << scientific << endl;   // 科学计数法的 有效数字 与 上面的 不同 增加了一位。
//
//    cout << setw(10);
//    // cout << setfill("*") ;
//
//	cout << "aaa :" << oct << a << endl;
//	cout << "bbb :" << hex << a << endl;
//
//	cout << setw(20) << setfill('*') << endl;   // setfill 只适合于 字符串，不适合其他的东西。
//	cout << "Integers " << endl;

	// cout << setiosflags(ios_base::hex | ios_base::showbase | ios_base::uppercase) << endl;
	// cout << a << endl;

	string myn;
    // cin >> myn;
	// getline(cin, temp, ' '); //这里的区别
	vector<float> myvector;
	string temp;
	while(getline(cin, myn))
	{
	    string temp;
	    istringstream line(myn);
	    while(line >> temp)
	    {
	        cout << "temp is " << temp << endl;
	        float temp_float;
	        stringstream << temp;
	        stringstream >> temp_float;
	        myvector.push_back(temp_float);
	    }
	}
    // showdata(myvector);
    for(int i=0; myvector.size(); ++i)
    {
        cout << "ele is " << myvector[i] << endl;
    }
	// cout << "myn :  --" << temp << endl;
    // string temp;
	// cout << myn[0] << "size is "<< myn.size() << endl;
//    vector<float> myvector;
//    while(getline(myn, temp, ' '))
//    {
//        myvector.push_back(stoi(temp));
//    }
//    // myvector = spilt(myn);

//    iostream myfile;
//    myfile.open("t.txt"; ios::in)
	return 0;
}