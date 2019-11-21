#include <iostream>
using namespace std;

template <typename T> class linklists
{
public:
	linklists()
	{
		head = new linknode();
	}
	linklists(linknode *node)
	{
		head = node;
	}
	~linklists()
	{
		delete node; //为什么是 delete;
	}

	bool insertnode(linknode *p, T data);
	bool removenode(linknode *p);
	linknode* findnode(T data);
	bool clearnlink();

	T getnode_data(linknode *p);
private:
	linknode *head;
};


template <typename T> class linknode
{
public:
	linknode()
	{
		next = NULL;
	}
	linknode(T item, linknode<T> *nextnode=NULL)
	{
		data = item;
		next = nextnode;
	}
	~linknode()
	{
		next = NULL;
	}
	T getdata()
	{
		return data;
	}
	linknode* getnext()
	{
		return next;
	}
private:
	friend typename linklists<T>;
	T data;
	T *next;

};