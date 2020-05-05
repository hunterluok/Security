
# include<iostream>
# include<string>
using namespace std;

int main(){

char buff[20] = {'\0'};

cout<<"enter a line of text:"<<endl;
string lienenter;
getline(cin,lienenter);

if(lienenter.length()<20)
{
strcpy(buff,lienenter.c_str());
cout<<"buffer contains:"<<buff<<endl;
return 0;

}


}
