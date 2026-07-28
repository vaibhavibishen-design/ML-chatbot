


import streamlit as st

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Chatbot")

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.chat_message("user").write(prompt)

    # Yahan apna chatbot function use karna hai
    response = "Hello! This is my chatbot."

    st.chat_message("assistant").write(response)


    st.markdown("""
<style>

.stApp{
background:#F5F7FB;
}

[data-testid="stHeader"]{
background:transparent;
}

h1{
text-align:center;
color:#4F46E5;
}

</style>
""",unsafe_allow_html=True)
    


   
