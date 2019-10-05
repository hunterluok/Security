#include <iostream> 
#include <list>
#include <forward_list>
#include <vector>

using namespace std;

template<typename T>
void showdata(const T& data)
{
	typename T::const_iterator iter = data.begin();
	for(; iter!= data.end(); ++iter)
	{
		cout  << ' ' << *iter;
	}
	cout << endl;
}

bool sortdata(const int& a, const int& b)
{
	return a < b;
	// return a > b;
}


int main()
{
	list<int> my;
	// my.reserve(6);
	my.push_back(2);
	my.push_front(1);

	list<int> my2(6, 5);
	showdata(my2);

	list<int> my3(my.begin(), my.end());
	showdata(my3);
	cout << "mys size is " << my3.size() << endl;

	list<int>::iterator res = my.insert(++my.begin(), 4);
	showdata(my);
	cout << "iter value is " << *res << endl;


	my.insert(++my.begin(), my2.begin(), my2.end());
	showdata(my);

	my.sort(sortdata);
	showdata(my);
	cout << "new data is " << *res << endl;

	// 	抹除 迭代器。
	// my.erase(res);
	// showdata(my);

	// 类似于 python 列表一样删除数据的
	my.remove(4);
	showdata(my);

	// 对 vector 进行 重新赋予空间
	// std::vector<int> v;
	// v.push_back(2);
	// v.push_back(4);
	// v.push_back(11);
	// v.reserve(4);
	// // my.reverse(6);dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddxx
	// v.push_back(2);
	// for(size_t i=0; i < 4; ++i)
	// {
	// 	v.push_back(i);
	// }
	// cout << "size " << v.size() << "capicaty is " << v.capacity() << endl;
	// showdata(my);
	return 0;
}