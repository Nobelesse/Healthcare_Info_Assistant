import streamlit as st

st.title("📜 Search History")

history = st.session_state.get(
    "history",
    []
)

if history:

    for item in reversed(history):

        st.write(f"• {item}")

else:

    st.info(
        "No search history available."
    )