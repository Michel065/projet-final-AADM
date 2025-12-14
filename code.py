import os

import subprocess
print(subprocess.check_output(["where", "java"], text=True))
print(subprocess.check_output(["java", "--version"], text=True))

import pyspark
print("pyspark =", pyspark.__version__)

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
spark.range(5).show()