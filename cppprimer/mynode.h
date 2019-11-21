#include<iostream>

using namespace std;

struct single
{
	int data;
	single* nexts;
};

struct treenode
{	
	int data;
	treenode* left;
	treenode* right;
};

template<typename T>
void shownode(T* node)
{
	while(node != nullptr)
	{
		cout << "-- " << node->data << endl;
		node = node->nexts;
	}
}

template<typename T>
void shownode_ano(T* node)
{
	if(node != nullptr)
	{
		if(node->nexts != nullptr)
		{
			shownode_ano(node->nexts);
		}
		cout << " recurive ele is " << node->data << endl;
	}
}

single* reverse(single* node)
{
	single *newhead = nullptr;
	while(node !=nullptr)
	{
		single* temp = node;
		node = node->nexts;
		temp->nexts = newhead;
		newhead = temp;
	}
	return newhead;
}
