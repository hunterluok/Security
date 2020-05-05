
# include<iostream>
# include<vector>
# include<string>
using namespace std;

int main(){
vector<string> a(3);
a[0]="a";
a[1]="py";
a[2]="on";


cout<<"Number of integers in array"<<a.size()<<endl;
cout<<"enter another number for the array"<<endl;

string b= "xx";
cin>>b;
a.push_back(b);
cout<<"number of integers in array"<<sizeof(a)<<"sds"<<endl;
cout<<"last element in array:";
cout<<a[a.size()-1]<<endl;
return 0;
}
