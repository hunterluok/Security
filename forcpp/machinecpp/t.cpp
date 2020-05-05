#include <iostream>
#include <cmath>

using namespace std;

#define random(x) rand() % (x)

float getRandU(float l, float r) {
	float len = r - l;
	srand((int)time(NULL));
	float res = (float)(rand()) / RAND_MAX;
	return res * len + l;
}

float rand_data_old(int length)
{
	srand((int)time(NULL));
	float temp = (random(length) / (1.00 * length)) * 2.0 - 1.0;
	return temp;
}


int main()
{
	cout<<rand_data_old(1000) << endl;
	return 0;
}