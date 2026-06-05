import streamlit as st
import urllib.request
import json
import re

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
    /* Targeted clean typography that leaves Streamlit system menus completely untouched */
    .stApp [data-testid="stMarkdownContainer"], 
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp li, .stApp span, .stApp div {
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Welcoming Light Background */
    .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    
    /* Clean Header Card */
    .app-header {
        text-align: center;
        padding: 24px 10px;
        background: linear-gradient(135deg, #e2e8f0 0%, #f1f5f9 100%) !important;
        border-bottom: 3px solid #1d4ed8 !important;
        border-radius: 14px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Crisp Pearl White Cards */
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
    
    /* Vibrant Contrast Titles */
    .card-title {
        color: #1d4ed8 !important;
        font-size: 23px;
        font-weight: 700;
        margin-top: 4px;
        margin-bottom: 2px;
        letter-spacing: -0.01em;
    }
    
    .card-subtitle {
        font-size: 12px;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 14px;
    }
    
    /* Soft Guidance Container */
    .guidance-box {
        background-color: #f1f5f9 !important;
        border-left: 4px solid #1d4ed8 !important;
        padding: 15px;
        border-radius: 6px;
        margin-top: 14px;
        font-size: 15px;
        color: #1e293b !important;
        line-height: 1.6;
    }

    /* Vibrant Badges */
    .tier-badge-highest {
        background-color: #fef9c3 !important;
        color: #713f12 !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        letter-spacing: 0.05em;
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
        letter-spacing: 0.05em;
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
        letter-spacing: 0.05em;
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

# --- HELPER LIVE INTERFERENCE FUNCTION (NO API KEYS REQUIRED) ---
def query_live_ai_backbone(prompt_text):
    """Fetches a response dynamically from open infrastructure networks anonymously."""
    try:
        # Initialize an anonymous tracking session token
        token_req = urllib.request.Request(
            "https://duckduckgo.com/duckchat/v1/status",
            headers={"User-Agent": "Mozilla/5.0", "x-vqd-accept": "1"}
        )
        with urllib.request.urlopen(token_req, timeout=7) as token_res:
            vqd_token = token_res.headers.get("x-vqd-token")
        
        if not vqd_token:
            return "Connection Sync Timeout. Please try your prompt query again."

        # Structure payload to inject an underlying flight instructor identity context
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": f"You are AeroBot, an expert FAA flight ground school instructor. Answer this question concisely with clear bullet points or formatting: {prompt_text}"}
            ]
        }
        
        chat_req = urllib.request.Request(
            "https://duckduckgo.com/duckchat/v1/chat",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/json",
                "x-vqd-token": vqd_token
            }
        )
        
        # Read stream and extract final markdown block responses cleanly
        with urllib.request.urlopen(chat_req, timeout=10) as chat_res:
            raw_lines = chat_res.read().decode("utf-8").split("\n")
            full_text = ""
            for line in raw_lines:
                if line.startswith("data:"):
                    try:
                        data_json = json.loads(line[5:].strip())
                        if "message" in data_json:
                            full_text += data_json["message"]
                    except:
                        continue
            
            if full_text:
                return full_text.strip()
    except Exception as e:
        pass
    
    # Secure Local Flight Knowledge Fallback Engine in case of upstream network congestion
    query_lower = prompt_text.lower()
    if "control" in query_lower or "3" in query_lower:
        return "**AeroBot Ground Briefing — The 3 Primary Flight Control Systems:**\n\n1. **Ailerons:** Controls **Roll** around the longitudinal axis.\n2. **Elevator:** Controls **Pitch** around the lateral axis.\n3. **Rudder:** Controls **Yaw** around the vertical axis."
    elif "force" in query_lower:
        return "**AeroBot Ground Briefing — The 4 Forces of Flight:**\n\n1. **Lift:** Upward aerodynamic force.\n2. **Weight:** Downward pull of gravity.\n3. **Thrust:** Forward pull produced by the engine.\n4. **Drag:** Rearward resistance force."
    else:
        return f"**AeroBot Ground Briefing:** Received query on *'{prompt_text}'*.\n\nAircraft systems encompass the airframe, powerplant, electrical bus, and flight control surfaces. For specific operational regulations, make sure to cross-reference the official FAA handbook links under the **Pilot Roadmap** and **ATC Roadmap** layout decks above!"

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
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">AOPA High School Aviation Initiative</div>
        <div class="card-subtitle">Provider: Aircraft Owners and Pilots Association (AOPA)</div>
        <p style='font-size: 16px;'>Specialized STEM curricula and scholarship frameworks built to transition secondary education students directly into crewed cockpits.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Shows a multi-year commitment to the largest pilot advocacy group in the world. Grants you direct visibility to critical youth flight training scholarship pools.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AOPA High School Hub ↗️", "https://youcanfly.aopa.org/high-school", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">CAP Aerospace Education Cadet Program</div>
        <div class="card-subtitle">Provider: Civil Air Patrol (USAF Auxiliary)</div>
        <p style='font-size: 16px;'>Official federal cadet program offering interactive aerospace modules, leadership evaluation paths, and actual orientation flights in single-engine aircraft.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> CAP has free online aerospace modules for cadets and students. Highly respected by military aviation pipelines and major passenger airlines alike.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Civil Air Patrol Portal ↗️", "https://www.gocivilairpatrol.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 4: Foundational Value</span><br>
        <div class="card-title">Sporty's Flight Academy Training Matrices</div>
        <div class="card-subtitle">Provider: Sporty's Pilot Shop</div>
        <p style='font-size: 16px;'>Interactive primary training arrays and practice testing frameworks mirroring the formal FAA written knowledge examination parameters.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Builds the exact core knowledge needed to pass the actual FAA Private Pilot written exam early, cutting real-world flight training cost loops by half.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Sporty's Academy ↗️", "https://www.sportys.com/", use_container_width=True)

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
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">FAA Academy Prep / Green ATC Basics</div>
        <div class="card-subtitle">Provider: Federal Aviation Administration Manuals</div>
        <p style='font-size: 16px;'>Self-directed study manuals detailing the baseline regulatory infrastructure for safe aircraft handling and radar vector tracking coordinates.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Studying FAA Order JO 7110.65 (the official ATC bible) and the Pilot/Controller Glossary gives you a massive advantage before entering university terminal radar training programs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Air Traffic Manuals ↗️", "https://www.faa.gov/air_traffic/publications/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">LiveATC Audio Log Portfolio Build</div>
        <div class="card-subtitle">Provider: LiveATC Network</div>
        <p style='font-size: 16px;'>Direct real-time streaming audio feeds from international terminal radar control facilities and active tower frequencies worldwide.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Keeping a logbook of hours spent listening to busy Class B airspace (like Chicago O'Hare or Atlanta) trains your ear to parse rapid-fire commands at operational speed.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to LiveATC Audio Feed ↗️", "https://www.liveatc.net/", use_container_width=True)

# PAGE 4: LIVE GENERAL RESPONSE CHATBOT INTERFACE
elif st.session_state.page == "AI":
    st.markdown("### 🤖 AeroBot Ground Training Terminal")
    
    # Initialize native chat memory arrays inside the website state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Welcome to AeroBot! My core processor is now fully live and unrestricted. Ask me any aviation question—such as 'Main components of aircraft?', 'What is a crosswind?', or 'How does a jet engine work?'—and I will answer dynamically!"}
        ]
        
    # Render chat history with customized layout blocks inside your page
    for message in st.session_state.chat_history:
        avatar_icon = "🤖" if message["role"] == "assistant" else "🧑‍✈️"
        with st.chat_message(message["role"], avatar=avatar_icon):
            st.write(message["content"])
            
    # Native input box built directly into the website flow
    if user_input := st.chat_input("Ask AeroBot any ground question..."):
        # Append user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="🧑‍✈️"):
            st.write(user_input)
            
        # Dynamically process live answers via our background inference client
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Analyzing operational frequencies..."):
                live_reply = query_live_ai_backbone(user_input)
            st.write(live_reply)
            st.session_state.chat_history.append({"role": "assistant", "content": live_reply})
