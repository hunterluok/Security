#ifndef TT_H
#define TT_H

#include<vector>
#include<iostream>

using namespace std;


void showdata(vector< vector<int> > x)
{
	for(int i=0; i<x.size(); i++)
	{
		for(int j=0; j<x[i].size(); j++)
		{
			cout<< x[i][j]<< " ";
		}
	cout << endl;
	}
}


#endif