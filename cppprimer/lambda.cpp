# include<iostream>
# include<algorithm>
# include<vector>

using namespace std;

void display(vector<int> & dynarray)
{
	for_each(dynarray.begin(),dynarray.end(),[](int element){ cout<<element<<" "<<endl;});
	cout<<endl;
}

int main(){
	vector <int> Mynumbers;
	Mynumbers.push_back(501);
	Mynumbers.push_back(-1);
	Mynumbers.push_back(25);
	Mynumbers.push_back(-35);

	display(Mynumbers);

	cout<<"sorting them in decengding order"<<endl;

	sort(Mynumbers.begin(),Mynumbers.end(),[](int num1,int num2){ return (num2<num1);});

	display(Mynumbers);
	return 0;
}