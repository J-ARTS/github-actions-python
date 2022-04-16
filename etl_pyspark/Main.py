from dependency_injector.wiring import Provide, inject
from time import perf_counter
from etl_pyspark.flows.MainCoordinator import MainCoordinator
from etl_pyspark.modules.spark.PySparkManager import PySparkManager
from etl_pyspark.di.Container import Container
'''
- PYTHONUNBUFFERED=1;SPARK_HOME=C:\spark\spark-3.1.3-bin-hadoop2.7;PYSPARK_PYTHON=python
'''


@inject
def main(spark_manager: PySparkManager = Provide[Container.spark_manager]) -> None:
    t1 = perf_counter()
    coordinator = MainCoordinator(spark_manager)
    coordinator.start("resources/")
    t2 = perf_counter()
    print(f"Done after {t2-t1}s")

if __name__ == '__main__':
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main()

