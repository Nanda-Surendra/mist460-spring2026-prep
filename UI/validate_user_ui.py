import streamlit as st
from fetch_data import fetch_data

def validate_user_ui():

    st.header("Validate User")
    username = st.text_input("Username *")
    password = st.text_input("Password *", type="password")

    if st.button("Validate"):
        params = {}
        if username.strip():
            st.error("Username is required.")
        else:
            params["username"] = username.strip()
        if password.strip():
            st.error("Password is required.")
        else:
            params["password"] = password.strip()

        df = fetch_data("validate_user", params)

        if df is not None and not df.empty:
            st.success("User validated successfully!")
            output_string = "App User ID: " + str(df["AppUserID"].values[0]) + ", Full Name: " + df["FullName"].iloc[0]
            st.write(output_string)
            st.session_state.app_user_id = df["AppUserID"].values[0]
        else:
            st.error("Invalid username or password.")