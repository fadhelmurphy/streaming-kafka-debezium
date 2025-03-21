from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "salesdb_server.public.transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for msg in consumer:
    print("Data Baru:", msg.value)
