
# include<iostream>
# include<string>

using namespace std;

int main(){
string greatings ("helle std::string");
cout<<greatings<<endl;

cout<<"enter a line of text:"<<endl;

string firstline;
getline(cin,firstline);

cout<< "enter another"<<endl;
string secline;
getline(cin,secline);

cout<<"result of concatenation"<<endl;
string concat=firstline +" " + secline;
cout<<concat<<endl;

cout<<"copy of concatenated string:"<<endl;
string copy;
copy = concat;
cout<<copy<<endl;
cout<<concat.length()<<endl;
return 0;

}


