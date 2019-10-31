#!/usr/bin/env bash
hadoop fs -rm -r for3
hadoop fs -rm -r data.txt
hadoop fs -put data.txt
hadoop jar /Users/luokui/bigdata/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.job.name="JE" \
-D mapred.map.tasks=1 \
-D mapred.reduce.tasks=1 \
-input  data.txt \
-output for3 \
-mapper  "python mapper.py" \
-reducer  "python reducer.py" \
-file mapper.py  reducer.py