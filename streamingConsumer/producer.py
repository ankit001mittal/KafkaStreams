from kafka import KafkaProducer
import pymongo
import pprint
from pymongo import MongoClient
from bson.json_util import dumps
import time


while(True):

    # Generating fake data

    myFactory = Faker()
    data = myFactory.random_number()

    # Produce sample message from localhost
    # producer = KafkaProducer(bootstrap_servers=['localhost:9092'], retries=5)
    # Produce message from docker
    producer = KafkaProducer(bootstrap_servers=['kafka:29092'], retries=5)

    producer.send('live-transactions', dumps(data))

    # block until all async messages are sent
    producer.flush()
    # tidy up the producer connection
    producer.close()
    time.sleep(0.5)
