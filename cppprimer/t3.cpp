
#include<iostream>
using namespace std;

int main(){

char sayhello[] = {'h','e','l','l','0',' ','w','o','r','l','d','\0'};
cout<< sayhello<<endl;

cout<<"Size of sayhello:"<<sizeof(sayhello)<<";"<<"sayhello.size()没法用"<<endl;

cout<<"replace space with null:"<<endl;

sayhello[5]='\0';

cout<<sayhello<<endl;
cout<<sizeof(sayhello)<<endl;
return 0;
}
