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
		this->length = 0;
		elements = new T[maxsize];
	}
	~mylists()
	{
		delete [] elements;
	}

    bool append(T value);
//    bool find(T value);
//    bool omit(T value);
    bool show();

private:
	int maxsize;
	int length;
	T *elements;
	
};


template<typename T> bool mylists<T>::show()
{
	//mylists<T>::iterator it=elements.begin();
	for(size_t i = 0; i < length; ++i)
	{
		cout << "ele is : " << elements[i] << endl;
 	}
 	return true;
};


template<typename T> bool mylists<T>::append(T value)
{
    if(length < maxsize)
    {
        elements[length] = value;
        length++;
        return true;
    }
    else
    {
        cout << "lists is full" << endl;
        return false;
    }

};


int main()
{
    mylists<int> my(4);
    my.append(2);
    my.append(11);
    my.append(33);
    my.show();


}