#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
// #include <assert.h>
// #include <exception>
using namespace std;

#define indef_min -32767;

template<typename T> T conv(vector<vector<T> > data, vector<vector<T> >kernel, 
int row, int col, int row_filter, int col_filter);

template<typename T>
T pool(vector<vector<T> > data, int row, int col,int row_filter, int col_filter, string flag);


vector<vector<float> > readtarget()
{
    // string path = argv[1];
    // cout << " " << argv[0]  << " " << argc << endl;
    string path = "t.txt";
    ifstream myfile(path, ios::in);

    if (!myfile)
    {
        cout << "file is bad" << endl;
        throw "file is wrong";
    }

    vector<vector<float> > newdata;
    string line;
    while(getline(myfile, line))
    {
        istringstream nline(line);
        vector<float> temp_line;
        string s;
        while(nline >> s)
        {
            float temp = 0.0;
            stringstream ano;
            ano << s;
            ano >> temp;

            temp_line.push_back(temp);
        }
        newdata.push_back(temp_line);
    }
    return newdata;
}


template<typename T>
vector<vector<T> > cal_conv(vector<vector<T> > data, vector<vector<T> >kernel)
{
	int row_data = data.size();
	int col_data = data[0].size();
	int row_kenel = kernel.size();
	int col_kenel = kernel[0].size();

	if(row_data <= row_kenel || col_data <= col_kenel)
	{
		return data;
	}

	int out_row = row_data - row_kenel + 1;
	int out_col = col_data - col_kenel + 1;

	vector<std::vector<T > > result(out_row, vector<T> (out_col, 0));
	for(size_t row = 0; row < out_row; ++row)
	{
		for(size_t col = 0; col < out_col; ++col)
			result[row][col] = conv(data, kernel, row, col, row_kenel, col_kenel);
	}
	return result;
}


template<typename T>
T conv(vector<vector<T> > data, vector<vector<T> >kernel, 
int row, int col, int row_filter, int col_filter)
{
	
	T sums = 0;
	for(size_t i=row; i < row + row_filter; ++i)
	{
		for(size_t j=col; j < col + col_filter; ++j)
			sums += data[i][j] * kernel[i-row][j-col];
	}
	return sums;
}


template<typename T>
vector<vector<int> > cal_pool(vector<vector<T> > data, vector<T>kernel, string flag="max")
{
	int row_data = data.size();
	int col_data = data[0].size();
	T row_kenel = 2;
	T col_kenel = 2;
	
	if(kernel.size() == 2)
	{
		T row_kenel = kernel[0];
		T col_kenel = kernel[1];
	}
	else if(kernel.size() == 1)
	{
		T row_kenel = kernel[0];
		T col_kenel = kernel[0];
		cout << "kernel size is " << kernel.size()<< " " << row_kenel << " " << col_kenel << endl;
	}
	else
	{
		cout << " kernel size must be 1 or 2" << endl;
		return data;
	}

	T out_row = row_data - row_kenel + 1;
	T out_col = col_data - col_kenel + 1;

	cout << "row_data is " << row_data << " out_row is " << out_row << endl;
	cout << "row_kenel is " << row_kenel << " col_kenel is " << col_kenel << endl;
	cout << "out_row is " << out_row << " out_col is " << out_col << endl;

	vector<std::vector<T > > result(out_row, vector<T> (out_col, 0));
	for(size_t row = 0; row < out_row; ++row)
	{
		for(size_t col = 0; col < out_col; ++col)
			result[row][col] = pool(data, row, col, row_kenel, col_kenel, flag);
	}
	return result;
}

template<typename T>
T pool(vector<vector<T> > data, int row, int col,int row_filter, int col_filter, string flag)
{
	T result = indef_min;
	if(flag == "max")
	{
		for(size_t i = row; i < row + row_filter; ++i)
		{
			for(size_t j = col; j < col + col_filter; ++j)
				if(result < data[i][j])
				{
					result = data[i][j];
				}
		}
		return result;
	}
	else if(flag == "mean")
	{
		T result = 0;
		for(size_t i = row; i < row + row_filter; ++i)
		{
			for(size_t j = col; j < col + col_filter; ++j)
			{
					result += data[i][j];
			}
		}
		result = result / (row_filter * col_filter);
		return result;
	}
	else
	{
		cout << "pool is wrong" << endl;
		return -1;
	}
	
}
