from kafka import KafkaProducer
import pprint
from faker import Faker
#from bson.json_util import dumps
import time
import pandas as pd
import pyarrow
import json

# Generating fake data
# myFactory = Faker()
# myFactory.random.seed(5467)

# Reading data from Parquet file
pdf = pd.read_parquet('parquet_dataset.parquet', engine='pyarrow')
json_df = json.loads(pdf.to_json(orient='records'))

for i in json_df:

    # data = myFactory.name()
    # print("data: ", data)

    KAFKA_VERSION = (0, 10)
    producer = KafkaProducer(bootstrap_servers=['kafka:29092'], retries=5, api_version = KAFKA_VERSION)

    producer.send('mytopic', i.encode('utf-8'))

    # block until all async messages are sent
    producer.flush()
    # tidy up the producer connection
    producer.close()
    time.sleep(0.5)
