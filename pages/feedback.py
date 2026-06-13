import sqlite3
import streamlit as st

st.title("⭐ Feedback")

rating = st.slider(
    "Rate the Application",
    1,
    5,
    5
)

feedback = st.text_area(
    "Share your feedback"
)

if st.button(
    "Submit Feedback"
):

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO feedback(
            rating,
            feedback
        )
        VALUES(?,?)
        """,
        (
            rating,
            feedback
        )
    )

    conn.commit()

    conn.close()

    st.success(
        "Feedback saved successfully."
    )