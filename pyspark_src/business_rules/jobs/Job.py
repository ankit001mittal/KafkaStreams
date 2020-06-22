from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
#import spark.implicits._


def main():
    '''
        Fp growth job according to the paper.
    '''
    # Read from the transactions restored db
    print("Reading from Kafka topics... \n")

    inputDf = spark_session.readStream.format("kafka").option("kafka.bootstrap.servers", "kafka:29092").option("subscribe", "mytopic").option("startingOffsets", "earliest").load()

    print("The streamed input is: \n")
    inputDf.printSchema()
    print("The show data is: \n")

    #consoleOutput = inputDf.writeStream.outputMode("append").format("console").start()
    #consoleOutput.awaitTermination()
    
    transactionJsonDf = inputDf.selectExpr("CAST(value AS STRING)")
    

    consoleOutput = transactionJsonDf.writeStream.outputMode("append").format("console").start()
    consoleOutput.awaitTermination()

    print("type:  ", type(transactionJsonDf))

    schema = StructType(
        [ StructField("payment_id", StringType())
        , StructField("merchant_id", StringType())
        , StructField("profile_id", StringType())
        , StructField("transaction_id", StringType())
        , StructField("amount_settlement", IntegerType())
        , StructField("paid_at", StringType())
        , StructField("description", StringType())
        , StructField("redirect_url", StringType())
        , StructField("consumer_ip", StringType())
        , StructField("created_at", StringType())
        , StructField("profile_website", StringType())
        , StructField("profile_merchant_category_code", StringType())
        , StructField("amount_original", IntegerType())
        , StructField("currency_original", StringType())
        , StructField("currency_settlement", StringType())
        , StructField("country_code_based_on_consumer_ip", StringType())
        , StructField("consumer_account", StringType())
        , StructField("consumer_name", StringType())
        , StructField("card_fingerprint", StringType())
        , StructField("card_issue_country", StringType())
        , StructField("paypal_status", StringType())
        , StructField("consumer_bic", StringType())
        , StructField("card_issue_organization", StringType())
        , StructField("consumer_account_country", StringType())
        , StructField("consumer_email_hashed", StringType())
        , StructField("paypal_id_hashed", StringType())
        , StructField("payment_type", StringType())
        , StructField("payment_state", StringType())
        , StructField("row_hashed", StringType())
        ])
    # transactionNestedDf = transactionJsonDf.select(from_json(transactionJsonDf["value"], schema))

    #df = df.withColumn("value", from_json(df["value"], jsonSchema))

    # personFlattenedDf = transactionNestedDf.selectExpr('transaction.payment_id', 'transaction.merchant_id', 'transaction.profile_id', 'transaction.transaction_id',
    #    'transaction.amount_settlement', 'transaction.paid_at', 'transaction.description', 'transaction.redirect_url',
    #    'transaction.consumer_ip', 'transaction.created_at', 'transaction.profile_website',
    #    'transaction.profile_merchant_category_code', 'transaction.amount_original',
    #    'transaction.currency_original', 'transaction.currency_settlement',
    #    'transaction.country_code_based_on_consumer_ip', 'transaction.consumer_account',
    #    'transaction.consumer_name', 'transaction.card_fingerprint', 'transaction.card_issue_country',
    #    'transaction.paypal_status', 'transaction.consumer_bic', 'transaction.card_issue_organization',
    #    'transaction.consumer_account_country', 'transaction.consumer_email_hashed', 'transaction.paypal_id_hashed',
    #    'transaction.payment_type', 'transaction.payment_state', 'transaction.row_hashed')

    # print("Types of : ", type(transactionNestedDf))









if __name__ == '__main__':
    # There is a bug that doesnt pass spark session objects when called from another func
    spark_session = SparkSession.builder \
        .appName("Spark-Kafka") \
        .master("spark://spark-master:7077") \
        .getOrCreate()
    spark_session.sparkContext.setLogLevel("ERROR")  # Set log level to error
    # Execute main method
    main()
