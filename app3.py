import streamlit as st
import requests

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
    .resource-card p {
        color: #334155 !important;
    }
    .card-title {
        color: #1d4ed8 !important;
        font-size: 23px;
        font-weight: 700;
        margin-top: 4px;
        margin-bottom: 2px;
    }
    .card-subtitle {
        font-size: 12px;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 14px;
    }
    .guidance-box {
        background-color: #f1f5f9 !important;
        border-left: 4px solid #1d4ed8 !important;
        padding: 15px;
        border-radius: 6px;
        margin-top: 14px;
        font-size: 15px;
        line-height: 1.6;
    }
    .tier-badge-highest {
        background-color: #fef9c3 !important;
        color: #713f12 !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
        border: 1px solid #eab308 !important;
        display: inline-block;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER DISPLAY ---
st.markdown("""
<div class="app-header">
    <h1 style='margin:0; color: #1d4ed8; font-size: 38px; font-weight: 800; letter-spacing: -0.03em;'>AeroLaunch</h1>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION DECK ---
if "page" not in st.session_state:
    st.session_state.page = "Feed"

nav_cols = st.columns(4)
with nav_cols[0]:
    if st.button("🏠 Home Feed", use_container_width=True, type="primary" if st.session_state.page == "Feed" else "secondary"):
        st.session_state.page = "Feed"
        st.rerun()
with nav_cols[1]:
    if st.button("🧭 Pilot Roadmap", use_container_width=True, type="primary" if st.session_state.page == "Pilots" else "secondary"):
        st.session_state.page = "Pilots"
        st.rerun()
with nav_cols[2]:
    if st.button("🎙️ ATC Roadmap", use_container_width=True, type="primary" if st.session_state.page == "ATC" else "secondary"):
        st.session_state.page = "ATC"
        st.rerun()
with nav_cols[3]:
    if st.button("🤖 AeroBot AI", use_container_width=True, type="primary" if st.session_state.page == "AI" else "secondary"):
        st.session_state.page = "AI"
        st.rerun()

st.write("") 

# --- ZAPIER WEBHOOK AI INFERENCE ROUTE ---
def query_zapier_ai(prompt_text):
    """Pipes the user prompt into Zapier Webhooks and returns the automated response."""
    if "ZAPIER_WEBHOOK_URL" not in st.secrets:
        return "⚠️ Configuration Error: Please add your `ZAPIER_WEBHOOK_URL` into the Streamlit Secrets tab."
    
    webhook_url = st.secrets["ZAPIER_WEBHOOK_URL"]
    
    # Bundle the student's question cleanly
    payload = {"prompt": prompt_text}
    
    try:
        response = requests.post(webhook_url, json=payload, timeout=20)
        
        if response.status_code in [200, 201]:
            try:
                res_json = response.json()
                # Try parsing standard text hooks returns
                if "response" in res_json:
                    return res_json["response"].strip()
                elif "text" in res_json:
                    return res_json["text"].strip()
                elif "output" in res_json:
                    return res_json["output"].strip()
            except Exception:
                # Fallback to text raw return if Zapier hook returns a flat string
                if response.text:
                    return response.text.strip()
            
            return "✅ Query processed by Zapier successfully! Check your integration action dashboard for the output."
        else:
            return f"⚠️ Zapier endpoint returned status code: {response.status_code}. Verify your active Zap setup."
    except Exception as e:
        return f"⚠️ Network pipeline timeout: {str(e)}. Please try sending your query again."

# --- ROUTING LOGIC ---

# PAGE 1: HOME FEED
if st.session_state.page == "Feed":
    st.markdown("### 📢 Mission Briefing")
    st.markdown("""
    <div class="resource-card">
        <div class="card-title">The High-School Aviation Deployment Matrix</div>
        <div class="card-subtitle">System Status: Operational</div>
        <p style='font-size: 17px;'>Welcome to AeroLaunch. Use the navigation deck above to deploy into your chosen vector.</p>
    </div>
    """, unsafe_allow_html=True)

# PAGE 2: PILOT HUB
elif st.session_state.page == "Pilots":
    st.markdown("### 🧭 Student Pilot Flight Matrix")
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">Aviation 101 Ground Course</div>
        <div class="card-subtitle">Provider: Embry-Riddle Aeronautical University (ERAU)</div>
        <p style='font-size: 16px;'>A comprehensive online academic baseline detailing structural aerodynamics.</p>
    </div>
    """, unsafe_allow_html=True)

# PAGE 3: ATC HUB
elif st.session_state.page == "ATC":
    st.markdown("### 🎙️ Air Traffic Control Vector Matrix")
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">VATSIM Virtual Controller Certification (S1, S2)</div>
        <p style='font-size: 16px;'>A global, high-fidelity simulation network using actual ATC phraseology.</p>
    </div>
    """, unsafe_allow_html=True)

# PAGE 4: LIVE CHATBOT INTERFACE (ZAPIER-POWERED)
elif st.session_state.page == "AI":
    st.markdown("### 🤖 AeroBot Dynamic Flight Simulator Terminal")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello! I am AeroBot. My backend is fully linked up to Zapier. Ask me absolutely ANY dynamic ground school question!"}
        ]
        
    for message in st.session_state.chat_history:
        avatar_icon = "🤖" if message["role"] == "assistant" else "🧑‍✈️"
        with st.chat_message(message["role"], avatar=avatar_icon):
            st.write(message["content"])
            
    if user_input := st.chat_input("Ask AeroBot anything..."):
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="🧑‍✈️"):
            st.write(user_input)
            
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Streaming request through Zapier core automated matrices..."):
                zapier_reply = query_zapier_ai(user_input)
            st.write(zapier_reply)
            st.session_state.chat_history.append({"role": "assistant", "content": zapier_reply})
