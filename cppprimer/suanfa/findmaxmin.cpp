#include<iostream>

using namespace std;


void show(int data[], int lens=6)
{
	for(int i=0; i < lens; ++i)
	{
		cout << data[i] << " : ele" << endl;
	}
}



int main()
{
	int data[6] = {1, 2, 5, 3, 2, 7};

	int mins = data[0];
	int maxs = data[0];

	cout << mins << " -- " << maxs << endl;

	int i = 1;
	for(int i, j=i+1; j<6; ++i, ++j)
	// 这里 int i, j=i+1 只是初始化的过程，后面 都必须进行 ++i， ++j 否则有问题。
	{
		if(data[j] > data[i])
		{
			maxs = data[j] > maxs? data[j]: maxs;
			mins = data[i] < mins? data[i]: mins;
		}
		else
		{
			maxs = data[i] > maxs? data[i]: maxs;
			mins = data[j] < mins? data[j]: mins;
		}
	}

	show(data);
	cout << "maxs is " << maxs << " mins is " << mins << endl;
	return 0;
}