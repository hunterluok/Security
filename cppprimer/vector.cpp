#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;


int cal_dist(vector<float> veca, vector<float> vecb, float& dists)
{
	// float sums = 0;
	if(veca.size() != vecb.size())
	{
		cout << "data shape is wrong" << endl;
		return -1;
	}
	for(int i=0; i< veca.size(); ++i)
	{
		cout << " ele a " << veca[i] << "  ele b " << vecb[i] << endl;

		dists += (veca[i] - vecb[i]) * (veca[i] - vecb[i]);
		// dists += veca[i] * vecb[i];
	}
	return 1;
}



void display(const vector<int>& inputs)
{
	for(vector<int>::const_iterator iele = inputs.begin(); iele != inputs.end(); ++iele)
	{
		cout << "ele is :" << *iele << endl;
		cout << endl;
	}
}


void display_2(const vector<int>& inputs)
{
	vector<int> :: const_iterator ieles = inputs.begin();
	while(ieles != inputs.end())
	{
		// cout << "eles is :" << *ieles << endl;
		// ++ ieles;
		size_t pos = distance(inputs.begin(),ieles);
		cout << pos << "---" << *ieles << " capacity :" << inputs.capacity() << endl;
		++ ieles;
	}
}




int main()
{
	std::vector<int> v (2, 2);

	v.push_back(5);
	v.insert(v.begin() + 1,2,666);

	std::vector<int> vs (2,888);
	v.insert(v.begin()+2, vs.begin(), vs.end());

	display_2(v);

	// std::vector<float> v_test {2.1, 3.2};
	// display_2(v_test);

	vector <int> ::const_iterator ielement;
	//auto ielement‰
	v.pop_back();
	//v.pop_back();


	vector<float> mya; // {3, 4, 1.1};
	mya.push_back(3);
	mya.push_back(4);
	mya.push_back(1);

	vector<float> myb;
	myb.push_back(3);
	myb.push_back(4);
	myb.push_back(1);

	float mydist=0.0;
	int result=0;
	// result = 
	cal_dist(mya, myb, mydist);
	// mydist = cal_distance(mya, myb);
	cout << "dist is " << mydist << endl;


	return 0;

}