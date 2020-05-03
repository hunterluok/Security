#include<iostream>
#include<string>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;


struct human
{
	human () {};
	human (const char* name, int inage, const char* indob): age(inage)
	{
		// sname = name;
		// sindob = indob;
		strcpy(sname, name);
		strcpy(sindob, indob);
	}

	char sname[20];
	int age;
	char sindob[20];
	
};

vector<vector<int> > readdata(string path)
{
    ifstream myfile(path, ios_base::in);
    if(myfile.is_open())
    {
        vector<vector<int> > data;

        string lines;
        while(getline(myfile, lines))
        {
            vector<int> temp;
            istringstream line(lines);
            string temp_str;
            while(line >> temp_str)
            {
                stringstream ss;
                int temp_int;
                ss << temp_str;
                ss >> temp_int;
                temp.push_back(temp_int);
            }
            data.push_back(temp);
        }
        return data;
        myfile.close();
    }
    else
    {
        cout << "file is bad " << endl;
        exit(1);
    }

}


int main()
{


//	human input("lk future", 22, "sangfor");
//
//	ofstream fsout("binary.bin", ios_base::out | ios_base::binary | ios_base::in);
//	if(fsout.is_open())
//	{
//		cout << "writing one object :" << endl;
//		fsout.write(reinterpret_cast<const char*>(&input), sizeof(input));
//		fsout.close();
//	}
//
//	ifstream fsin ("binary.bin", ios_base::in | ios_base::binary);
//	if(fsin.is_open())
//	{
//		human somepeople;
//		fsin.read((char*)&somepeople, sizeof(somepeople));
//		cout << "read data :" << endl;
//		cout << " name :" << somepeople.sname << endl;
//		cout << "age :" << somepeople.age << endl;
//		cout << "out : " << somepeople.sindob << endl;
//		fsin.close();
//
//	}
    vector<vector<int> > data;
    data = readdata("t.txt");
    cout << data[0][1]<< " " << data[0][2] << endl;

	return 0;
}