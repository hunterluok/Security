# include <iostream>
using namespace std;

int main(){
	cout<<"shuru name:";
	string Name;
	cin >> Name;

	int chartoallocat = Name.length()+1;

	char *copyofname = new char [chartoallocat];

	strcpy(copyofname,Name.c_str());

	cout<<"dynamically allocated buffer contains  "<<copyofname<<endl;
	cout<<chartoallocat<<endl;

	delete []copyofname;
	return 0;
}