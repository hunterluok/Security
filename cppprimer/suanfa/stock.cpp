#include <iostream>

using namespace std;


int find_max(const int* data, unsigned int length)
{
	if(data == nullptr && length < 2)
	{
		return 0;
	}

	int mins = data[0];
	int maxvalue = data[1] - mins;
	for(int i=2; i<length; ++i)
	{
		if(mins < data[i-1])
		{
			mins = data[i-1];
		}

		if(maxvalue < data[i] - mins)
		{
			maxvalue = data[i] - mins;
		}
	}
	return maxvalue;
}


int main()
{
	// int data[5] = {9, 11, 8, 5, 7};
	// int data[6] = {5 , 4, 3, 2, 1};
	int data[] = {1, 2, 3, 4, 5};

	int result = find_max(data, 5);
	cout << "result is " << result << endl;
	cout << "test is " << sizeof(data) << sizeof(int) << endl;
	return 0;
}