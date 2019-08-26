#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool find_value(vector<vector<int> > data, int value);

void create_vector(vector<vector<int> >& data)
{
	ifstream myfile("test.txt", ios::in);
	if(!myfile)
	{
		cout << "wrong" << endl;
	}

	int a, b, c, d;
	while(myfile >> a >> b >> c >> d)
	{
		std::vector<int> v;
		v.push_back(a);
		v.push_back(b);
		v.push_back(c);
		v.push_back(d);
		data.push_back(v);	
	}
	myfile.close();
}


void show_vector(vector<vector<int> > data)
{
	for(int i = 0; i < data.size(); ++i)
	{
		for(int j=0; j < data[0].size(); ++j)
		{
			cout << data[i][j] << " ";
		}
		cout << endl;
	}
}


bool find_value(std::vector<std::vector<int> > data, int value)
{
	int rows = data.size();
	int cols = data[0].size();
	//for(int col=cols-1; col>-1; --col)
	int row = 0;
	int col = cols - 1;
	int count = 0;

	while(row < rows && col >=0)
	{
		if(data[row][col] == value)
		{
			
			cout << "find it, use " <<  count << endl;
			return true;
		}
		else if(data[row][col] > value)
		{
			count ++;
			col --;
		}
		else
		{
			count ++;
			row ++;
		}
	}
	cout << "not find it" << endl;
	return false;
}


int tests(vector<vector<int> > data, int target)
{
	bool label = find_value(data, target);
	if(label)
	{
		cout << " ok" << endl;
	}
	else
	{
		cout << "no" << endl;
	}
	return -1;
}


int main()
{
	vector<vector<int> > data;
	create_vector(data);
	show_vector(data);
	//find_value(data, 7);

	tests(data, 1);
	tests(data, 7);
	tests(data, 113);

	return -1;

}