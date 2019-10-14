#include <iostream>

using namespace std;

class SortAlgo
{

private:
	int* a[];


public:
	SortAlgo()
	{
		cout << "hehe" << endl;
	}

	// SortAlgo(int* data[])
	// {
	// 	a = data;
	// }
	~SortAlgo()
	{
		delete [] *a;
	}
	
	void insertsort(int lens, int data[]);

};

void SortAlgo::insertsort(int lens, int data[])
{
	if(lens < 2)
	{
		cout << "wrong" << endl;
	}

	for(int i = 1; i < lens; ++i)
	{
		int key = data[i];
		int index = i - 1;
		while( index > -1 && key < data[index])
		{
			data[index + 1] = data[index];
			index--;
		}
		data[++index] = key;
	}
	// this->a = &data;
}


int main()
{
	int a[] = {4, 3, 2, 1};

	SortAlgo test = SortAlgo();

	test.insertsort(4, a);
	for(int i = 0; i < 4; ++i)
		{
			cout << "i is " << a[i] << endl;
		}

	return 1;
}