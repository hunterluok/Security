
#include<iostream>
#include<string>

using namespace std;

int main()
{
    string greatings("helle std::string");
    cout << greatings << endl;

    cout<<"enter a line of text:"<<endl;
    string firstline;
    getline(cin, firstline);


    cout << "result of concatenation" << endl;
    string concat = firstline + " " + secline;
    cout << concat < <endl;
    return 0;
}


