#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	string mystring ("hello future");
	cout << "mystring is :" << mystring << endl;

	// size_t 和 int 都可以的
	for(int ncharcount=0; ncharcount < mystring.length();  ++ncharcount)
	{
		cout << "char [" << ncharcount << "] is :";
		cout << mystring[ncharcount] << endl;
	}


	int chaoff = 0;
	string::const_iterator ichar;
	for (ichar = mystring.begin(); ichar != mystring.end(); ++ichar)
	{
		cout << "char [" << chaoff ++ << "] is :" ;
		cout << *ichar << endl;
	}

	string my (" hello lk");
	string my2 ("  hello memory");

	const char* my3 = " hello job";  // C风格的字符串。

	mystring += my;
	mystring.append(my2);
	mystring += my3;
	mystring.append(my3);

	string newmystring ("wo shi luo ai luo luo luo");
	const char mychar = 'o';

	int posit = newmystring.find(mychar, 0);

	while (posit != string::npos)
	{
		cout << mychar << "xx :" << posit << endl;

		int nposit = posit + 1;

		posit = newmystring.find(mychar, nposit);

	}
	
	//else
	// {
	//		cout << "not find;";
	// }

    // cout << "erase : " << newmystring.erase(10,20) << endl;
    cout << "newmystring " << newmystring << endl;
    const char nmychar = 'l';

    string::const_iterator myiter = find(newmystring.begin(), newmystring.end(),nmychar);

    while(myiter != newmystring.end()) // 删掉 nmychar 之后所有的元素。
    {
    	newmystring.erase(myiter);

    }
    cout <<"mystring is : " << newmystring << endl;
	// cout << "mystring is :" << mystring << endl;
	// cout << "posit : \"lk\" " << posit << endl;

	reverse (mystring.begin(),mystring.end());
	cout << "mystring reverse is :" << mystring << endl;

	transform(mystring.begin(),mystring.end(),mystring.begin(),toupper);
	cout << "mystring toupper" << endl;


	return 0;
}