from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import GradientBoostedTrees
from pyspark.mllib.linalg import SparseVector, DenseVector

sparse_data = [
    LabeledPoint(0.0, DenseVector([0,  1.0, 2])),
    LabeledPoint(1.0, DenseVector([0, 1, 1.0])),
    LabeledPoint(0.0, DenseVector([1, 0, 1.0])),
    LabeledPoint(1.0, DenseVector([1, 1.3,  2.0])),
    LabeledPoint(1.0, DenseVector([1, 2.1,  1.6])),
]


#data = sc.parallelize(sparse_data)
data = None

model = GradientBoostedTrees.trainRegressor(data, categoricalFeaturesInfo={0:2}, numIterations=10)

print(model.numTrees())

print(model.totalNumNodes())

model.predict(DenseVector([1, 1, 1.0]))
model.predict(DenseVector([0, 0, 1.0]))

#rdd = sc.parallelize([[0.0, 1.0], [1.0, 0.0]])
#model.predict(rdd).collect()