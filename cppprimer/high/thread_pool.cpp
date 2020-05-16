#include <cstdio>
#include <iostream>

#include "thread_pool.h"

using namespace std;

void CTask::setdata(void* data)
{
    m_ptrdata = data;

}

//
vector<CTask*> CThreadPool::m_vectasklist;
bool CThreadPool::shutdown = false;
pthread_mutex_t CThreadPool::m_pthreadmutex  = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t CThreadPool::m_pthreadcond = PTHREAD_COND_INITIALIZER;


CThreadPool::CThreadPool(int threadnum)
{
    this -> m_threadnum = threadnum;
    cout << "i will cread " << threadnum << " threads" << endl;
    create();
}

void* CThreadPool::ThreadFunc(void* threaddata)
{
    pthread_t tid = pthread_self();
    while(1)
    {
        pthread_mutex_lock(&m_pthreadmutex);
        while(m_vectasklist.size() == 0 && !shutdown)
        {
            pthread_cond_wait(&m_pthreadcond, &m_pthreadmutex);
        }
        if(shutdown)
        {
            pthread_mutex_unlock(&m_pthreadmutex);
            cout << " tid :" << pthread_self() << " exited" << endl;
            pthread_exit(NULL);

        }
        vector<CTask*>::iterator ele = m_vectasklist.begin();
        CTask* task = *ele;
        if(ele != m_vectasklist.end())
        {
            task = *ele;
            m_vectasklist.erase(ele);
        }

        pthread_mutex_unlock(&m_pthreadmutex);
        task -> run();
        cout << "tid " << tid << endl;
    }
    return (void*) 0;
}

int CThreadPool::addtask(CTask* task)
{
    pthread_mutex_lock(&m_pthreadmutex);
    m_vectasklist.push_back(task);
    pthread_mutex_unlock(&m_pthreadmutex);
    pthread_cond_signal(&m_pthreadcond);
    return 0;
}

int CThreadPool::create()
{
    pthread_id = new pthread_t[m_threadnum];
    for(int i = 0; i < m_threadnum; ++i)
    {
        pthread_create(&pthread_id[i], NULL, ThreadFunc, NULL);
    }
    return 0;

}

int CThreadPool::stopall()
{
    if(shutdown)
        return -1;

    shutdown = true;
    pthread_cond_broadcast(&m_pthreadcond);

    for(int i = 0; i < m_threadnum; ++i)
    {
        pthread_join(pthread_id[i], NULL);
    }
    delete [] pthread_id;
    pthread_id = NULL;
    pthread_mutex_destroy(&m_pthreadmutex);
    pthread_cond_destroy(&m_pthreadcond);
    return 0;

}

int CThreadPool::gettasksize()
{
    return m_vectasklist.size();
}
