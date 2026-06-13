import streamlit as st


def save_query(query):

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(query)