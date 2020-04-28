//
//  Header.h
//  learncpp
//
//  Created by 罗奎 on 2020/4/27.
//  Copyright © 2020 罗奎. All rights reserved.
//

#ifndef connmysql_h
#define connmysql_h

#include <iostream>
#include <string>
#include <vector>
#include <mysql.h>
#include <json.h>


using namespace std;


class ConnectMysql
{
    
public:
    ConnecMysql();
    ~ConnectMysql();

private:
    string port;
    string ip;
    string host;
    string dbname;
}


#endif /* Header_h */
