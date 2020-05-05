//
//  main.cpp
//  learncpp
//
//  Created by 罗奎 on 2020/4/26.
//  Copyright © 2020 罗奎. All rights reserved.
//

#include <iostream>
#include <mysql.h>
#include <vector>
#include <iomanip>
#include <json/json.h>
//#include <json.h>

#include "kmalgo.h"
#include "util.h"


using namespace std;

template<typename T>
void showvec(vector<vector<T> > data)
{
    long int m = data.size();
    long n = data[0].size();
    for(int i = 0; i < m; ++i)
    {
        for(int j = 0; j < n; ++j)
        {
            cout << data[i][j] << " ";
        }
        cout << endl;
    }
    cout << "show over" << endl;
}

//template<typename T>
vector<vector<float> > my_select(MYSQL *conn)
{
    vector<vector<float> > data;
    const char *sql = "select * from nd";
    
    int ret = mysql_query(conn, sql);
    if (ret != 0)
    {
        cout << "error:%s\n" << mysql_error(conn) << endl;
        system("pause");
        exit(1);
    }
    
    MYSQL_RES *result = mysql_store_result(conn);
    if (NULL == result)
    {
        cout << "error " << mysql_errno(conn) << " " << mysql_error(conn) << endl;;
        system("pause");
        exit(1);
    }
    else
    {
        my_ulonglong  num_rows = mysql_num_rows(result);
        cout << "data size is " << (int)num_rows << endl;
 
        unsigned int num_fields = mysql_num_fields(result);
        cout << "number of fields: "  << (int)num_fields << endl;
 
        MYSQL_ROW row = mysql_fetch_row(result);
        
        while(row)
        {
            vector<float> temp_line;
            for(int i = 0; i < num_fields; ++i)
            {
                float b = atof(row[i]);
                temp_line.push_back(b);
            }
            data.push_back(temp_line);
            row = mysql_fetch_row(result);
        }
        mysql_free_result(result);
    }
    return data;
}

//int main (int argc, const char * argv[])
//{
//    MYSQL *connection, conn;
//    mysql_init(&conn);
//    connection = mysql_real_connect(&conn,"127.0.0.1","root","root","hs300",0,0,0);
//    if (connection == NULL)
//    {
//        //unable to connect
//        printf("Oh Noes!\n");
//    }
//    else
//    {
//        printf("Connected.\n");
//        vector<vector<float> > data;
//        data = my_select(&conn);
//        // showvec(data);
//        mysql_close(&conn);
//
//
//        cout << setiosflags(ios::fixed) << setprecision(2);
//
//        kmeans myk(2, 10, 0.001);
//        vector<vector<float> > result;
//        result = myk.fit(data);
//        writedata("data.txt", result);
//    }
//    return 0;
//}


class my
{
public:
    virtual void show()
    {
        cout << "test1 " << endl;
    }
};


class my2: public my
{
public:
    void show()
    {
        cout << "test2" << endl;
    }
};

void sh(my& d)
{
    d.show();
}

int main()
{
    
    my2 tx;
    sh(tx);
    
    ifstream myfile("/Users/luokui/text.txt", ios::in);
    vector<vector<string> > data;
    const char delim = '|';
    if(myfile)
    {
        string s;
        while(getline(myfile, s))
        {
            // cout << "content is " << s << endl;
            stringstream temp(s);
            string tx;
            vector<string> temp_data;
            while(getline(temp, tx, delim))
            {
                //if(tx.length() > 10)
                if(strlen(tx.c_str()) > 10)
                {
                    temp_data.push_back(tx);
                }
            }
            data.push_back(temp_data);
        }
    }
    else
    {
        system("wrong");
        exit(1);
    }
    myfile.close();
    
    showvec(data);
    cout << "m " << data.size() << endl;
    cout << "n " << data[0].size() << endl;

    return 1;
}
