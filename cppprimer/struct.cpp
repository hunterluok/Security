#include<iostream>
#include<string>
using namespace std;

struct human
{
	human(int sage,string sname)
	:age(sage),name(sname) {}

	int getage()
	{
		return age;
	}

	string get_name()
	{
		return name;
	}

private:
	int age;
	string name;
};


struct test
{	
	test(int da, test* nnexts)
	{
		data = da;
		nexts = nnexts;
	}

// private:
	int data;
	test* nexts;

};

struct node
{
	int data;
	node* nexts;
};


template<typename T> 
class link
{
public:
	node* mylink;

public:
	void insert(T data)
	{
		if(mylink == NULL)
		{
			mylink->data = data;

		}
		else
		{
			node* temp = mylink;
			while(temp->nexts !=NULL)
			{
				temp = temp->nexts;
			}
			// node* temp_node = new node(data, NULL);
			node temp_node(data, NULL);
			temp->nexts = &temp_node;
		}
	}
};



int main()
{
	// human* myhuamn = new human(22,"xxx");
	// cout << myhuamn-> getage() 
	// cout << myhuamn.getage() << endl;
	test* t1 = new test(22, NULL);
	test* t2 = new test(32, t1);
	test* t3 = new test(11, t2);

	test* temp = t3;
	int count = 0;
	while(temp != NULL)
	{
		cout << "data is " << temp->data << endl;
		count ++;
		temp = temp->nexts;

	}
	cout << "count is " << count << endl;

	link<int> ss;
	ss.insert(10);
	ss.insert(22);
	ss.insert(9);

	return 0;
}