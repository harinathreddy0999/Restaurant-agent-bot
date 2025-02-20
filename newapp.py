import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Debugging: Print to check if the token is loaded
APPLICATION_TOKEN = "OPEN API KEY"
if APPLICATION_TOKEN is None:
    raise ValueError("APP_TOKEN is not set. Please check your .env file.")

# Define constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "9c55e3db-f93a-4fe1-a07a-31fadf5e6bf3"
FLOW_ID = "0a7f156a-e035-4457-94df-f46a3e1a0221"
ENDPOINT = "restaurent"  # The endpoint name of the flow

# Function to run the flow
def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {"Authorization": f"Bearer {APPLICATION_TOKEN}", "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    
    return response.json()
# Main function
def main():
    st.title("Restaurant Chat Interface")

    message = st.text_area("Message", placeholder="Ask something...")

    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return

        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)

        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()