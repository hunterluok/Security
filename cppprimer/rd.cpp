#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<int> temp_line;
    vector< vector<int> > Vec_Dti;
    string line;

    ifstream in("t.txt");  //读入文件
    regex pat_regex("[[:digit:]]+");  //匹配原则，这里代表一个或多个数字

    while(getline(in, line)) 
    {  //按行读取
        for (sregex_iterator it(line.begin(), line.end(), pat_regex), end_it; it != end_it; ++it) {  //表达式匹配，匹配一行中所有满足条件的字符
            // cout << it->str() << " ";  
            //输出匹配成功的数据
            temp_line.push_back(stoi(it->str()));  
            //将数据转化为int型并存入一维vector中
        }
        Vec_Dti.push_back(temp_line);  //保存所有数据
        temp_line.clear();
    }

    for(int i=0; i <Vec_Dti.size(); i++) {  //输出存入vector后的数据
        for(int j=0; j<Vec_Dti[0].size(); j++) {
            cout << Vec_Dti[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}