#include <iostream>
#include <fstream>
using namespace std;


template<typename T> class seqlist
{
public:
	seqlist(int size)
	{
		maxsize = size;
		length = 0;
		elements = new T[maxsize];
	}
	~seqlist()
	{
		delete [] elements;
		//  使用了 new 所以使用 析构函数处理下。
	}
	bool insertdata(T data);
	T show_data(int pos);
	bool delete_data(int pos);
	bool change_data(int pos, T data);

	int get_size()
	{
		return length;
	}
private:
	int maxsize;
	int length;
	T *elements;
};


template<typename T> bool seqlist<T> ::insertdata(T data)
{
	int  currentList = length;
	if(currentList < maxsize)
	{
		elements[currentList] = data;
		length ++;
		return true;
	}
	else
	{
		return false;
	}
}

template<typename T> bool seqlist<T>::change_data(int pos, T data)
// 这里的方法需要注意。
{
	if(pos > length || pos < 0)
	{
		cout <<" wrong " << endl;
		return false;
	}
	else
	{
		elements[pos] = data;
		return true;
	}
}

template<typename T> T seqlist<T>::show_data(int pos)
{
	if(pos > length || pos < 0)
	{
		cout <<" wrong " << endl;
		return 0;
	}
	else
	{
		return elements[pos];
	}
}


template<typename T> bool seqlist<T>::delete_data(int pos)
{
	if(pos < 0 || pos > length)
	{
		cout << "wu fa shu chu " << endl;
		return false;
	}
	else
	{
		for(int i=pos; i<length; ++i)
			elements[i] = elements[i+1];
		length--;
		return true;
	}
}


int main()
{
	seqlist<int> mylist(4);
	// 如何实例化一个变量这里有用。
	mylist.insertdata(1);
	mylist.insertdata(22);
	mylist.insertdata(3);
	mylist.insertdata(32);
	mylist.delete_data(2);
	mylist.change_data(2, 110);

	for(int i=0; i < mylist.get_size(); ++i)
		cout<< "xx: " << mylist.show_data(i) << endl;


	return 0;
}



