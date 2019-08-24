#include <iostream>
#include <algorithm>
#include <cmath>
#include <regex>
#include <string>
#include <vector>

using namespace std;


void readdata(int data[2][3]);


/*
unsigned long long *next_random;

unsigned long long randd(int id) {
	next_random[id] = next_random[id] * (unsigned long long)2527 + 11;
	return next_random[id];
}

int rand_max(int id, int x)
{
	int res = randd(id) % x;
	while (res < 0)
		res += x;
	return res;
}*/
const float pi = 3.14;

float rand(float min, float max) {
	return min + (max - min) * rand() / (RAND_MAX + 1.0);
}

float normal(float x, float miu, float sigma) {
	float constants = 1.0/ sqrt(2 * pi) / sigma;
	return constants * exp(-1 * (x-miu) * (x - miu ) / ( 2 * sigma * sigma));
}

float randn(float miu, float sigma, float min, float max) {
	float x, y, dScope;
	do {
		x = rand(min, max);
		y = normal(x, miu, sigma);
		dScope=rand(0.0, normal(miu, miu, sigma));
	} while (dScope > y);
	return x;
}

float *rv;

int main()
{
	cout<<"hello world" <<endl;

/*
	rv = (float*) calloc(12, sizeof(float));
	for(int i=0; i<3; i++)
	{
		for (int j=0; j<4; j++)
			rv[i*3 + j] = randn(0, 1./ 4, -6 / sqrt(4), 6 / sqrt(4));
	}

	cout << "te :" << rand() << endl; // 得到一个随机数的方法。

	for(int i=0; i<3; i++)
	{
		for (int j=0; j<4; j++)
			cout << "result : " << rv[i*3 + j] << endl;
	}
	*/


	int data[2][3];
	readdata(data);

	for(int i=0; i<2; i++)
	{
		for(int j=0; j<3; j++)
		{
			cout<< data[i][j]<<"-";
		}
		cout<< endl;
	}
	cout << "read data over" << endl;

	return 0;
}


void readdata(int data[2][3])
{
	int i, j;
	for (int i=0; i<2; i++)
	{
		for(int j=0; j<3; j++)
		{
			scanf("%d", &data[i][j]);
		}	
	}
}
