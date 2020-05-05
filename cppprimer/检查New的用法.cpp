# include <iostream>
using namespace std;

int main()
{
	try
	{
		int *page = new int[5443434232323];

		delete[] page;
	}
	catch(bad_alloc)
	{
		cout<<"memory allocation fauled."<<endl;
	}

	return 0;
}