#include<iostream>
using namespace std;


class mystring
{
private:
	char* buffer;

public:
	mystring(const char* input)
	{
		if (input != NULL)
		{
			buffer = new char [strlen(input) +1];
			strcpy(buffer, input);
		}
		else
		{
			buffer = NULL;
		}
	}


	mystring(const mystring& copysource)
	{
		if(copysource.buffer != NULL)
		{
			buffer = new char [strlen(copysource.buffer) + 1];
			strcpy(buffer,copysource.buffer);

		}
	}

	~mystring()
	{
		if(buffer !=NULL)
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
