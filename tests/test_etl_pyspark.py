import pytest
import ujson
from pyspark.sql.session import SparkSession
from pyspark.sql.types import Row

@pytest.fixture
def spark():
    return SparkSession.builder.appName("test").getOrCreate()

def test_spark_version(spark):
    assert spark.version == "3.1.3"

def test_create_data_from_range(spark):
    data = spark.range(1, 7, 2).collect()
    result = [Row(id=1), Row(id=3), Row(id=5)]
    assert data == result

def test_create_dataframe(spark):
    data = [Row(name="abc", id=1)]
    df = spark.createDataFrame(data)
    assert df is not None

def test_count_dataframe(spark):
    data = [Row(name="abc", id=1)]
    df = spark.createDataFrame(data)
    assert df.count() == 1
