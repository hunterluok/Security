#include <iostream>
using namespace std;


bool find_dup(int data [], int lens, int* target)
{
	if(data==nullptr || lens <= 0)
	{
		cout << "wrong" << endl;
		return false;
	}


	for(int i = 0; i < lens; ++i)
	{
		while(data[i] != i)
		{
			if(data[i] == data[data[i]])
			{
				cout << data[i] << "duplicates " << endl;
				*target = data[i];
				return true;
			}
			int temp = data[i];
			data[i] = data[temp];
			data[temp] = temp;
		}
	}

	return false;
}



int main()
{
	int data[7] = {1, 3, 0, 4, 2, 2};
	int lens = 7;
	int target = -1;
	bool result = find_dup(data, lens, &target);
	cout << " result is " << target << " ---" << endl;
	return 0;
}