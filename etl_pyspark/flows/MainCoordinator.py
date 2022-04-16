from etl_pyspark.modules.spark.PySparkManager import PySparkManager
from etl_pyspark.flows.IMainCoordinator import IMainCoordinator
from etl_pyspark.flows.flows.ReadFilesFlow import ReadFilesFlow
from etl_pyspark.flows.flows.StreamFilesFlow import StreamFilesFlow
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.streaming import StreamingQuery


class MainCoordinator(IMainCoordinator):
    def __init__(self, spark_manager: PySparkManager):
        self.spark_manager = spark_manager
        super().__init__()

    def start(self, path: str) -> None:
        read_stream = self.readFilesFlow(path)
        self.processFilesFlow(read_stream)
        self.finish()

    def readFilesFlow(self, path: str):
        flow = ReadFilesFlow(self.spark_manager)
        return flow.start(path)

    def processFilesFlow(self, read_stream) -> None:
        flow = StreamFilesFlow(self.spark_manager)
        activity_query = flow.start(read_stream)
        activity_query.awaitTermination()

    def finish(self) -> None:
        self.logger.debug("Coordinator Completed")
