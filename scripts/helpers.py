def wait_for_db():
    import psycopg2
    MAX_RETRIES = 5
    for i in range(MAX_RETRIES):
        try:
            conn = psycopg2.connect(
                host="postgres",
                database="salesdb",
                user="user",
                password="password"
            )
            print("✅ Koneksi ke database berhasil!")
            return conn
        except psycopg2.OperationalError:
            print(f"⏳ Database belum siap, mencoba lagi ({i+1}/{MAX_RETRIES})...")