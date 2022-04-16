from dependency_injector import containers, providers
import logging.config

from etl_pyspark.modules.spark.PySparkManager import PySparkManager


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logger.ini",
    )

    spark_manager = providers.Singleton(
        PySparkManager,
        "test[*]"
    )



