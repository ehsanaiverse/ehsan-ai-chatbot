import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# --- Configuration & Constants ---
PAGE_TITLE = "Ehsan AI ChatBot"
PAGE_ICON = "🤖"
LAYOUT = "wide"

THEME_COLORS = {
    "primary": "#4F46E5",
    "secondary": "#818CF8",
    "background": "#0F172A",
    "text": "#F8FAFC"
}

MODELS = {
    'llama-3.1-8b-instant': 'Llama 3.1 8B (Fast)',
    'llama-3.3-70b-versatile': 'Llama 3.3 70B (Smart)'
}

# --- Styling ---
def load_css():
    st.markdown(f"""
    <style>
        /* Modern Glassmorphism Theme */
        .stApp {{
            background-color: {THEME_COLORS['background']};
            color: {THEME_COLORS['text']};
        }}
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {{
            background-color: #1E293B;
            border-right: 1px solid #334155;
        }}
        
        /* Chat Message Styling */
        .stChatMessage {{
            background-color: rgba(30, 41, 59, 0.5);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        
        div[data-testid="stChatMessage"] {{
            background-color: rgba(30, 41, 59, 0.5);
        }}

        .stChatMessage p, .stChatMessage div, .stChatMessage span {{
            color: #FFFFFF !important;
        }}

        .stChatMessage[data-testid="user-message"] {{
            background: linear-gradient(135deg, {THEME_COLORS['primary']} 0%, {THEME_COLORS['secondary']} 100%);
            border: none;
        }}
        
        /* Input Field Styling */
        .stTextInput > div > div > input {{
            background-color: #1E293B;
            color: white;
            border: 1px solid #475569;
            border-radius: 8px;
        }}
        
        .stTextInput > div > div > input:focus {{
            border-color: {THEME_COLORS['primary']};
            box-shadow: 0 0 0 1px {THEME_COLORS['primary']};
        }}
        
        /* Button Styling */
        .stButton > button {{
            background: linear-gradient(to right, {THEME_COLORS['primary']}, {THEME_COLORS['secondary']});
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.2s;
        }}
        
        .stButton > button:hover {{
            opacity: 0.9;
            transform: scale(1.02);
        }}
        
        /* Header Styling */
        h1, h2, h3 {{
            color: {THEME_COLORS['text']} !important;
            font-family: 'Inter', sans-serif;
        }}
        
        /* Hide Streamlit Branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- State Management ---
class SessionState:
    @staticmethod
    def initialize():
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'model_id' not in st.session_state:
            st.session_state.model_id = 'llama-3.3-70b-versatile'
        if 'temperature' not in st.session_state:
            st.session_state.temperature = 0.7
        if 'system_prompt' not in st.session_state:
            st.session_state.system_prompt = "You are a helpful, professional AI assistant. Answer concisely and accurately."

# --- Core Logic ---
class ChatBot:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        
    def get_llm(self):
        if not self.api_key:
            st.error("API Key not found. Please set GROQ_API_KEY in your .env file.")
            return None
        return ChatGroq(
            model=st.session_state.model_id,
            temperature=st.session_state.temperature,
            api_key=self.api_key
        )

# --- UI Components ---
def render_sidebar():
    with st.sidebar:
        st.title(f"Settings")
        st.divider()
        
        # Model Selection
        st.subheader("Model Configuration")
        
        # Helper to find index safely
        current_model = st.session_state.model_id
        model_keys = list(MODELS.keys())
        index = model_keys.index(current_model) if current_model in model_keys else 0
        
        st.session_state.model_id = st.selectbox(
            "Select Model",
            options=model_keys,
            format_func=lambda x: MODELS[x],
            index=index
        )
        
        st.session_state.temperature = st.slider(
            "Creativity (Temperature)",
            min_value=0.0, max_value=1.0, value=st.session_state.temperature, step=0.1
        )
        
        # System Prompt
        st.subheader("Persona")
        st.session_state.system_prompt = st.text_area(
            "System Instructions",
            value=st.session_state.system_prompt,
            height=100
        )
        
        st.divider()
        
        # Actions
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Clear", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
        with col2:
            if st.button("Export", use_container_width=True):
                # Export logic
                export_data = []
                for m in st.session_state.chat_history:
                    role = "user" if isinstance(m, HumanMessage) else "assistant"
                    export_data.append({"role": role, "content": m.content})
                
                json_str = json.dumps(export_data, indent=2)
                st.download_button(
                    "Download", 
                    data=json_str, 
                    file_name=f"chat_export_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json"
                )

def render_chat_interface(bot):
    st.title("Ehsan AI ChatBot")
    
    # Display History
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
             with st.chat_message("user", avatar="👤"):
                st.markdown(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(msg.content)

    # Chat Input
    if prompt := st.chat_input("What can I help you with today?"):
        # Display User Message
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)
        
        # Generate Response
        with st.chat_message("assistant", avatar="🤖"):
            llm = bot.get_llm()
            if llm:
                try:
                    # Construct messages
                    messages = [SystemMessage(content=st.session_state.system_prompt)] + st.session_state.chat_history
                    messages.append(HumanMessage(content=prompt))
                    
                    # Stream response
                    stream = llm.stream(messages)
                    response = st.write_stream(stream)
                    
                    # Update History
                    st.session_state.chat_history.append(HumanMessage(content=prompt))
                    st.session_state.chat_history.append(AIMessage(content=str(response)))
                
                except Exception as e:
                    st.error(f"An error occurred: {e}")

# --- Main App ---
def main():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)
    load_css()
    SessionState.initialize()
    
    bot = ChatBot()
    render_sidebar()
    render_chat_interface(bot)

if __name__ == "__main__":
    main()
