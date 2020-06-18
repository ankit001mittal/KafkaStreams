import sys
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.context import SQLContext


if __name__ == '__main__':

    n_secs = 1
    topic = "mytopic"

    conf = SparkConf().setAppName("KafkaStreamProcessor").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, n_secs)
        
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {
                            'bootstrap.servers':'localhost:9092', 
                            'fetch.message.max.bytes':'15728640',
                            'auto.offset.reset':'smallest'})
                            # Group ID is completely arbitrary

    lines = kafkaStream.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
    counts.pprint()

    ssc.start()
    time.sleep(600) # Run stream for 10 minutes just in case no detection of producer
    # ssc.awaitTermination()
    ssc.stop(stopSparkContext=True,stopGraceFully=True)




