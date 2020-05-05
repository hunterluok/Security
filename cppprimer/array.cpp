
#include <iostream>
using namespace std;

void displayarray(int numbers[],int length)
{
	for(int index=0;index<length;++index){
		cout<<numbers[index]<<' ';
	}
	cout<<endl;

}

void displayarray(char characters[],int length){
	for(int index=0;index<length;++index){
		cout<<characters[index]<<' ';
	}
	cout<<endl;
}

int main()
{
int mynumbers[4] = {24,58,-1,245};
displayarray(mynumbers,4);

char mychars[6]={'h','e','l','l','o','\0'};
displayarray(mychars,6);
return 0;
}
