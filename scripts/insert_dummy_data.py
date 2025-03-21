from faker import Faker
import random
from helpers import wait_for_db

conn = wait_for_db()

cursor = conn.cursor()
faker = Faker()

for _ in range(3000000):
    cursor.execute(
        "INSERT INTO transactions (user_id, amount, status) VALUES (%s, %s, %s)",
        (random.randint(1, 10000), round(random.uniform(1000, 50000000), 2), random.choice(["pending", "success", "failed"]))
    )

conn.commit()
cursor.close()
conn.close()
print("✅ Data dummy berhasil dimasukkan!")
