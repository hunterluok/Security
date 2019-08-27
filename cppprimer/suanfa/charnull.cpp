#include<iostream>
using namespace std;

/*
void show(char my[])
{
	//
	int lens = sizeof(my) - 1;
	for(size_t i = 0; i < lens; ++i)
	{
		cout << " element is " << my[i] << endl;
	}
}
*/

int main()
{
	// 这里给 字符数组  赋予 长度空间是一个比较好的办法。
	// char my [20] = "helloword";
	char my [10] = "  ";
	char replace [] = "xxx";
	// cout << my[0] << my[10] <<  "__" << sizeof(my) << endl;

	int my_len = 0;
	int black_count = 0;

	while(my[my_len] != '\0')
	{
		if(my[my_len] == ' ')
		{
			black_count ++;
		}
		// 这一步才能加
		my_len ++;
	}
	int new_len = my_len + 2 * black_count;

	int sizeofmy = new_len;

	cout << "my_len is " << my_len << " count" << black_count << " new_Len is " << new_len << "-" << sizeof(my) << endl;

	// my[new_len] = 's';
	while(new_len > my_len && my_len>=0)
	{
		if(my[my_len]==' ')
		{
			my[new_len--] = 'x';
			my[new_len--] = 'x';
			my[new_len--] = 'x';
		}
		else
		{
			my[new_len--] = my[my_len];
		}
		--my_len;
	}

	for(int i=0; i<sizeofmy ; ++i)
	{
		cout << " ele is " << my[i] << endl;
	}

	// char* my1 = "he";
	// char* my2 = "he";
	// cout << "reut " << my1==my2 << endl;

	return -1;
}