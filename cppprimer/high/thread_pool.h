#ifndef THREAD_POOL_H
#define THREAD_POOL_H

#include <vector>
#include <string>
#include <pthread.h>

using namespace std;

class CTask
{
protected:
    string m_strtaskname;
    void* m_ptrdata;

public:
    CTask() = default;
    CTask(string &name): m_strtaskname(name), m_ptrdata(NULL){}
    virtual int run() = 0;
    void setdata(void* data);
    virtual ~CTask(){}
};

class CThreadPool
{
private:
    static vector<CTask* > m_vectasklist;
    static bool shutdown;

    int m_threadnum;
    pthread_t *pthread_id;

    static pthread_mutex_t m_pthreadmutex;
    static pthread_cond_t m_pthreadcond;

protected:
    static void* ThreadFunc(void* threaddata);
    static int movetoidel(pthread_t tid);
    static int movetobusy(pthread_t tid);
    int create();

public:
    CThreadPool(int m_threadnum);
    int addtask(CTask *task);
    int stopall();
    int gettasksize();

};


#endif