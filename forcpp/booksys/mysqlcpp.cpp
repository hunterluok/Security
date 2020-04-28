#include<errno.h>
#include<stdio.h>
#include<string>
#include<iostream>
#include<mysql.h>

using namespace std;

#define host "localhost"
#define user "root"
#define pass "root"
#define db "lktest"


static inline void _mysql_check(MYSQL* con) {
    fprintf(stderr, "%s", mysql_error(con));
//    std::cerr << mysql_error(con) << std::endl;
    //mysql_close(con);
    exit(EXIT_FAILURE);
}

int main()
{
    MYSQL* con=mysql_init(0);
    MYSQL_RES* result=NULL;
    MYSQL_FIELD *fd;
    MYSQL_ROW sql_rom;
    std::cout << con << std::endl;
    mysql_options(con,
        MYSQL_SET_CHARSET_NAME,
        MYSQL_AUTODETECT_CHARSET_NAME);
    /*if (!mysql_real_connect(con, host, user, pass, db, 3306, NULL, 0)) {
        _mysql_check(con);
    }
    */
    con = mysql_real_connect(con, host, user, pass, db, 3306, NULL, 0);
    if (con) {
        if (!mysql_select_db(con, db)) {
            printf("connect successfule \n");
            mysql_options(con, MYSQL_SET_CHARSET_NAME, "gbk");
            if (!mysql_query(con, "SELECT * FROM student"))
            {
                result = mysql_store_result(con);
                int j = mysql_num_fields(result);
                for (int i = 0; mysql_fetch_field(result); i++) {
                    printf("%s\t", "ok ");
                }
                printf("\n");
                while (mysql_fetch_row(result)) {
                    for (int i = 0; i < j; i++) {
                        cout << "sss " << endl;
                    }
                    printf("\n");
                }
            }
        }

    }
    mysql_free_result(result);
    mysql_close(con);
    getchar();
    return 0;
}