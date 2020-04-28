#ifndef ML_H
#define ML_H

#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include "gradit.h"

using namespace std;

#define random(x) rand() % (x)

float rand_data(int length);
template<typename T> 
vector<vector<T> > add(vector<vector<T> > x, vector<vector<T> > b);
template<typename T> 
vector<vector<T> > dot(vector<vector<T> > veca, vector<vector<T> > vecb);



template<typename T>
void forword(vector<vector<T> > x, vector<vector<T> > w1, 
	vector<vector<T> > w2, vector<vector<T> > b1, vector<vector<T> > b2, 
	vector<vector<T> >& y1, vector<vector<T> >& f1,
	vector<vector<T> >& y2, vector<vector<T> >& target)
{
	y1 = add(dot(x, w1), b1);
	f1 = sigmoid(f1);
	y2 = add(dot(f1, w2), b2);
	target = sigmoid(y2);
}


template<typename T>
vector<vector<T> > sum_dim(vector<vector<T> > x)
{
	int row = x.size();
	int col = x[0].size();
	vector<vector<T> > result(row, vector<float>(1, 0.0));
	for(size_t i = 0; i < row; ++i)
	{
		T temp = 0.0;
		for(size_t j = 0; j < col; ++j)
		{
			temp += x[i][j];
		}
		temp = temp / col;
		result[i][0] = temp;
	}
	return result;
}

template<typename T>
vector<vector<T> > add_vector(vector<vector<T> > x, vector<vector<T> > b)
{
	int row = x.size();
	int col = x[0].size();
	int col_b = b[0].size();
	int row_b = b.size();
	if(row != row_b || col != col_b)
	{
		throw "wrong shape ---- ";
	}
	vector<vector<T> > result(row, vector<T>(col, 0));
	for(size_t i = 0; i < row; ++i)
	{
		for(size_t j = 0; j < col; ++j)
		{
			result[i][j] = x[i][j] + b[i][j];
		}
	}
	return result;
}

template<typename T>
vector<vector<T> > add(vector<vector<T> > x, vector<vector<T> > b)
{

	int row = x.size();
	int col = x[0].size();
	vector<vector<T> > result(row, vector<T>(col, 0));
	int col_b = b[0].size();
	if(col_b != 1)
	{
		cout << " wrong shape of b" << col_b << endl;
		throw "wrong";
	}

	for(size_t i = 0; i < row; ++i)
	{
		for(size_t j = 0; j < col; ++j)
		{
			result[i][j] = x[i][j] + b[i][0];
		}
	}
	return result;
}


template<typename T>
vector<vector<T> > cal_err(vector<vector<T> > label, vector<vector<T> >  target)
{
	int row = label.size();
	int col = label[0].size();
	vector<vector<T> > err(row, vector<T>(col, 0));

	for(size_t i = 0; i < row; ++i)
	{
		for(size_t j = 0; j < col; ++j)
		{
			err[i][j] = label[i][j] - target[i][j];
		}
	}
	return err;
}


template<typename T> 
vector<vector<T> > dot(vector<vector<T> > veca, vector<vector<T> > vecb)
{
	int row_veca = veca.size();
	int col_veca = veca[0].size();
	int row_vecb = vecb.size();
	int col_vecb = vecb[0].size();

	if(col_veca != row_vecb)
	{
		throw "data shape is wrong";
	}

	vector<vector<T> > result(row_veca, vector<T> (col_vecb, 0));
	for(int row = 0; row < row_veca; ++row)
	{
		for(int col = 0; col < col_vecb; ++ col)
		{
			T temp = 0.0;
			for(int i = 0; i < col_veca; ++i)
			{
				temp += veca[row][i] * vecb[i][col];
			}
			result[row][col] = temp;
		}
	}
	return result;
}


template<typename T>
vector<vector<T> > multiply_lambda(T lambda, vector<vector<T> >vecb)
{
	int row_b = vecb.size();
	int col_b = vecb[0].size();

	vector<vector<T> > result(row_b, vector<T> (col_b, 0));

	for(size_t i = 0; i < row_b; ++i)
	{
		for(size_t j = 0; j < col_b; ++j)
		{
			result[i][j] = lambda * vecb[i][j];
		}
	}
	return result;
}


template<typename T>
vector<vector<T> > multiply(vector<vector<T> > veca, vector<vector<T> >vecb)
{
	int row_a = veca.size();
	int col_a = veca[0].size();
	int row_b = vecb.size();
	int col_b = vecb[0].size();

	vector<vector<T> > result(row_a, vector<T> (col_a, 0));

	if(row_a != row_b || col_b != col_a)
	{
		cout << " wrong " << endl;
		return result;
	}

	for(size_t i = 0; i < row_a; ++i)
	{
		for(size_t j = 0; j < col_a; ++j)
		{
			result[i][j] = veca[i][j] * vecb[i][j];
		}
	}
	return result;
}

template<typename T>
vector<vector<T> > transpose(vector<vector<T> > v)
{
	int rowa = v.size();
	int cola = v[0].size();
	std::vector<vector<T> > nv(cola, vector<T>(rowa, 0));
	for(int row = 0; row < rowa; ++row)
	{
		for(int col = 0; col < cola; ++col)
		{
			nv[col][row] = v[row][col];
		}
	}
	return nv;

}


void init_w(vector<vector<float> >& w)
{
	int lens = w.size();
	srand((int)time(NULL));
	for(int i = 0; i < lens; ++i)
	{
		//srand((int)time(NULL));
		for(int j = 0; j < w[0].size(); ++j)
		{
			w[i][j] = rand_data(lens);
		}
	}
}

void init_b(vector<vector<float> >& b)
{
	int row = b.size();
	int col = b[0].size();
	if(col != 1)
	{
		cout << "wrong init b" << endl;
		throw "wrong init b";
	}
	srand((int)time(NULL));
	for(int i = 0; i < row; ++i)
	{
		
		b[i][0] = rand_data(row);
	}

}



float rand_data_old(int length) {
	float len = 100;
	float res = (float)(rand()) / RAND_MAX;
	return res * len + len;
}


float rand_data(int lens)
{
	// srand((int)time(NULL));
	float temp = (random(10000) / (1.00 * 10000)) * 2.0 - 1.0;
	return temp;
}


template<typename T> void showvec(T& data)
{
    //typename T::iterator iter = data.begin();
    int rows = data.size();
    int cols = data[0].size();
    for(size_t i = 0; i < rows; ++i)
    {
        for(size_t j = 0; j < cols; ++j)
        {
            cout << data[i][j] << " ";
        }
        cout << endl;
    }
    cout << " over " << endl;
}

template<typename T> void showsize(T data)
{
    //typename T::iterator iter = data.begin();
    int rows = data.size();
    int cols = data[0].size();
    cout << " row is " << rows << " cols " << cols << endl;
}

#endif