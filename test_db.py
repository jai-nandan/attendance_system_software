
import psycopg

try:
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="face_recognizer",
        user="postgres",
        password="jai5911"
    )

    print("PostgreSQL connected successfully!")

    with conn.cursor() as cur:
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name")
        tables = cur.fetchall()
        print("Tables found:", tables)

        cur.execute("SELECT COUNT(*) FROM public.student")
        print("Student records:", cur.fetchone()[0])

        cur.execute("SELECT COUNT(*) FROM public.register")
        print("Register records:", cur.fetchone()[0])

    conn.close()

except Exception as e:
    print("Database connection/error:", e)
