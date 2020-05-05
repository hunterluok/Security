CC = g++
HADOOP_INSTALL = /Users/luokui/bigdata/hadoop-2.7.3
PLATFORM = -m64
CPPFLAGS = -m64 -I$(HADOOP_INSTALL)/c++/$(PLATFORM)/include
LIBS = -L$(HADOOP_INSTALL)/c++/$(PLATFORM)/lib -lhadooppipes -lhadooputils -lpthread 
wordcount: wordcount.cpp
	$(CC) $(CPPFLAGS) $< -Wall $(LIBS) -g -O2 -o $@
