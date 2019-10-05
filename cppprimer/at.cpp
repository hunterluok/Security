# include "tspace.h"

# include<iostream>
using namespace std;

int main()
{
    cout << "hello world" << endl;
    using namespace testspace;
    cout << f(4) << endl;

    return 0;

}

