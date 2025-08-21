import mysql.connector
from datetime import datetime

# Branded identity tag
db_identity = "R0bsen_DB!2025"

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R0bsen_DB!2025",  # ✅ Correct password
        database="R0bsen_DB"
    )
    cursor = conn.cursor()

    # Create log table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS integration_log (
            id INT AUTO_INCREMENT PRIMARY KEY,
            status VARCHAR(255),
            timestamp DATETIME,
            note TEXT,
            identity_tag VARCHAR(255)
        )
    """)

    # Insert success log with branded identity
    cursor.execute("""
        INSERT INTO integration_log (status, timestamp, note, identity_tag)
        VALUES (%s, %s, %s, %s)
    """, (
        "✅ Success",
        datetime.now(),
        "MySQL–Python connection verified. Branded backend alive.",
        db_identity
    ))

    conn.commit()
    print(f"[🧠 {db_identity}] ✅ Connection verified — backend faith alive.")
except mysql.connector.Error as err:
    print(f"[🧠 {db_identity}] ❌ Connection failed: {err}")
    # Optional: log failure
    if 'cursor' in locals():
        cursor.execute("""
            INSERT INTO integration_log (status, timestamp, note, identity_tag)
            VALUES (%s, %s, %s, %s)
        """, (
            "❌ Failure",
            datetime.now(),
            str(err),
            db_identity
        ))
        conn.commit()
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()