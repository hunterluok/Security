
# include<iostream>
# include<string>
using namespace std;

int main()
{
cout<<"su ru 2ge float"<<endl;
float a1=0.0;
float a2=0.0;
cin>>a1;
cin>>a2;

cout<<"jin xing jisuan,shuru char:"<<endl;

char selectchar ='\0';
cin >> selectchar;

if (selectchar=='d')
{
 cout<<"chu fa"<<endl;
	if(a2!=0)
		{ cout<<"re:"<<a1/a2<<endl;}
	else
		{cout<<"chu shu bu wei 0"<<endl;}
}
else
{
cout<<"result :"<<a1+a2<<endl;
}
return 0;
}
