from pyspark.sql.session import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.streaming import StreamingQuery
from etl_pyspark.modules.spark.IPySparkManager import IPySparkManager


class PySparkManager(IPySparkManager):
    def __init__(self, app_name: str):
        self.spark = (
            SparkSession
                .builder
                .appName(app_name)
                .enableHiveSupport()
                .getOrCreate()
        )
        print("Spark version: ", self.spark.version)

    def readStream(self, schema: str, resources: str):
        return (
            self.spark
                .readStream
                .schema(schema)
                .option("maxFilesPerTrigger", 5)
                .json(resources)
        )

    def writerStream(self, func, stream):
        return (
            stream
                .writeStream
                .outputMode("append")
                .foreach(func)
                .start()
        )
