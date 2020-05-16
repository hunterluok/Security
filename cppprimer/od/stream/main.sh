#!/usr/bin/env bash

# g++ js2str.cpp -o js2str -ljsoncpp -std=c++11 && js2str /Users/luokui/newdata.txt > t.txt
g++ main.cpp -o main -ljsoncpp -std=c++11 && main /Users/luokui/oddata/  new 256 > t.txt

# g++ main.cpp -o main -ljsoncpp -std=c++11 && main /Users/luokui/newdata.txt 25