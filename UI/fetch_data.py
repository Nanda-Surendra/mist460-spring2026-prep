import requests
import pandas as pd
import streamlit as st

FASTAPI_URL = "http://localhost:8000"

def fetch_data(endpoint : str, params : dict, method: str = "get") -> pd.DataFrame:
    if method == "get":
        response = requests.get(f"{FASTAPI_URL}/{endpoint}", params=params)

    if response.status_code == 200:
        payload = response.json()
        rows = payload.get("data", [])
        df = pd.DataFrame(rows)
        return df

    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None
