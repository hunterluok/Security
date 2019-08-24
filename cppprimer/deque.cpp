#include <iostream>
#include <deque>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

int main()
{
	// deque <int> mydeque;
	stack <int> mystack;
	mystack.push(22);
	mystack.push(21);
	mystack.push(20);

	while(mystack.size() != 0)
	{
		cout << "top is : " << mystack.top() << endl;
		mystack.pop();
	}

	if(mystack.empty())  // 不是 isempty;
	{
		cout << "e ,is empty" << endl;
	}
	queue <int> myqueue;
	myqueue.push(22);
	myqueue.push(21);
	myqueue.push(20);

	while(myqueue.size() != 0)
	{
		cout << "front is : " << myqueue.front() << endl;
		cout << "back is : " << myqueue.back() << endl;
		myqueue.pop(); // 从前面 pop 掉 而不能从后面。
	}
	if(myqueue.empty())  // 不是 isempty;
	{
		cout << "e ,queue is empty" << endl;
	}
	// cout << mystack.top() << endl;

	priority_queue <int, vector<int>, greater<int> >  pg;
	pg.push(22);
	pg.push(3);
	pg.push(23); // 自动就排序好了
	//pg.pop();
	//for(size_t n=0; n<pg.size(); ++n)
	// cout << " : " << pg.top() << endl;

	while (pg.size() !=0)  //while 可以执行多次 ，但是 if 只执行一次。
	{
		cout << "pg top " << pg.top() << endl;
		pg.pop();
	}
	return 0;

}