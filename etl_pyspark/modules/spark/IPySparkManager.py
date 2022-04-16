import logging
from abc import ABC, abstractmethod
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.streaming import StreamingQuery


class IPySparkManager(ABC):
    def __init__(self):
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    @abstractmethod
    def readStream(self, schema: str, resources: str):
        pass

    @abstractmethod
    def writerStream(self, func, stream):
        pass
