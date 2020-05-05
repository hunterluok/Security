#include "util.h"
#include "kmclass.h"

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;


int main()
{
	// kmeans *myk = new kmeans(2);
	// cout << myk.get_k() << "\n" << endl;
	// delete myl;
	cout << setiosflags(ios::fixed) << setprecision(2);
	
	vector<vector<float> > data;
	readdata("iris.txt", data);
	cout << "===" << data.size() << "===" << endl;

	kmeans myk(3, 10, 1.1);
	vector<vector<float> > result;
	result = myk.fit(data);

	writedata("resultt.txt", result);
	return -1;
}