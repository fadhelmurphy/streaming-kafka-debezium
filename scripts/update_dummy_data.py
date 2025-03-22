from faker import Faker
import random
from helpers import wait_for_db

conn = wait_for_db()

cursor = conn.cursor()
faker = Faker()

cursor.execute("UPDATE transactions SET status = 'pending' WHERE id = 1;")

conn.commit()
cursor.close()
conn.close()
print("✅ Update Data dummy berhasil!")
