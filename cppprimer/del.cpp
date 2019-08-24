#include<iostream>
using namespace std;

class mystring
{
private:
	char* buffer;

public:
	mystring(const char* initinput)
	{
		cout << "creat a new string" << endl;
		if (initinput != NULL)
		{
			buffer = new char [strlen(initinput)+1];
			strcpy(buffer, initinput);
			cout << "buff post is :ox " << hex;
			cout << (unsigned int*) buffer << endl;
		}
		else
		{
			buffer = NULL;
		}
	}


	mystring(const mystring& copysource)
	{
		cout << "copy constructor : copying from mystring" << endl;
		if (copysource.buffer != NULL)
		{
			buffer = new char[strlen(copysource.buffer) + 1];
			strcpy(buffer,copysource.buffer);

			cout << "buffer points to :Ox" << hex;
			cout << (unsigned int*)buffer << endl;
		}
		else
		{
			buffer = NULL;
		}
	}


	~mystring()
	{
		cout << "invoking ,clearing up" << endl;
		if (buffer!= NULL)
		{
			delete [] buffer;
		}
	}

	int getlength()
	{
		return strlen(buffer);
	}

	const char* getstring()
	{
		return buffer;
	}
};


void usemystring(mystring input)
{
	cout << "String buffer in mystring is " << input.getlength();
	cout << "char long" << endl;

	cout << "buffer contains" << input.getstring() << endl;
	return ;
}

mystring copy(mystring& source)
{
	mystring copyforreturn(source.getstring());
	return copyforreturn;
}


int main()
{
	//mystring sayhello("hello for string class");
	//cout << "string buffer in mystring is" << sayhello.getlength() << endl;
	//cout << "char long " << endl;

	//cout << "get if " << sayhello.getstring() << endl;
	//mystring sayhello("hello future");
	//usemystring(sayhello);
	mystring sayhello("hello world c++");
	mystring sayhelloagain(copy(sayhello));


	return 0;
}