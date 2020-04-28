#include <iostream>
#include <vector>

using namespace std;

class node
{
public:

    friend class nodelist;

    node(int data, node* newnode):value(data), nexts(newnode)
    {
    }

    node()
    {
    }

    virtual ~node()
    {
    }

    void show()
    {
        cout << "ele is " << value << endl;
    }


private:
    int value;
    node* nexts;
    // virtual ~node();
};


class nodelist
{
public:
    nodelist()
    {
        head = NULL;
    }
    virtual ~nodelist()
    {
        delete head;
    }

    bool insert(int data);
    bool show();
    bool delhead();

private:
    node* head;


};

bool nodelist::insert(int data)
{
    if(head == NULL)
    {
        head = new node(data, NULL);
        return true;

    }
    else
    {
        node* p = head;
        while(p->nexts != NULL)
        {
            p = p->nexts;
        }
        p->nexts = new node(data, NULL);
        return true;

    }
}


bool nodelist::show()
{
    if(head == NULL)
    {
        cout << "link is empty" << endl;
        return false;
    }
    else
    {
        node* p = head;
        while(p != NULL)
        {
            cout << " value is " << p->value << endl;
            p = p->nexts;
        }
        return true;
    }
}

bool nodelist::delhead()
{
    if(head == NULL)
    {
        return true;
    }
    else
    {
        node* p = head;
        head = p->nexts;
        delete p;
        return true;
    }
}


int main()
{
    // node my(2, NULL);
    node* my = new node(2, NULL);
    my->show();
    //cout << my->value << " " << endl;

    cout << "linked list : " << endl;
    nodelist* h = new nodelist();
    h->show();
    h->insert(232);
    h->insert(44);
    h->insert(666);
    h->show();
    h->delhead();
    h->show();

    return 0;
}