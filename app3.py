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
    .tier-badge-high {
        background-color: #dbeafe !important;
        color: #1e40af !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
        border: 1px solid #60a5fa !important;
        display: inline-block;
        margin-bottom: 8px;
    }
    .tier-badge-medium {
        background-color: #d1fae5 !important;
        color: #065f46 !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
        border: 1px solid #34d399 !important;
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

# --- STABLE HUGGING FACE AI INFERENCE ENGINE ---
def query_aviation_llm(prompt_text):
    """Queries an optimized model via stable API routes instantly."""
    if "HF_TOKEN" not in st.secrets:
        return "⚠️ Configuration Error: Please add your `HF_TOKEN` into the Streamlit Secrets tab."
    
    api_token = st.secrets["HF_TOKEN"]
    
    # Using the universally available open-access endpoint route
    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    
    # Clean system prompt instructions combined directly to maximize execution speed
    full_prompt = (
        f"<s>[INST] You are AeroBot, an expert FAA flight instructor. "
        f"Answer the student's question accurately, directly, and comprehensively using markdown formatting. "
        f"Question: {prompt_text} [/INST]"
    )
    
    payload = {
        "inputs": full_prompt,
        "parameters": {
            "max_new_tokens": 500,
            "temperature": 0.4,
            "return_full_text": False
        },
        "options": {
            "wait_for_model": True
        }
    }
    
    try:
        req = urllib.request.Request(
            api_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_token}",
                "Content-Type": "application/json"
            }
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            
            if isinstance(res_data, list) and len(res_data) > 0:
                reply = res_data[0].get("generated_text", "")
            elif isinstance(res_data, dict):
                reply = res_data.get("generated_text", "")
            else:
                reply = str(res_data)
                
            if reply:
                return reply.strip()
    except Exception as e:
        return f"⚠️ Server update in progress. Please re-send your question in a brief moment! (Details: {str(e)})"
    
    return "No definitive training data returned. Please try rephrasing your request."

# --- ROUTING LOGIC ---

# PAGE 1: HOME FEED
if st.session_state.page == "Feed":
    st.markdown("### 📢 Mission Briefing")
    st.markdown("""
    <div class="resource-card">
        <div class="card-title">The High-School Aviation Deployment Matrix</div>
        <div class="card-subtitle">System Status: Operational</div>
        <p style='font-size: 17px;'>Welcome to AeroLaunch. This portal was engineered specifically to solve the information gap for high school students looking to enter professional aviation. Instead of generic landing loops, this engine presents structured, tiered matrices compiled from verified federal and academic data. Use the navigation deck above to deploy into your chosen vector.</p>
    </div>
    """, unsafe_allow_html=True)

# PAGE 2: PILOT HUB
elif st.session_state.page == "Pilots":
    st.markdown("### 🧭 Student Pilot Flight Matrix")
    st.write("Structured resources built to optimize competitive college applications and accelerate flight training timelines.")
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">Aviation 101 Ground Course</div>
        <div class="card-subtitle">Provider: Embry-Riddle Aeronautical University (ERAU)</div>
        <p style='font-size: 16px;'>A comprehensive online academic baseline detailing structural aerodynamics, instrumentation arrays, atmospheric profiles, and airspace classification systems.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Proves academic capability at the top aviation university in the world. Completing this module is an exceptional 'proof-of-passion' credential to list on early college transcripts.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Official ERAU Portal ↗️", "https://erau.edu/academics/degrees-and-programs/free-online-courses/Aviation-101", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">FAA Part 107 Remote Pilot Certification</div>
        <div class="card-subtitle">Provider: Federal Aviation Administration (FAA)</div>
        <p style='font-size: 16px;'>A formal federal license authorizing commercial unmanned aircraft systems operations. Requires structural recall of chart layouts, weather trends, and aviation safety mandates.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> An official federal license. Proves you understand national airspace, sectional charts, weather graphics, and federal regulations before even logging a real cockpit flight hour.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Unmanned Portal ↗️", "https://www.faa.gov/uas/commercial_operators", use_container_width=True)

# PAGE 3: ATC HUB
elif st.session_state.page == "ATC":
    st.markdown("### 🎙️ Air Traffic Control Vector Matrix")
    st.write("Professional simulation tracks and phraseology baselines designed to secure federal placement pathways.")
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">VATSIM Virtual Controller Certification (S1, S2)</div>
        <div class="card-subtitle">Provider: Virtual Air Traffic Simulation Network</div>
        <p style='font-size: 16px;'>A global, high-fidelity simulation network where student controllers go through rigorous exams and practical tests to manage real virtual pilot flights using actual ATC phraseology.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> You must pass real-world-style ATC entry exams and practical training to control virtual aircraft. Real-world controllers use this to keep their situational awareness locked in.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to VATSIM Network ↗️", "https://vatsim.net/", use_container_width=True)

# PAGE 4: LIVE DYNAMIC RESPONSE CHATBOT INTERFACE
elif st.session_state.page == "AI":
    st.markdown("### 🤖 AeroBot Dynamic Flight Simulator Terminal")
    
    # Initialize native chat memory arrays inside the website state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello! I am AeroBot. My server backend is now fully linked up to live cloud-hosted open models. Ask me absolutely ANY dynamic aviation or ground school question and I will generate an unscripted response!"}
        ]
        
    # Render historical conversation elements
    for message in st.session_state.chat_history:
        avatar_icon = "🤖" if message["role"] == "assistant" else "🧑‍✈️"
        with st.chat_message(message["role"], avatar=avatar_icon):
            st.write(message["content"])
            
    # Capture input dynamically from the viewport chat bar
    if user_input := st.chat_input("Ask AeroBot anything..."):
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="🧑‍✈️"):
            st.write(user_input)
            
        # Run live model processing via API call
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Connecting to live flight intelligence matrix..."):
                live_reply = query_aviation_llm(user_input)
            st.write(live_reply)
            st.session_state.chat_history.append({"role": "assistant", "content": live_reply})
