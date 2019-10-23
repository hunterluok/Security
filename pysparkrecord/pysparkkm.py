import pyspark
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import PCA
from pyspark.ml.feature import MinMaxScaler

import pyspark.sql.functions as fn

# spark = SparkSession.builder.appName("t").master("local[*]").getOrCreate()


def scale_model(data, inputcol='features', outputcol='scale_features'):
    """
    标准化数据
    """
    mmscale = MinMaxScaler(inputCol=inputcol, outputCol=outputcol)
    scale_model = mmscale.fit(data)
    print(scale_model.originalMax)
    print(scale_model.originalMin)
    scale_data = scale_model.transform(data)
    return scale_data

def pca_model(data, k=7, inputcol='scale_features', outputcol='pca_features'):
    # new_df
    pca = PCA(k=k, inputCol=inputcol, outputCol=outputcol)
    model = pca.fit(data)
    variance = model.explainedVariance
    pca_data = model.transform(data)
    return variance, pca_data


class kmclass:
    def __init__(self, ncluster, select_feature="features", id_feature='word_id'):
        self.kms = KMeans().setK(ncluster).setSeed(1)
        self.id_feature = id_feature
        self.select_feature = select_feature

    def __call__(self, data):
        """
        得到标签数据
        """
        self.model = self.kms.fit(data.select(self.select_feature))
        result = self.model.transform(data.select(self.select_feature, self.id_feature))
        return result.select(self.id_feature, "prediction")

    @property
    def get_model(self):
        """
        获取模型的属性
        """
        return self.model
