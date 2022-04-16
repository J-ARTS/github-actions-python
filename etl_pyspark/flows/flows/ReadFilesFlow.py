from pyspark.sql.types import StructField, StringType, StructType
from etl_pyspark.modules.spark.PySparkManager import PySparkManager
from etl_pyspark.flows.IMainCoordinator import IMainCoordinator
from pyspark.sql.dataframe import DataFrame


class ReadFilesFlow(IMainCoordinator):
    def __init__(self, spark_manager: PySparkManager):
        self.spark_manager = spark_manager
        super().__init__()


    def start(self, path: str):
        schema = StructType([
            StructField("name", StringType(), True),
            StructField("plant", StringType(), True),
            StructField("city", StringType(), True),
        ])
        stream = self.spark_manager.readStream(schema, path)
        stream.printSchema()
        return stream

