from etl_pyspark.modules.spark.PySparkManager import PySparkManager
from etl_pyspark.flows.IMainCoordinator import IMainCoordinator
from pyspark.sql.streaming import StreamingQuery
from pyspark.sql.dataframe import DataFrame


class StreamFilesFlow(IMainCoordinator):
    def __init__(self, spark_manager: PySparkManager):
        self.spark_manager = spark_manager
        super().__init__()

    def start(self, stream) -> StreamingQuery:
        return self.spark_manager.writerStream(self.process_row, stream)

    @staticmethod
    def process_row(row) -> None:
        print(row)



