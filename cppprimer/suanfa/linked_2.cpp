#include<iostream> 
#include<string>
#include<stack>


using namespace std;


class node
{
public:
	friend class nodelist;
	node()
	{
		next = NULL;
	}
	node(int ndata, node * newnode = NULL)
	{
		data = ndata;
		next = newnode;
	}

private:
	int data;
	node * next;
};


class nodelist
{
public:
	nodelist()
	{
		head = new node();
	}
	nodelist(node *newnode)
	{
		head = newnode;
	}
	~nodelist()
	{
		delete head;
	}
	bool insertnode(int data);
	void show();
	void reverseshow();
	stack<node*> mynodestack;
private:
	node *head;
};

bool nodelist:: insertnode(int data)
{
	node *p = head;
	node *mynode= new node(data);
	if(mynode == NULL)
	{
		return false;
	}
	if(p == NULL)
	{
		head = mynode;
		return true;
	}
	while(p->next != NULL)
	{
		p = p->next;
	}
	p->next = mynode;
	return true;
}

void nodelist::show()
{
	node *p = head;
	while(p != NULL)
	{
		cout << "ele is " << p->data << endl;
		p = p->next;
	}
}

void nodelist:: reverseshow()
{
	node *p = head;
	while(p != NULL)
	{
		mynodestack.push(p);
		p = p->next;
	}
	while(!mynodestack.empty())
	{
		node* pnode = mynodestack.top();
		cout << "e is " << pnode->data << endl;
		mynodestack.pop();
	}
}

int main()
{
	nodelist mylist;
	mylist.insertnode(22);
	//
	mylist.insertnode(11);
	mylist.insertnode(15);
	mylist.show();
	// stack<node*> mystack;
	mylist.reverseshow();

	return -1;
}