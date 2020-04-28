#include <iostream>
#include <vector>
#include "ml.h"
#include "gradit.h"
#include "util.h"

using namespace std;


float mean_error(vector<vector<float> > data)
{
	int row = data.size();
	int col = data[0].size();
	float sums = 0.0;
	for(size_t i = 0; i < row; ++i)
	{
		for(size_t j = 0; j < col; ++j)
		{
			sums += pow(data[i][j], 2);
		}
	}
	return sqrt(sums / row);
}


int main()
{
	cout << "read data" << endl;
	cout << setiosflags(ios::fixed) << setprecision(2);
	vector<vector<float> > data;
	readdata("iris.txt", data);
	// showvec(data);

	vector<vector<float> > train;
	vector<vector<float> > label;
	int size = data.size();
	for(size_t i = 0; i < size; ++i)
	{
		vector<float> temp_train;
		vector<float> temp_label;
		for(size_t j = 0; j < data[0].size(); ++j)
		{
			if(j != 3)
			{
				temp_train.push_back(data[i][j]);
			}
			else
			{
				temp_label.push_back(data[i][j]);
		
			}
		}
		train.push_back(temp_train);
		label.push_back(temp_label);
	}



	cout << "init data" << endl;
	int mid_hidden = 5;
	int n_feature = train[0].size();
	int batch_size = train.size();
	vector<vector<float> > w1(n_feature, vector<float>(mid_hidden, 0.0));
	vector<vector<float> > w2(mid_hidden, vector<float>(1, 0.0));
	vector<vector<float> > b1(batch_size, vector<float>(1, 0.0));
	vector<vector<float> > b2(batch_size, vector<float>(1, 0.0));
	init_w(w1);
	init_w(w2);
	init_b(b1);
	init_b(b2);

	cout << " forword process " << endl;
	vector<vector<float> > y1(batch_size, vector<float>(mid_hidden, 0.0));
	vector<vector<float> > f1(batch_size, vector<float>(mid_hidden, 0.0));
	vector<vector<float> > y2(batch_size, vector<float>(1, 0.0));
	vector<vector<float> > target(batch_size, vector<float>(1, 0.0));
	// forword(train, w1, w2, b1, b2, y1, f1, y2, target);
	// showvec(target);
	cout << " cal_err " << endl;
	vector<vector<float> > error(batch_size, vector<float>(1, 0.0));
	// error = cal_err(label, target);
	// showvec(error);

	int iter = 0;
	float lambda = 0.00001;


	showvec(w1);
	while(iter < 1000)
	{
		forword(train, w1, w2, b1, b2, y1, f1, y2, target);
		error = cal_err(label, target);

		++iter;
		vector<vector<float> > f1_t = transpose(f1);
		vector<vector<float> > w2_t = transpose(w2);
		vector<vector<float> > train_t = transpose(train);
		vector<vector<float> >  mid = multiply(dot(multiply(error, y2), w2_t), sigmoid_gradient(f1));

		w1 = add_vector(w1, multiply_lambda(lambda, dot(train_t, mid)));
		b1 = add_vector(b1, multiply_lambda(lambda, sum_dim(mid)));
		w2 = add_vector(w2, multiply_lambda(lambda, dot(f1_t, multiply(error, sigmoid_gradient(target)))));
		b2 = add_vector(b2, multiply_lambda(lambda, multiply(error, sigmoid_gradient(target))));
		
		if(iter % 100 == 0)
		{
			cout << " error is " << mean_error(error) << " at iter " << iter << endl;
			showvec(w1);
		}
	}

	showvec(target);
	showvec(label);

	return 0;
}















