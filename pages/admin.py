import sqlite3
import streamlit as st

st.title(
    "📋 Admin Dashboard"
)

conn = sqlite3.connect(
    "healthcare.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT *
    FROM feedback
    """
)

feedback_rows = cursor.fetchall()

conn.close()

st.subheader(
    "User Feedback"
)

for row in feedback_rows:

    st.write(
        f"⭐ {row[1]}/5"
    )

    st.write(
        row[2]
    )

    st.markdown("---")