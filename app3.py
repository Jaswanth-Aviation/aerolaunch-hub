import streamlit as st
import urllib.request
import json

# --- CORE RESPONSE STRUCTURE CONFIGURATION ---
st.set_page_config(
    page_title="AeroLaunch Hub",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CLEAN WELCOMING LIGHT MODE STYLING ---
st.markdown("""
<style>
    .stApp [data-testid="stMarkdownContainer"], 
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp li, .stApp span, .stApp div {
        font-family: "Times New Roman", Times, serif !important;
    }
    .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    .app-header {
        text-align: center;
        padding: 24px 10px;
        background: linear-gradient(135deg, #e2e8f0 0%, #f1f5f9 100%) !important;
        border-bottom: 3px solid #1d4ed8 !important;
        border-radius: 14px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    }
    .resource-card {
        background: #ffffff !important;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #cbd5e1 !important;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }
    .resource-card p { color: #334155 !important; }
    .card-title { color: #1d4ed8 !important; font-size: 23px; font-weight: 700; margin-top: 4px; }
    .card-subtitle { font-size: 12px; color: #64748b !important; text-transform: uppercase; letter-spacing: 0.07em; }
    .guidance-box { background-color: #f1f5f9 !important; border-left: 4px solid #1d4ed8 !important; padding: 15px; border-radius: 6px; margin-top: 14px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER DISPLAY ---
st.markdown('<div class="app-header"><h1 style="margin:0; color: #1d4ed8; font-size: 38px; font-weight: 800;">AeroLaunch</h1></div>', unsafe_allow_html=True)

# --- NAVIGATION DECK ---
if "page" not in st.session_state:
    st.session_state.page = "Feed"

nav_cols = st.columns(4)
buttons = [("🏠 Home Feed", "Feed"), ("🧭 Pilot Roadmap", "Pilots"), ("🎙️ ATC Roadmap", "ATC"), ("🤖 AeroBot AI", "AI")]
for i, (label, p_name) in enumerate(buttons):
    with nav_cols[i]:
        if st.button(label, use_container_width=True, type="primary" if st.session_state.page == p_name else "secondary"):
            st.session_state.page = p_name
            st.rerun()

# --- ROUTING LOGIC ---
if st.session_state.page == "Feed":
    st.markdown("### 📢 Mission Briefing")
    st.markdown('<div class="resource-card"><div class="card-title">High-School Aviation Deployment Matrix</div><p>Welcome to AeroLaunch. This portal was engineered specifically to solve the information gap for high school students looking to enter professional aviation.</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "Pilots":
    st.markdown("### 🧭 Student Pilot Flight Matrix")
    st.markdown('<div class="resource-card"><div class="card-title">Aviation 101 Ground Course</div><p>A comprehensive online academic baseline detailing structural aerodynamics and instrumentation arrays.</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "ATC":
    st.markdown("### 🎙️ Air Traffic Control Vector Matrix")
    st.markdown('<div class="resource-card"><div class="card-title">VATSIM Virtual Controller Certification</div><p>A global, high-fidelity simulation network where student controllers manage real virtual pilot flights.</p></div>', unsafe_allow_html=True)

# --- DYNAMIC AI PAGE (NO KEYS REQUIRED) ---
elif st.session_state.page == "AI":
    st.markdown("### 🤖 AeroBot: Avionics Ground Instructor")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [{"role": "assistant", "content": "AeroBot online and fully accessible. Ask me anything about aviation regulations, flight mechanics, or training matrices!"}]
        
    for text in st.session_state.chat_history:
        icon = "🤖" if text["role"] == "assistant" else "🧑‍✈️"
        with st.chat_message(text["role"], avatar=icon):
            st.write(text["content"])
            
    if prompt := st.chat_input("Query aerodynamics, FAA regulations, terminal fields..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑‍✈️"):
            st.write(prompt)
            
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Processing flight telemetry arrays..."):
                try:
                    # Formulate a completely free, cross-origin open-access API request
                    api_url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt + ' (Answer as an expert aviation flight instructor)')}"
                    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response:
                        reply = response.read().decode('utf-8')
                except Exception as e:
                    reply = "Telemetry Error: Unable to sync with the public flight engine. Please verify your internet connection link."
            
            st.write(reply)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
