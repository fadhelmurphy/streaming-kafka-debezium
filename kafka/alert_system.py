from kafka import KafkaConsumer
import json
import smtplib
from email.mime.text import MIMEText

TOPIC = "salesdb_server.public.transactions"
BROKER = "localhost:9092"

EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"
EMAIL_RECEIVER = "admin@example.com"

def send_email_alert(message):
    msg = MIMEText(message)
    msg["Subject"] = "⚠️ ALERT: Perubahan Data!"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BROKER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for msg in consumer:
    data = msg.value
    if data.get("payload") and data["payload"].get("after"):
        transaction = data["payload"]["after"]
        if transaction["amount"] > 10000000 or transaction["status"] == "failed":
            send_email_alert(f"🚨 ALERT! Perubahan besar terjadi: {transaction}")
