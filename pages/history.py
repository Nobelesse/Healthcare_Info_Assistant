import sqlite3
import streamlit as st

st.title("📜 Search History")

conn = sqlite3.connect(
    "healthcare.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT query
FROM history
ORDER BY id DESC
""")

rows = cursor.fetchall()

conn.close()

if rows:

    for row in rows:

        st.write(
            f"• {row[0]}"
        )

else:

    st.info(
        "No history found."
    )