#include <iostream>
#include <map>
#include <string>
#include <set>
#include <vector>
using namespace std;


int main()
{
	map<string, string> words;

	//string word;
	// while(cin >> word)
	//{
	//	words[word]++;
	//}

	words["s"] = "a";
	words["xx"] = "b";
	words["sds"] = "c";

	map<string, string>::iterator it = words.begin();

	for( ;it != words.end(); it++)
	{
		cout << "key: " << it->first << " value: " << it->second << endl;
	}

/*
	int count = 0;
	map<string, int>::iterator its;
	its = words.find("sds");
	if( its != words.end())
	{
		count = its -> second;
	}
	cout << "count is :" << count << endl;
	int counts = 0;
	// string search_word("sds");
	if(words.count("sds"))
		counts = words["sds"];

	cout << "counts is :" << counts << endl;
*/
	int a[6] = {1, 3, 4, 2, 1, 10};

	map<int, int> mycount;

	for(int i=0; i<6; i++)
	{
		/*
		
		if(mycount.contain(a[i]))
			mycount[a[i]]+=1
		else
			mycount[a[i]] = 1
			*/
		mycount[a[i]]++;
	}

	if(mycount[1100])
	// 不存在的 key 会被 插入 其value 为0.
  	{
  		cout << "ok" << endl;
  	}


	for(map<int, int>::iterator it=mycount.begin(); it!=mycount.end(); it++)
	{
		cout<< "key is " << it -> first << "value is " << it -> second << endl;
  	}


  	// 利用map 的 count 函数进行查找。
  	int ps(1);
  	if(mycount.count(ps))
  		cout << mycount[ps] << "----" << endl;

  	// 利用 finnd查找
  	map<int, int>::iterator mit;
  	mit = mycount.find(1);
  	if(mit !=mycount.end())
  		cout << "--" << mit->second << endl;

	vector<int> vs(a, a+6);
	set<int> mset(vs.begin(), vs.end());
	set<int>::iterator txx = mset.begin();
	for(; txx!=mset.end(); txx++)
	{
		cout << "myset is " << *txx << endl;
	}
	
	set<string> my_set;
	my_set.insert("s");
	my_set.insert("sss");
	set<string>::iterator itx = my_set.begin();
	for(;itx!= my_set.end(); itx ++)
	{
		// 注意这里与其他地方的区别。
		cout << "re: " << *itx << endl;
	}
	return 0;
}