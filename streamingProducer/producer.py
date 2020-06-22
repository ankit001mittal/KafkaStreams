from confluent_kafka import Producer
import pprint
from faker import Faker
#from bson.json_util import dumps
import time
import pandas as pd
import pyarrow
import json



def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


# Generating fake data
# myFactory = Faker()
# myFactory.random.seed(5467)

# Reading data from Parquet file
pdf = pd.read_parquet('parquet_dataset.parquet', engine='pyarrow')
json_df = json.loads(pdf.to_json(orient='records'))


for i in json_df:

    # data = myFactory.name()
    #print(i)
    # Produce sample message from localhost
    # producer = KafkaProducer(bootstrap_servers=['localhost:9092'], retries=5)
    # Produce message from docker
    producer = Producer({'bootstrap.servers': 'kafka:29092'})

    producer.poll(0)

    #producer.send('live-transactions', dumps(data).encode('utf-8'))
    producer.produce('mytopic', json.dumps(i, indent=2).encode('utf-8'))

    # block until all async messages are sent
producer.flush()
    # tidy up the producer connection
    # producer.close()
time.sleep(0.5)
