
#include "thread_pool.h"
#include <stdlib.h>
#include <cstdio>
#include <unistd.h>
#include <iostream>
#include <string>
using namespace std;

class mytask: public CTask
{
public:
    mytask() = default;

    int run()
    {
      cout << " -- " <<  m_ptrdata << endl;
      int x = rand() % 4 + 1;
      sleep(x);
      return 0;
    }
    ~mytask(){}

};

int main()
{
    mytask mt;
    string d = "hello world";
    mt.setdata(&d);

    CThreadPool tp(5);
    for(int i = 0; i < 10; ++i)
    {
        tp.addtask(&mt);

    }
    while(1)
    {
        cout << " least thread pool " << tp.gettasksize() << "----" << endl;
        if(tp.gettasksize() == 0)
        {
            if(tp.stopall() == -1)
            {
                cout << "thread pool clear, exit" << endl;
                exit(0);
            }
        }
        sleep(2);
        cout << "2 second s .." << endl;
    }
    return 0;
}