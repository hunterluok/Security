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


class human
{
private:
	int age;
	bool gender;
	mystring name;

public:
	human(const mystring myname, int inputage, bool inputgender)
	: name(myname),age(inputage),gender(inputgender) {}

	int getage()
	{
		return age;
	}

};

int main()
{
	mystring firstman("zs");
	mystring secondman("eve");

	cout << "sizeof (mystring)" << sizeof(mystring) << endl;
	cout << "sizeof (firstman)" << sizeof(firstman) << endl;
	cout << "sizeof (secondman)" << sizeof(secondman) << endl;

	human firsthu(firstman, 25, true);
	human sencodhu(secondman, 33 , false);

	cout << "sizeof (humna)" << sizeof(human) << endl;
	cout << "sizeof (firsthu)" << sizeof(firsthu) << endl;
	cout << "sizeof(sencodhu)" << sizeof(sencodhu) << endl;
	return 0;
}


