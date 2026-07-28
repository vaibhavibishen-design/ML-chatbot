import streamlit as st

st.set_page_config(
    page_title="ML Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- Sidebar ----------
with st.sidebar:
    

    st.title("🤖 ML Chatbot")
    dark_mode = st.toggle("🌙 Dark Mode")

    st.markdown("---")

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("### 📚 Suggested Questions")

    st.write("• What is Machine Learning?")
    st.write("• Explain Artificial Intelligence")
    st.write("• Python Interview Questions")
    st.write("• Data Science Roadmap")

    st.markdown("---")

    st.markdown("### ℹ About")

    st.info("""
This chatbot is developed using Streamlit.

Developer: Vaibhavi Bishen
""")
#------------css-----------


# ---------- CSS ----------
if dark_mode:
    st.markdown("""
    <style>

    .stApp{
        background:#0E1117;
        color:white;
    }

    [data-testid="stSidebar"]{
        background:#1E1E1E;
    }

    h1,h2,h3,p,label,span{
        color:white !important;
    }

    [data-testid="stChatMessage"]{
        background:#262730;
        border-radius:12px;
        padding:10px;
        margin-bottom:10px;
    }

    </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>

    .stApp{
        background:#F5F7FB;
    }

    [data-testid="stSidebar"]{
        background:#ECEFF5;
    }

    h1{
        color:#4F46E5;
    }

    [data-testid="stChatMessage"]{
        background:white;
        border-radius:12px;
        padding:10px;
        margin-bottom:10px;
        box-shadow:0 2px 8px rgba(0,0,0,0.1);
    }

    </style>
    """, unsafe_allow_html=True)

# ---------- Main ----------
st.title("🤖 ML Chatbot")

st.caption("Your AI Learning Assistant")

# Welcome Message
st.markdown("### 💡 Try asking:")

col1, col2 = st.columns(2)

with col1:
    st.button("🤖 What is Machine Learning?")
    st.button("🐍 Explain Python")

with col2:
    st.button("📊 Data Science Roadmap")
    st.button("🧠 What is Deep Learning?")
if len(st.session_state.messages) == 0:

    st.chat_message("assistant").write(
        """
👋 Hello!

Welcome to **ML Chatbot**.

You can ask me about:

• Artificial Intelligence

• Machine Learning

• Python

• Data Science
"""
    )

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat Input
prompt = st.chat_input("💬 Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # ---------- Replace This Later ----------
    response = "Hello! This is my chatbot."
    # ---------------------------------------

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )
    st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;color:gray;">
        🤖 ML Chatbot | Built with ❤️ using Streamlit <br>
        © 2026 Vaibhavi Bishen
    </div>
    """,
    unsafe_allow_html=True
)
