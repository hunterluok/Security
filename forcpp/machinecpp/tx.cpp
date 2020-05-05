#include <iostream>
#include <map>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;
char buffer[100000];

int relationTotal;
map<string, int> relationMapping;
vector<string> nam;

void show_map(map<string, int> v)
{
	map<string, int>::iterator ier = v.begin();
	while(ier != v.end())
	{
		cout << "key is " << ier->first << " value is " << ier->second << endl;
		ier ++;
	}
}


// void read_data(int flag, string name, map<string,int> wordMapping, vector<int> &headList, vector<int> &tailList, vector<int> &relationList, vector<int> &Length,
// 		vector<vector<int> > &Lists, vector<vector<int> > &PositionE1, vector<vector<int> > &PositionE2, map<string,vector<int> > &bags)

bool read_data(int flag, string name)
{
	ifstream f("../../data/"+name+".txt");
	if(!f)
	{
		cout << "file is wrong " << endl;
		return false;
	}

	int sc = 0;
	string line;
	while (getline(f, line))  
	{
		istringstream data(line);

		string temp;
		vector<string> vec_temp;
		int count = 0;
		while(data >> temp)
		{
			vec_temp.push_back(temp);
			count += 1;
			if(count == 5)
			{
				break;
			}
		}
		string e1 = vec_temp[0];
		string e2 = vec_temp[1];
		// int head  = wordMapping[vec_temp[2]];
		string head_s = vec_temp[2];
		string tail_s = vec_temp[3];
		// int tail = wordMapping[tail_s];
		string relat_string = vec_temp[4];

		cout << "e1 " << e1 << " e2 " << e2 << " head_s " << head_s;
		cout << " tail_s " << tail_s << " -- " << relat_string << endl;

		// 利用getline 将 sstream 转换为 string.这里需要注意的哦。
		string nd;
		getline(data, nd);
		cout << "dat is " << nd << endl;

		sc++;
		if(sc > 10)
		{
			break;
		}
		// string e1 = buffer;
		// fscanf(f,"%s",buffer);
		// string e2 = buffer;

		// fscanf(f,"%s",buffer);
		// string head_s = (string)(buffer);
		// int head = wordMapping[(string)(buffer)];

		// fscanf(f,"%s",buffer);
		// int tail = wordMapping[(string)(buffer)];
		// string tail_s = (string)(buffer);

		// fscanf(f,"%s",buffer);
		// if (flag)
		// 	bags[e1+"\t"+e2+"\t"+(string)(buffer)].push_back(headList.size());
		// else
		// 	bags[e1+"\t"+e2].push_back(headList.size());
		// int num = relationMapping[(string)(buffer)];

		//cout<<e1+"\t"+e2+"\t"+(string)(buffer)<<' '<<num<<endl;
		// int len = 0, lefnum = 0, rignum = 0;
		// vector<int> tmpp;
		// while (fscanf(f,"%s", buffer)==1) 
		// {
		// 	std::string con = buffer;
		// 	if (con=="###END###") 
		// 		break;
		// 	int gg = wordMapping[con];
		// 	if (con == head_s) 
		// 		lefnum = len;
		// 	if (con == tail_s) 
		// 		rignum = len;
		// 	len++;
		// 	tmpp.push_back(gg);
		// }
		// headList.push_back(head);
		// tailList.push_back(tail);
		// relationList.push_back(num);
		// Length.push_back(len);
		// vector<int> con,conl, conr;
		// for (int i = 0; i < len; i++) 
		// {
		// 	con.push_back(tmpp[i]);
		// 	conl.push_back(lefnum - i);
		// 	conr.push_back(rignum - i);
		// 	if (conl[i] >= limit) conl[i] = limit;
		// 	if (conr[i] >= limit) conr[i] = limit;
		// 	if (conl[i] <= -limit) conl[i] = -limit;
		// 	if (conr[i] <= -limit) conr[i] = -limit;
		// 	conl[i]+=limit;
		// 	conr[i]+=limit;
		// }
		// Lists.push_back(con);
		// PositionE1.push_back(conl);
		// PositionE2.push_back(conr);
	}
	return true;
}


int  main()
{ 
	cout << "Begin_init_para" << endl;
	// ifstream mfile("../../data/relation2id.txt", ios::in);
	// if(!mfile)
	// {
	// 	cout << "file is wrong" << endl;
	// 	return 0;
	// }
	// string line;
	// while(getline(mfile, line))
	// {
	// 	istringstream data(line);
	// 	string d1;
	// 	int d2;
	// 	data >> d1;
	// 	data >> d2;
	// 	relationMapping[d1] = d2;
	// 	nam.push_back(d1);
	// 	// cout << "--" << d1 << " " << d2 << endl;
	// }
	// show_map(relationMapping);
	// cout<<"relationTotal:\t"<<relationTotal<<endl;
	bool res = false;
	int flag = 1;
	res = read_data(flag, "test_zh");
	return 0;
}

// int  main()
// {
// 	cout<<"Begin_init_para"<<endl;
// 	FILE* f = fopen("../../data/relation2id.txt", "r");
// 	while (fscanf(f,"%s",buffer)==1) {
// 		int id;
// 		fscanf(f,"%d",&id);
// 		relationMapping[(string)(buffer)] = id;
// 		relationTotal++;
// 		nam.push_back((string)(buffer));
// 	}
// 	fclose(f);
// 	cout<<"relationTotal:\t"<<relationTotal<<endl;
// 	return 0;
// }