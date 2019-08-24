#ifndef KMCLASS_H
#define KMCLASS_H

#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>
#include <iomanip>

using namespace std;

class kmeans
{
private:
	int k;
	int maxiter;
	float diff_loss;

public:
	// 构造函数
	kmeans(int nk, int nmaxiter, float ndiff_loss):diff_loss(ndiff_loss)
	{
		k = nk;
		maxiter = nmaxiter;
	}

	vector<vector<float> > fit(vector<vector<float> > data)
	{
		int m, n;
		m = data.size();
		n = data[0].size();

		vector<int> vecc;
		vecc = centor(m, k);
		// 得到初始化的中心点。
		vector<vector<float> > mycentor;
		for(int i=0; i<vecc.size(); ++i)
		{
			mycentor.push_back(data[vecc[i]]);
		}
		cout << "init_center is : \n";
		//showvector(mycentor);
		cout << endl;

		float init_loss = -10000.0;
		float total_loss = 0.0;
		// 初始化一个2维的vector 存放 距离和 标签。
		vector<vector<float> > labels(m, vector<float>(k, 0));
		int counts = 0;
		while(total_loss - init_loss > diff_loss)
		{	
			counts ++ ;
			if(counts > maxiter)
				break;
			init_loss = total_loss;
			for(int i=0; i<m; ++i)
			{
				int label = 0;
				float dist = 100000;
				for(int j=0; j<k; ++j)
				{
					float mydist;
					cal_dist(data[i], mycentor[j], mydist);
					if(mydist < dist)
					{
						dist = mydist;
						label = j;
					}
				}
				// 更新聚类标签， 更新 距离。
				labels[i][0] = label;
				labels[i][1] = dist;
			}

			for(int j=0; j<k; ++j)
			{
				vector<vector<float> > subdata;
				for(int index=0; index<m; ++index)
					if(labels[index][0] == j)
						subdata.push_back(data[index]);
				// 更新 新的聚类中心。
				vector<float> sub_mean;
				sub_mean = get_mean(subdata);
				mycentor[j] = sub_mean;
			}
			// 更新 loss;
			total_loss = get_totalloss(labels);
			cout << "iter " << counts << " total_loss " << total_loss << endl;
		}
		return labels;
	}

	void cal_dist(vector<float> veca, vector<float> vecb, float& distance);
	int find_value(vector<int> v, int ele);
	vector<int>  centor(int lens, int k);
	vector<float> get_mean(vector<vector<float> > data);
	float get_totalloss(vector<vector<float> > data);
};


void kmeans::cal_dist(vector<float> veca, vector<float> vecb, float& distance)
{
	for(int i=0; i < veca.size(); ++i)
		distance += (veca[i] - vecb[i]) * (veca[i] - vecb[i]);
	distance = sqrt(distance);
};


int kmeans::find_value(vector<int> v, int ele)
{
	for(vector<int>::iterator it = v.begin(); it !=v.end(); ++it)
	{
		if(*it == ele)
			return 1;
		else
			return -1;
	}
	return -1;
}

vector<int> kmeans::centor(int lens, int k)
{
	std::vector<int> v;
	int count = 0;
	srand(time(0));
	while(count < k)
	{
		int tempindex = rand() % lens;
		if(find_value(v, tempindex) != 1)
		{
			v.push_back(tempindex);
			count ++;
		}
	}
	return v;
}


vector<float> kmeans::get_mean(vector<vector<float> > data)
{
	vector<float> new_vector;
	for(int i=0; i<data[0].size(); ++i)
	{
		float temp_value = 0.;
		for(int j=0; j<data.size(); ++j)
		{
			temp_value += data[j][i];
		}
		temp_value = temp_value / (0.00001 + data.size());
		new_vector.push_back(temp_value);
	}
	return new_vector;
}

float kmeans::get_totalloss(vector<vector<float> > data)
{
	float loss=0.;
	// vector<vector<float> >::iterator it=data.begin();
	for(int i=0; i<data.size(); ++i)
	{
		loss += data[i][1];
		// cout << " local loss is " << data[i][1] << endl;
	}
	return loss;
}


#endif