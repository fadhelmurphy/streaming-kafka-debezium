from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "salesdb_topic.public.transactions",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for msg in consumer:
    data = msg.value

    # Debugging: Cek isi data
    # print("🔍 RAW MESSAGE:", json.dumps(data, indent=2))

    # Pastikan ada "payload"
    payload = data.get("payload", {})
    
    before = payload.get("before")
    after = payload.get("after")
    op = payload.get("op")

    print(f"🔄 Operasi: {op}")
    if op == "c":
        print(f"✅ Data Baru : {after}")
    elif op == "u":
        print(f"🔻 Sebelum  : {before}")
        print(f"✅ Sesudah  : {after}")
    elif op == "d":
        print(f"🗑️ Data Terhapus : {before}")
    print("-" * 40)