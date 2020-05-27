from confluent_kafka import Consumer
import json

# try:
#     print('Welcome to parse engine')
#     # From inside a container
#     #consumer = KafkaConsumer('test-topic', bootstrap_servers='kafka:29092')
#     # From localhost
#     consumer = KafkaConsumer('test-topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
#     for message in consumer:
#         print('im a message')
#         print(message)
        
# except Exception as e:
#     print(e)
#     # Logs the error appropriately. 
#     pass


c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['mytopic'])

print("topic: mytopic")

while True:
    msg = c.poll(1.0)

    print("inside the loop")

    # if msg is None:
    #     continue
    # if msg.error():
    #     print("Consumer error: {}".format(msg.error()))
    #     continue

    print("before the print value")
    for message in c:
        print('Received message: {}'.format(message.value().decode('utf-8')))
    print("after the print value")

c.close()