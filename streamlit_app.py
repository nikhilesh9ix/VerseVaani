import streamlit as st
import requests
import json
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are ShlokaSevak, a wise and devotional assistant who explains Sanskrit shlokas in English.
For each Sanskrit verse:
1. Provide a poetic and clear English translation.
2. Break down the verse word-by-word with meanings.
3. Explain the deeper spiritual or cultural context.
Respond respectfully, and ask for clarification if the input is unclear.
"""
}

#Streamlit
st.set_page_config(page_title="VerseVaani 📜", page_icon="📜")
st.title("📜 VerseVaani – Sanskrit Shloka Explainer")

# --- Initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display existing messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#Input box
user_input = st.chat_input("Enter a Sanskrit shloka or question...")

if user_input:

    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": [SYSTEM_PROMPT] + st.session_state.messages,
        "temperature": 0.7
    }

    with st.spinner("Thinking..."):
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
    else:
        reply = f"❌ Error {response.status_code}: {response.text}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})