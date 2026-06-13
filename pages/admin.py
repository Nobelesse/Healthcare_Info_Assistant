import sqlite3
import streamlit as st
import pandas as pd

st.title(
    "📋 Admin Dashboard"
)

conn = sqlite3.connect(
    "healthcare.db"
)

feedback_df = pd.read_sql_query(
    "SELECT * FROM feedback",
    conn
)

conn.close()

st.subheader(
    "Feedback Records"
)

st.dataframe(
    feedback_df,
    use_container_width=True
)

if not feedback_df.empty:

    csv = feedback_df.to_csv(
        index=False
    )

    st.download_button(
        "⬇ Download Feedback CSV",
        csv,
        "feedback.csv",
        "text/csv"
    )