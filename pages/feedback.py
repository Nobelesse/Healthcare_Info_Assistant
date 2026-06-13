import streamlit as st

st.title("⭐ Feedback")

rating = st.slider(
    "Rate the Application",
    min_value=1,
    max_value=5,
    value=5
)

feedback = st.text_area(
    "Share your feedback"
)

if st.button("Submit Feedback"):

    st.success(
        "Thank you for your feedback!"
    )

    st.write(
        f"Rating Submitted: {rating}/5"
    )

    if feedback:
        st.write(
            "Feedback received."
        )