#include <string>
#include <map>
#include <iostream>
#include <iterator>
using namespace std;

/*
int main()
{
	string key;
	string value;
	map<string, int> word2count;
	map<string, int>:: iterator it;
	while(cin >> key)
	{
		cin >> value;
		it = word2count.find(key);
		if(it != word2count.end()){
			(it->second) ++;
		}else
	{
		word2count.insert(make_pair(key, 1));
	}
}
	for(it = word2count.begin(); it!= word2count.end(); ++it)
	{			
		cout << it->first << "\t" << it->second << endl;
}
}
*/
template<typename T>
void display(const T& inputs)
{
	for (typename T::const_iterator iele = inputs.begin(); iele != inputs.end(); ++iele)
	{
		cout << "ielement : " << *iele << endl;
	}
} 


template<typename T>
int dp(const T& inputs)
{
	int new_n = static_cast <int> (inputs);
	return  new_n * 2;
} 


template<typename T1, typename T2>
void dp(const T1& input1, const T2& input2)
{
	int new_n = static_cast <int> (input2);
	// return  new_n * 3;
	// cout << input1 << "\t" << new_n * 3 << endl;
	cout << input1 << "\t" << new_n << endl;
}



int main()
{
	// string cur_key = '0', last_key = '0', value = '0'; char 不能写成 string
	string cur_key, last_key, value;
	cin >> cur_key >> value;

	last_key = cur_key;
	int n=1;
	while(cin >> cur_key)
	{
		cin >> value;
		if (last_key != cur_key)
		{
			cout << last_key << "\t" << n << endl;
			// cout << last_key << "\t" << displays(n) << endl;
			dp(last_key, n);
			last_key = cur_key;
			n = 1;
		}
		else
		{
			n++;
		}
	}
	cout << last_key << "\t" << n << endl;
	dp(last_key, n);
	return 0;
}