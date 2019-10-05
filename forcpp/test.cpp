#include "util.h"
#include "mybayes.h"
#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>


using namespace std;


int main()
{
	cout << setiosflags(ios::fixed) << setprecision(2);
	cout << "=== read data==="  << endl;
	vector<vector<float> > data;
	readdata("iris.txt", data);
	showdata(data[0]);
	cout << "===" << data.size() << "==="  << endl;

	cout << "=== read label==="  << endl;
	vector<int> label;
	read_label("label.txt", label);
	showdata(label);
	cout << "===" << label.size() << "==="  << endl;


	mybaye model(1);
	// map<int, vector<float> > result;
	// result = 
	model.fit(data, label);
	// model.fit(data, label, resu);

	map<int, vector<float> > result;
	result = model.get_result();

	map<int, vector<float> >::iterator iter=result.begin();
	while(iter != result.end())
	{
		cout << "key is " << iter -> first << endl;
		cout << "likelihood vector ";
		showdata(iter->second);
		cout << "---" << endl;
		iter++;
	}

	printf("*************************");

	int index = 101;
	// int pred = model.predict_line(data[index]);
	// cout << " pred is " << pred << " data is " << endl;
	// cout << " real label is " << label[index] << endl;
	vector<int> preds = model.predict(data);
	//  
	showdata(preds);

	float acc = model.acc_score(preds, label);
	cout << " acc score is " << acc << endl;

	return 0;
}