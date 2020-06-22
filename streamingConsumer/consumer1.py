from kafka import KafkaConsumer


try:
    print('Welcome to parse engine')
    # From inside a container
    #consumer = KafkaConsumer('test-topic', bootstrap_servers='kafka:29092')
    # From localhost
    KAFKA_VERSION = (0, 10)
    consumer = KafkaConsumer('mytopic', bootstrap_servers='localhost:9092', auto_offset_reset='smallest', api_version = KAFKA_VERSION)
    for message in consumer:
        print('im a message')
        inp = (message.value.decode("utf-8"))
        print((message.value.decode("utf-8")))
        
        
        
except Exception as e:
    print(e)
    # Logs the error appropriately. 
    pass
