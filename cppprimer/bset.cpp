#include<iostream>
#include <bitset>
#include <vector>
using namespace std;

int main()
{
	bitset <8> a("00011000");
	bitset <8> b("11111111");

	bitset <8> c(a | b); // ^ & | ~ 取反 四种做法。

	a >>=(2);
	b[2] = 0;

	a.set();  // 设置为1 全部。
	// a.reset(); // 重置为 0
	b.flip();
	size_t n = b.size();
	size_t n_1 = b.count();

	a.set(2, 1);
	a.reset(3); // 将第三位 设置为 0. 


	// 两个对象相加 得到的结果：
	bitset<12>  f = a.to_ulong() + b.to_ulong();

	// a <<=(1);
	// cin >> a; // 输入一个数据。
	cout << "a : " << a << endl;
	cout << "b : " << b << endl;
	cout << "c : " << c << endl;
	cout << "n : " << n << "n_1: " << n_1 << endl ; 
	cout << "f : " << f << endl;

	cout << "------------" << endl;

	vector<bool> v (14);  // 实际上 为
	v.push_back(true);  // push_back 为在末尾 追加数据， 所以是 初始化化的个数 + 3.
	v.push_back(false);
	v.push_back(true);
	// v.push_back(false);

	for(size_t n=0; n< v.size(); ++n)
		cout << "n is " << n << "result :" << v[n] << "---" << endl;
	// cout << "v : " << v << endl; 

	return 0;
}