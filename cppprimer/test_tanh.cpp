
#include <iostream>
#include <cmath>
using  namespace std;

float calctanh(float con)
{
	if (con>20) return 1.0;
	if (con<-20) return -1.0;

	float sinhx = exp(con)-exp(-con);
	float coshn = exp(con)+exp(-con);

	return sinhx/coshn;
}

float tanhgrad(float con)
{
	float res = calctanh(con);
	float tanhd = 1- res*res;
	return tanhd;
}

float sigmoid(float con)
{
	if (con>20) return 1.0;
	if (con<-20) return 0.0;
	float temp = 1 + exp(-con);
	return 1/temp;
}


int gerRand(int l,int r)
{
	int len = r-1;
	int res = rand()*rand() % len;
	if (res<0)
		res += len;
	return res+1;
}


int main()
{
	float a = -0.0;
	float s = tanhgrad(a);
	cout<<s<<endl;

	float ras = rand()*rand() % 100;

	cout<< ras<<endl;
	return 0;
}