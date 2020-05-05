#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <ctime>
#include <iomanip>

using namespace std;
int find_value(vector<int> v, int ele);


void cal_dist(vector<float> veca, vector<float> vecb, float& distance)
{
	for(int i=0; i < veca.size(); ++i)
		distance += (veca[i] - vecb[i]) * (veca[i] - vecb[i]);
	distance = sqrt(distance);
}

int find_value(vector<int> v, int ele)
{
	for(vector<int>::iterator it = v.begin(); it !=v.end(); ++it)
	{
		if(*it == ele)
		{
			return 1;
		}
		else
		{
			return -1;
		}
	}
	return -1;
}

vector<int> centor(int lens, int k)
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
/*
template<typename T> void showdata(vector<T> data)
{
	vector<T>::iterator it = data.begin();
	while(it !=data.end())
	{
		cout << "ele is " << *it << endl;
	}
}*/
void showdata(vector<int> data)
{
	vector<int>::iterator it = data.begin();
	while(it != data.end())
	{
		cout << "ele is " << *it << endl;
		++it;
	}
}


bool readdata(string path,  vector<vector<float> >& data)
{
	ifstream myfile(path, ios::in);
	if(!myfile)
    {
        cout << "打开文件出错" << endl;
        return false;
    }

    // 如何 一行行的 读入 vector 方便进行计算。
	float index, a , b ,c, d;
	while(myfile >> index >> a >> b >> c >> d)
	{
		vector<float> temp_vec;
		temp_vec.push_back(a);
		temp_vec.push_back(b);
		temp_vec.push_back(c);
		temp_vec.push_back(d);
		data.push_back(temp_vec);
	}
	myfile.close();
	return true;
}

bool writedata(string path,  vector<vector<float> > data)
{
	ofstream myfile(path, ios::out);
	if(!myfile)
    {
        cout << "打开文件出错" << endl;
        return false;
    }

	for(int i=0; i<data.size(); ++i)
	{
		// 如何一行行的读入数据，
		myfile << data[i][0] << " " << data[i][1] << endl;
	}
	myfile.close();
	return true;
}


void showvector(vector<vector<float> > data)
{
	for(int i=0; i<data.size(); ++i)
	{
		for(int j=0; j<data[i].size(); ++j)
			cout << data[i][j] << " ";
		cout << endl;
	}
}


vector<float> get_mean(vector<vector<float> > data)
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

float get_totalloss(vector<vector<float> > data)
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


int main()
{
	cout << setiosflags(ios::fixed) << setprecision(2);

	vector<vector<float> > data;
	readdata("iris.txt", data);
	cout << "===" << data.size() << endl;

	int maxiter = 10;
	int k = 3;
	int m, n;
	float diff_loss = 1;
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
	showvector(mycentor);
	cout << endl;


	float init_loss = -10000.0;
	float total_loss = 0.0;
	// 初始化一个2维的vector 存放 距离和 标签。
	vector<vector<float> > labels(m, vector<float>(k, 0));
	int count = 0;
	while(total_loss - init_loss > diff_loss)
	{	
		count ++ ;
		if(count > maxiter)
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
		cout << "iter " << count << " total_loss " << total_loss << endl;
	}

	cout << "last_center is : \n";
	showvector(mycentor);
	cout << endl;

	cout << "total loss is " << total_loss << endl;
	cout << "total iter is " << count << endl;
	// 将数据的标记 存储在特定的文件中。
	writedata("resutl.txt", labels);
	return -1;
}