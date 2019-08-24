#include <iostream>
using namespace std;


template<typename T> class hashtable
{
public:
	hashtable(int size)
	{
		maxsize = size;
		count = 0;
		elements = new T[size];

		if(elements == NULL)
		{
			exit(-1);
		}
		for (int i=0; i < maxsize; ++i)
		{
			elements[i] = 0;
		}
	}
	~hashtable()
	{
		delete [] elements;
	}

	int hash(T value);
	int searchhash(T value);
	bool insertdata(T value);

	T getdata(int i)
	{
		if(i <= 0)
		{
			cout << " i must >=0 " << endl;
			exit(-1);
		}
		return elements[i-1];
	}

private:
	int maxsize;
	T *elements;
	int count;
};


template<typename T> int hashtable<T>:: hash(T value)
{
	return value % maxsize;
}

template<typename T> int hashtable<T>:: searchhash(T value)
{
	int m = hash(value);
	if(elements[m] == value)
	{
		return m;
	}

	int rp = (m+1) % maxsize;
	while( rp != m)
	{
		if(elements[rp] == value)
			return rp;
		if(elements[rp] == 0)
			break;
		rp = (rp + 1) % maxsize;
	}

	if (rp == m)
		return -1;
	else
	{
		elements[rp] = value;
		return rp;
	}
}

template<typename T> bool hashtable<T>:: insertdata(T value)
{
	int p = hash(value);
	if( p < 0)
	{
		return false;
	}
	else if(elements[p] == value)
	{
		cout<< " value is already exits: " << value << endl;
		return false;
	}
	else
	{
		elements[p] = value;
		return true;
	}
}

int main()
{
	//T table = new hashtable(10);
	int maxsize = 10;
	hashtable<int> mytable = hashtable<int>(maxsize);
	mytable.insertdata(11);
	mytable.insertdata(22);
	mytable.insertdata(33);
	mytable.insertdata(44);
	mytable.insertdata(13);
	mytable.insertdata(21);
	mytable.insertdata(35);
	//mytable.insertdata(44);

	int p = mytable.searchhash(21);
	cout << "  : " << p << endl;
	mytable.searchhash(100); // 如果不存在 则存入到数据中去

	for(int i=1; i<maxsize; ++i)
	{
		cout << " shuchu :" << mytable.getdata(i) << endl;
	}
	return 0;
}


