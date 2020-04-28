#ifndef GRADIT_H
#define GRADIT_H

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
void sigmoid_local(vector<vector<float> >& data);


void sigmoid_local(vector<vector<float> >& data)
{
	int row = data.size();
	int col = data[0].size();
	for(int i = 0; i < row; ++i)
	{
		for(int j = 0; j < col; ++j)
		{
			data[i][j] = 1 / ( 1 + exp(-1.0 * data[i][j]));
		}
	}
}


vector<vector<float> > sigmoid(vector<vector<float> > data)
{
	int row = data.size();
	int col = data[0].size();
	vector<vector<float> > result(row, vector<float>(col, 0));
	for(int i = 0; i < row; ++i)
	{
		for(int j = 0; j < col; ++j)
		{
			result[i][j] = 1 / ( 1 + exp(-1.0 * data[i][j]));
		}
	}
	return result;
}


 vector<vector<float> >  sigmoid_gradient(vector<vector<float> > data)
{
	// sigmoid_local(data);
	int row = data.size();
	int col = data[0].size();
	vector<vector<float> > result(row, vector<float>(col, 0));
	for(int i = 0; i < data.size(); ++i)
	{
		for(int j = 0; j < data[0].size(); ++j)
		{
			result[i][j] = (1 - data[i][j]) * data[i][j];
		}
	}
	return result;
}

#endif