#include <iostream>
#include <string>

using namespace std;

const int count = 0;

template<typename T> class mylists
{
public:
	mylists(int size)
	{
		maxsize = size;
		elements = new T[maxsize];
	}
	~mylists()
	{
		delete elements;
	}

    bool append(T value);
    bool find(T value);
    bool omit(T value);
    bool show();

private:
	int maxsize;
	T *elements;
	
};


template<typename T> bool mylists<T>::show()
{
	mylists<T>::iterator it=elements.begin();
	if(; it!=elements.end(); it++)
	{
		cout << "ele is : " << *it << endl;
 	}
 	return true;
};


template<typename T> bool mylists<T>::append(T value)
{
	return true;
};