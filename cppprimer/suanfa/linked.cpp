
#include<iostream> 
using namespace std;





template<typename T> class listnode
{
public:
	friend  class linklist<T>;
	
	listnode()
	{
		next = NULL;
	}
	listnode(T item, listnode<T> *nextnode = NULL)
	{
		data = item;
		next = nextnode;
	}
	~listnode()
	{
		next = NULL;
	}
	

private:
	T *next;
	T data;

}


template<typename T>  class linklist
{
public:
	linklist()
	{
		head = new listnode();
	}
	linklist(listnode *node)
	{
		// head =  new listnode(data, NULL);
		head = node;
	}
	~linklist()
	{
		delete head;
	}

	bool insertnode(int data);

private:
	listnode *head;
};


/*
 bool linklist:: insertnode(int data)
{
	listnode *p = head;
	listnode *node = new listnode(data);
	if(node == NULL)
	{
		return false;
	}
	while(p->next != NULL)
	{
		p = p->next;
	}
	p->next = node;
	return true;
}
*/

/*
template<typename T> void linklist<T>:: showdata()
{
	listnode *p = head
	if(p !=null)
	{
		cout << "ele is " << p->data << endl;
	}
	while(p->next !=NULL)
	{
		p = p->next;
		cout << "ele is " << p->data << endl;
	}
}
*/

int main()
{
	linklist mylist;

	mylist.insertnode(3);
	mylist.insertnode(4);
	mylist.insertnode(10);

	return -1;
}