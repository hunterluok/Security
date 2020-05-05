# include <iostream>
using namespace std;

int main()
{
	int mynum[5];
	int *pmy = mynum;
	cout <<"pnumber=0x"<<hex<< pmy <<endl;
	cout<<"mynum[0]=ox"<<hex<<&mynum[0]<<endl;

	for(int i=0;i<5;i++)
	{
		cout<<"pnumber=0x"<<hex<<pmy<<endl;
		pmy +=1;
	}

	cout<<"**************************"<<endl;

	for (int i=0;i<5;i++)
	{
		cout<<"mynum point =0x"<<hex<<&mynum[i]<<endl;
	}
	return 0;



}