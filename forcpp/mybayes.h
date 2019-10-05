#include "util.h"

#include <iostream>
#include <map>
#include <set>
#include <cmath>
// #include <iomanip>


using namespace std;

class mybaye
{
private:
	int a;
	map<int, vector<float> > myresult;

public:
	mybaye()
	{
		a = 1;
		// myresult = NULL;
		cout << "mo ren init" << endl;
	}

	mybaye(int inta)
	{
		a = inta;
		// myresult = NULL;
	}

	int get_a()
	{
		return a;
	}

	map<int, vector<float> > get_result()
	{
		return myresult;
	}

	vector<vector<float> > split_data(vector<vector<float> > data, vector<int> label, int sub_label);
	// 获取  概率.
	vector<float> get_like(vector<vector<float> > data); 
	map<int, float> get_pri(vector<int> label, vector<int>& keys);
	// void fit (vector<vector<int> > data, vector<int> label, map<int, vector<float> >& result);
	map<int, vector<float> > fit (vector<vector<float> > data, vector<int> label);
	// int predict_line(vector<int> line, map<int, vector<float> >& result);
	int predict_line(vector<float> line);
	float multiply(vector<float> veca, vector<float> vecb);
	vector<int> predict(vector<vector<float> > testdata);
	float acc_score(vector<int> veca, vector<int> vecb);
};


// void mybaye::fit(vector<vector<int> > data, vector<int> label, map<int, vector<float> >& result)
map<int, vector<float> >  mybaye::fit(vector<vector<float> > data, vector<int> label)
{
	map<int, vector<float> > result;

	vector<int> keys;
	map<int, float> pri = get_pri(label, keys);

	for(int i=0; i < keys.size(); ++i)
	{
		int target_label = keys[i];
		float temp_pri = pri[target_label];

		vector<vector<float> > temp_subdata;
		vector<float> temp_likelihood;
		temp_subdata = split_data(data, label, target_label);
		// 获取特定数据集的似然函数。
		temp_likelihood = get_like(temp_subdata);
		temp_likelihood.push_back(temp_pri);
		showdata(temp_likelihood);
		result.insert(make_pair(target_label, temp_likelihood));
	}
	this->myresult = result;
	// showmap(result);
	return result;
}


int mybaye::predict_line(vector<float> line) //, map<int, vector<float> >& result);
{
	int line_pred = -1;
	float maxsums = -10000;

	map<int, vector<float> > result = this -> myresult;
	// map<int, vector<float> > result = myresult;
	map<int, vector<float> >::iterator iter = result.begin();
	while(iter != result.end())
	{
		int key = iter -> first;
		float sums = multiply(line, iter -> second);
		if(sums > maxsums)
		{
			maxsums = sums;
			line_pred = key;
		}
		iter ++;
	}
	return line_pred;
}

nnm
float mybaye::multiply(vector<float> veca, vector<float> vecb)
{

	int vsize = veca.size();
	// 最后一个 是 pri
	float sums = log(vecb[vsize]);
	for(int i=0; i < vsize; ++i)
	{
		sums += veca[i] * log(vecb[i]);
	}
	return sums;
}


vector<int> mybaye::predict(vector<vector<float> > testdata)
{
	vector<int> pred;
	for(int i = 0; i < testdata.size(); ++i)
	{
		vector<float> temp_line = testdata[i];
		int temp_pred = predict_line(temp_line);
		pred.push_back(temp_pred);
	}
	return pred;
}

float mybaye::acc_score(vector<int> veca, vector<int> vecb)
{
	int sums = 0;
	int lens = veca.size();
	for(int i = 0; i < lens; ++i)
	{
		if(veca[i] == vecb[i])
			sums += 1;
	}
	return  sums / (lens * 1.0);
}


vector<vector<float> > mybaye::split_data(vector<vector<float> > data, vector<int> label, int sub_label)
{
	vector<vector<float> > sub_data;
	int lens = data.size();

	for(int index = 0; index < lens; ++index)
	{
		if(label[index] == sub_label)
		{
			sub_data.push_back(data[index]);
		}
	}
	return sub_data;
}

// void mybaye::sums(vector<vector<int> > data, vector<float>& sum_row, float& sums_all)
vector<float> mybaye::get_like(vector<vector<float> > data)
{
	int rows = data.size();
	int cols = data[0].size();
	vector<float> likelihood(cols, 0.0);

	float sums_all = 0.0;
	vector<float>  sum_row(cols, 0.0);

	for(int i=0; i < rows; ++i)
	{
		for(int j=0; j< cols; ++j)
		{
			sum_row[j] += data[i][j];
			sums_all += data[i][j];
		}
	}
	for(int j = 0; j < cols; ++j)
	{
		likelihood[j] = (sum_row[j] + this->a) / (sums_all + (this->a) * rows);
	}
	// cout << " likelihood vector  " << endl;
	// showdata(likelihood);
	// cout << " ***** " << endl;
	return likelihood;
}


map<int, float> mybaye::get_pri(vector<int> label, vector<int>& keys)
{
	int lens = label.size();
	map<int, int> mymap;
	for(int i=0; i < lens; ++i)
	{
		mymap[label[i]]++;
	}
	map<int, float> pri;
	for(map<int, int>::iterator iter=mymap.begin(); iter != mymap.end(); ++iter)
	{
		int key = iter -> first;
		float value = (iter -> second) / (lens * 1.0);
		pri[key] = value;
		keys.push_back(key);
	}
	return pri;
}