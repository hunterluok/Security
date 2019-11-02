#include <iostream>
#include <vector>

using namespace std;


int cal_max(const vector<int> data)
{
	int lens = data.size();
	if(lens < 2)
	{
		cout << "wrong " << endl;
		return 0;
	}

	int mins = data[0];
	int maxfit = data[1] - data[0];
	// 注意这里的思想
	for(int i = 2; i < lens; ++i)
	{
		if(data[i-1] < mins)
		{
			mins = data[i-1];
		}
		int temp = data[i] - mins;
		if(temp > maxfit)
		{
			maxfit = temp;
		}
	}
	return maxfit;
}

int main()
{
	int a[8] = {9, 11,8, 5, 7,12, 16, 14};
	std::vector<int> v;
	for(int i=0; i < 8; ++i)
	{
		v.push_back(a[i]);
	}

	int result = cal_max(v);
	cout << "best is " << result << endl;
	return 0;
}