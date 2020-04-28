#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <mysql.h>
#include <stdio.h>
//#include <mysql++/mysql++.h>
using namespace std;


template<typename T> void showvec(vector<vector<T> > data)
{
	int m = data.size();
	int n = data[0].size();
	for(int i = 0; i < m; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			cout << data[i][j] << " ";
		}
		cout << endl;
	}
}


void myower(vector<vector<int> >& data)
{
	int m = data.size();
	int n = data[0].size();
	for(int i = 0; i < m; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			data[i][j] = data[i][j] * data[i][j];
		}
	}
}


void readdata_text(string path, vector<vector<int> >& data)
{
	ifstream myfile(path, ios::in);
	if(myfile)
	{
		string lines;
		while(getline(myfile, lines))
		{
			istringstream temp_str(lines);
			vector<int> v;
			string s;
			while(temp_str >> s)
			{
				int temp = 0;
				stringstream ano;
				ano << s;
				ano >> temp;
				v.push_back(temp);
			}
			data.push_back(v);
		}
	}
	else
	{
		cout << "file is wrong " << endl;
	}
	myfile.close();
}


// void readdata_mysql()
// {
// 	string host = "localhost";
//     string user = "root";
//     string passwd = "root";
//     string db_name = "lktest";
//     int port = 3306;

//     MYSQL *con = mysql_init(0);

//     mysql_options(con, MYSQL_SET_CHARSET_NAME, MYSQL_AUTODETECT_CHARSET_NAME);

//     // MYSQL_RES *result;

//     // conn = mysql_real_connect(&mysql,"127.0.0.1","root","root","lktest",0,0,0);



//     if(mysql_real_connect(con, host.c_str(), user.c_str(), passwd.c_str(), db_name.c_str(), port, NULL, 0))
//     {
//     	cout << "connected " << endl;
//         // cout << "Error:  ------ " << mysql_error(mysql);
//         // exit(1);
//     }
//     mysql_close(con);
//     // string sqls = "select * from lktest limit 3";


//     // if (mysql_query(mysql, sqls.c_str())) {
//     //     cout<<"Query Error: "<<mysql_error(mysql);
//     // }


// }


int main (int argc, const char * argv[])
{
    MYSQL *connection, mysql;
    mysql_init(&mysql);
    connection = mysql_real_connect(&mysql,"127.0.0.1","root","root","lktest",0,0,0);
    if (connection == NULL)
    {
        //unable to connect
        printf("Oh Noes!\n");
    }
    else
    {
        printf("Connected.\n");
    }
    return 0;
}

// int main()
// {
// 	string path = "d.txt";

// 	vector<vector<int> > data;
// 	readdata_text(path, data);	
// 	myower(data);
// 	showvec(data);

// 	readdata_mysql();
// 	return 0;

// }
