from kafka import KafkaProducer
import pprint
from faker import Faker
#from bson.json_util import dumps
import time

# Generating fake data

myFactory = Faker()
myFactory.random.seed(5467)

for i in range(10):

    data = myFactory.name()
    print("data: ", data)

    KAFKA_VERSION = (0, 10)
    producer = KafkaProducer(bootstrap_servers=['kafka:29092'], retries=5, api_version = KAFKA_VERSION)

    producer.send('mytopic', data.encode('utf-8'))

    # block until all async messages are sent
    producer.flush()
    # tidy up the producer connection
    producer.close()
    time.sleep(0.5)
