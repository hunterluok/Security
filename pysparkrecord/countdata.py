

import pyspark.sql.functions as fn

def correct_cig(feat):
    return fn.when(fn.col(feat)=='男',0).when(fn.col(feat)=='女',1).otherwise(99)  # 这里注意 fn.when(fn.col(feat)=='男',0).when
#data = data.select('gender').withColumn('gender',correct_cig('gender'))
data = data.withColumn('gender',correct_cig('gender'))



col_name = data.columns
col_rdd = data.rdd.map(lambda row :[e for e in row]) #利用rdd.map 将 dataframe 进行 rdd --- 列表转换  列表如何转换成rdd

for i,col in enumerate(col_name):
    agg= col_rdd.groupBy(lambda row : row[i]).map(lambda row: (row[0],len(row[1])))
    print(col,sorted(agg.collect(),key=lambda el:el[1],reverse=True))
print(col_rdd)


#print(data.agg(*[fn.countDistinct(c) for c in p]).show()) # 如何像groupby的效果？


############################## 筛选出所有  需要进行  哑变量 转换的。
import pyspark.sql.types as typ
cols =[(col.name,col.dataType) for col in data.schema]
string_cols =[]
num_cols = []
for i,s in enumerate(cols):
    if s[1]==typ.StringType():
        string_cols.append(s[0])
    else:
        num_cols.append(s[0])

# 对 部门string型 数据 转换成 int 型
num_cols = ['sbl','timecj','sb_year_bjl','sb_month_bjl','sb_long_bjl','sb_zhou_bjl']
del_cols =['sfygjj','sfjnsb','sfzzgzf','sqjb','sqrlx']

str_cols = []
for i in string_cols:
    if (i not in num_cols) and(i not in del_cols):
        str_cols.append(i)
select_feature=str_cols + num_cols
data = data.select(select_feature)


#for i in ts:
#    data = data.withColumn(i,data[i].cast(typ.IntegerType()))  # 如何快速将需要的 字段转换成需要的 数据类型。 这样转换不行，将汉字 也算整形了


col_names = new_data.columns
col_rdd = new_data.rdd.map(lambda row :[e for e in row]) #利用rdd.map 将 dataframe 进行 rdd --- 列表转换  列表如何转换成rdd

for i,col in enumerate(col_names):
    agg= col_rdd.groupBy(lambda row : row[i]).map(lambda row: (row[0],len(row[1])))
    print(col,sorted(agg.collect(),key=lambda el:el[1],reverse=True))
col_rdd


for i in last_feature:  #这里注意 ，先将float 转化成 int 型 再转化成 string<,接着进行下一步的转。
    new_data = new_data.withColumn(i,new_data[i].cast(typ.IntegerType()))  # 如何快速将需要的 字段转换成需要的 数据类型。 这样转换不行，将汉字 也算整形了
    if i not in num_cols:
        new_data = new_data.withColumn(i,new_data[i].cast(typ.StringType()))

import pyspark.mllib.linalg as ln
import pyspark.mllib.feature as ft
import pyspark.mllib.regression as reg

hashing = ft.HashingTF(7)

last_data = new_data \
    .rdd \
    .map(lambda row: [
            list(hashing.transform(row[1]).toArray())
                if col == 'bjsxmc_index'
                else row[i]
            for i, col
            in enumerate(last_feature)]) \
    .map(lambda row: [[e] if type(e) == int else e
                      for e in row]) \
    .map(lambda row: [item for sublist in row
                      for item in sublist]) \
    .map(lambda row: reg.LabeledPoint(
            row[0],
            ln.Vectors.dense(row[1:]))
        )

y_data = new_data.where('gender==99')   # 待预测的 数据
use_data = new_data.where('gender!=2.0') # 训练数据
train_data,validation_data,test_data = use_data.randomSplit([0.6,0.3,0.1])

#from pyspark.ml.feature import VectorAssembler
#$va = VectorAssembler(inputCols=['category'],outputCol='features')
#va.transform(df).head().features
# params = {va.inputCols:['b','a'],va.outputCol:"vector"}
# va.transform(df,params).head().vector


#sqlContext 也能创建 dataframe
# df = sqlContext.createDataFrame([(0, "a"),(1, "b"), (2, "c"),  (3, "a"),(4, "a"), (5, "c")], ["id", "category"])
# stringIndexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
# model = stringIndexer.fit(df)
# indexed = model.transform(df)


# encoder = OneHotEncoder(inputCol="categoryIndex", outputCol="categoryVec")
# encoded = encoder.transform(indexed)
# encoded.show()
#from pyspark.ml.feature import VectorAssembler
#va = VectorAssembler(inputCols=['categoryVec'],outputCol='xx')
#va.transform(encoded).head().xx
#print(df)
#print(encoded.select('categoryVec'))
#print(encoded.select('categoryVec').show())
#for line in encoded.select('categoryVec'):
#print(line.toArray)