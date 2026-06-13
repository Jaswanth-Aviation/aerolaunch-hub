# ==========================================
# 1. CORE IMPORTS, DATABASE PERSISTENCE & CONFIG
# ==========================================
import streamlit as st
import json
import os
import re
from datetime import datetime

# Initialize the main page layout configuration
st.set_page_config(
    page_title="AeroLaunch Hub",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Lightweight file paths for persistent JSON storage
USER_DB = "user_db.json"
CHAT_DB = "chat_db.json"

# Auto-generate mock backend data profiles if they do not exist
if not os.path.exists(USER_DB):
    with open(USER_DB, "w") as f:
        json.dump({
            "pilot1": {"name": "Ace Maverick", "email": "pilot1@aerolaunch.com", "password": "password123"},
            "control2": {"name": "Tower Boss", "email": "control2@aerolaunch.com", "password": "password123"}
        }, f, indent=4)

if not os.path.exists(CHAT_DB):
    with open(CHAT_DB, "w") as f:
        json.dump([], f, indent=4)

def load_users():
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)

def load_global_chat():
    with open(CHAT_DB, "r") as f:
        return json.load(f)

def get_avatar_url(nickname):
    # Generates unique profile avatars using the custom Initials API based on nickname letters
    clean_name = re.sub(r'[^a-zA-Z0-9 ]', '', nickname).strip().replace(" ", "%20")
    if not clean_name:
        clean_name = "User"
    return f"https://api.dicebear.com/7.x/initials/svg?seed={clean_name}"

# ==========================================
# 🔐 AUTHENTICATION GATEWAY & SESSION STABILITY
# ==========================================
# Check URL parameter states to prevent unexpected page drops during operations
if st.query_params.get("session") == "active" and st.query_params.get("current_user"):
    st.session_state.logged_in = True
    st.session_state.user_username = st.query_params["current_user"]
    users = load_users()
    if st.session_state.user_username in users:
        st.session_state.user_display_name = users[st.session_state.user_username]["name"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_username" not in st.session_state:
    st.session_state.user_username = ""
if "user_display_name" not in st.session_state:
    st.session_state.user_display_name = ""

# Block unauthenticated view tracking
if not st.session_state.logged_in:
    st.markdown('<div class="auth-container" style="text-align: center; padding: 20px 40px 10px 40px;">', unsafe_allow_html=True)
    st.markdown('<h2 class="auth-title" style="font-size: 36px; color: #1d4ed8; font-family: \'Times New Roman\'; font-weight: bold;">Welcome to AeroLaunch</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    auth_mode = st.radio("Choose Action", ["🔑 Log In to Account", "📝 Register New Account"], horizontal=True, label_visibility="collapsed")
    users = load_users()
    
    if auth_mode == "🔑 Log In to Account":
        with st.form("login_form"):
            st.markdown("### Pilot Login Deck")
            login_user = st.text_input("Username", placeholder="e.g. pilot1")
            # type="password" provides the interactive unhide eye icon to show/hide plaintext inputs
            login_pass = st.text_input("Password", type="password", placeholder="Enter account password")
            submit_login = st.form_submit_button("Enter Flight Deck Controls 🚀", use_container_width=True, type="primary")
            
            if submit_login:
                if login_user in users and users[login_user]["password"] == login_pass:
                    st.session_state.logged_in = True
                    st.session_state.user_username = login_user
                    st.session_state.user_display_name = users[login_user]["name"]
                    
                    st.query_params["session"] = "active"
                    st.query_params["current_user"] = login_user
                    st.success("Access Granted! Loading main hub...")
                    st.rerun()
                else:
                    st.error("Invalid Username or Password. Use 'pilot1' and 'password123' to test.")
                    
    else:
        with st.form("signup_form"):
            st.markdown("### Create New Account Profile")
            new_user = st.text_input("Choose Unique Username (lowercase, no spaces)").strip().lower()
            new_name = st.text_input("Choose Display Nickname (Your dynamic avatar is built from this)")
            new_email = st.text_input("Email Address")
            new_pass = st.text_input("Account Password", type="password", placeholder="Click the built-in eye icon to unhide and verify your password")
            submit_signup = st.form_submit_button("Register Account & Deploy Profile 📡", use_container_width=True)
            
            if submit_signup:
                if not new_user or not new_name or not new_pass:
                    st.error("Please fill out all username, nickname, and password fields.")
                elif " " in new_user:
                    st.error("Username cannot contain spaces.")
                elif new_user in users:
                    st.error("Username is already taken. Please select a different identifier.")
                else:
                    users[new_user] = {
                        "name": new_name,
                        "email": new_email if new_email else f"{new_user}@aerolaunch.com",
                        "password": new_pass
                    }
                    save_users(users)
                    st.success("🎉 Account created successfully! Select 'Log In to Account' above to connect.")

    st.stop()

# Safety profile fallback to catch database changes
users_data = load_users()
current_username = st.session_state.user_username

if current_username not in users_data:
    st.session_state.logged_in = False
    st.query_params.clear()
    st.rerun()

current_nickname = users_data[current_username]["name"]

# ==========================================
# 🧭 SIDEBAR SESSION & FUNCTIONAL LOGOUT
# ==========================================
with st.sidebar:
    st.markdown("### 👤 User Session")
    user_avatar_side = get_avatar_url(current_nickname)
    
    # Styled Profile Badge Card
    st.markdown(f"""
    <div style="text-align: center; padding: 10px; background-color: white; border-radius: 8px; border: 1px solid #cbd5e1; margin-bottom: 10px;">
        <img src="{user_avatar_side}" width="55" style="border-radius: 50%; background: #f1f5f9; border: 2px solid #1d4ed8;"><br>
        <strong style="font-size: 14px; color: #0f172a;">{current_nickname}</strong><br>
        <span style="font-size: 11px; color: #64748b;">@{current_username}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("🟢 Status: Connected as Pilot")
    st.markdown("---")
    
    # Fully functional logout clearing the query states and application logs
    if st.button("🚪 Log Out & Clear Session", use_container_width=True, type="secondary"):
        st.session_state.logged_in = False
        st.session_state.user_username = ""
        st.session_state.user_display_name = ""
        st.query_params.clear()
        st.rerun()

# ==========================================
# 🎨 CLEAN WELCOMING LIGHT MODE STYLING
# ==========================================
st.markdown("""
<style>
    div[data-testid="stMarkdownContainer"]:-webkit-any(:contains("keyboard_double_arrow_left"), :contains("double_arrow_right")) {
        display: none !important;
    }

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
    
    .app-header h1 {
        margin: 0;
        color: #1d4ed8; 
        font-size: 38px; 
        font-weight: 800; 
        letter-spacing: -0.03em;
    }
    
    .resource-card {
        background: #ffffff !important;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #cbd5e1 !important;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }
    
    .resource-card p {
        color: #334155 !important;
        font-size: 15px;
        line-height: 1.5;
        margin-bottom: 8px;
    }

    .resource-link {
        display: inline-block;
        color: #1d4ed8 !important;
        font-weight: bold;
        text-decoration: none;
        margin-top: 6px;
    }
    .resource-link:hover {
        text-decoration: underline;
    }
    
    .card-title {
        color: #1d4ed8 !important;
        font-size: 21px;
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
    .tier-badge-foundational {
        background-color: #f1f5f9 !important;
        color: #475569 !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        border: 1px solid #cbd5e1 !important;
        display: inline-block;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER DISPLAY ---
st.markdown('<div class="app-header"><h1>AeroLaunch</h1></div>', unsafe_allow_html=True)

# --- NAVIGATION DECK ---
if "page" not in st.session_state:
    st.session_state.page = "Feed"

nav_cols = st.columns(8)
pages_list = ["Feed", "Pilots", "ATC", "Crew", "Maintenance", "Drone", "AI", "Community"]
button_labels = ["🏠 Home Feed", "🧭 Pilot Roadmap", "🎙️ ATC Roadmap", "💁‍♀️ Crew Roadmap", "🔧 Maintenance", "🛸 Drone Logistics", "🤖 AeroBot AI", "🌐 Community"]

for idx, p_name in enumerate(pages_list):
    with nav_cols[idx]:
        if st.button(button_labels[idx], use_container_width=True, type="primary" if st.session_state.page == p_name else "secondary"):
            st.session_state.page = p_name
            st.rerun()

st.write("")

# ==========================================
# 🧭 MAIN ROUTING LOGIC & ROADMAP SECTIONS
# ==========================================

# PAGE 1: HOME FEED
if st.session_state.page == "Feed":
    st.markdown("### 📢 Mission Briefing")
    st.markdown(f"""
    <div class="resource-card">
        <div class="card-title">The High-School Aviation Deployment Matrix</div>
        <div class="card-subtitle">System Status: Operational</div>
        <p style='font-size: 17px;'>Welcome back to AeroLaunch, <strong>{current_nickname}</strong>.
        This portal was engineered specifically to solve the information gap for high school students looking to enter professional aviation.
        Instead of generic landing loops, this engine presents structured, tiered matrices compiled from verified federal and academic data.
        Use the navigation deck above to deploy into your chosen vector.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="resource-card" style="margin-top: 15px;">
        <div class="card-title" style="color: #0f172a !important; font-size: 24px;">Jaswanth Mallareddi</div>
        <div class="card-subtitle">Founder & Developer</div>
        <p style='font-size: 17px; line-height: 1.6;'>
            Hi, I am Jaswanth Mallareddi, a 16-year-old who is deeply interested in aviation! I wanted to give 
            valuable opportunities to other future aviation industry students who will turn 16 soon. 
            I have set up 25 high-quality websites for each section of the aviation industry provided, 
            so I hope it is helpful for all you future aviation students!
        </p>
    </div>
    """, unsafe_allow_html=True)

# PAGE 2: PILOT ROADMAP
elif st.session_state.page == "Pilots":
    st.markdown("### ✈️ Section 1: The Pilot Hub")
    st.markdown("#### 🥇 Foundational Academics & Checkride Essentials")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#1: FAA Pilot’s Handbook of Aeronautical Knowledge (PHAK)</div>
        <div class="card-subtitle">Strategic Value: Bedrock Theoretical Knowledge</div>
        <p><strong>Summary:</strong> The definitive textbook covering aerodynamic principles, aircraft systems, flight instruments, weather theory, and basic navigation.</p>
        <p><strong>Strategic Value:</strong> Forms the absolute bedrock of theoretical knowledge required to pass any aviation written exam or oral checkride globally.</p>
        <a class="resource-link" href="https://open.umn.edu/opentextbooks" target="_blank">Open Textbook Library Repository →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#2: FAA Airplane Flying Handbook (AFH)</div>
        <div class="card-subtitle">Strategic Value: Practical Maneuver Standardization</div>
        <p><strong>Summary:</strong> A comprehensive guide focusing on the physical mechanics of flight, including maneuvers, takeoffs, landings, and emergency procedures.</p>
        <p><strong>Strategic Value:</strong> Bridges the gap between classroom theory and real-world stick-and-rudder skills, standardizing flight training maneuvers.</p>
        <a class="resource-link" href="https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/airplane_handbook" target="_blank">FAA Document Gateway →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#3: Pilot Institute Free Private Pilot Ground School Primer</div>
        <div class="card-subtitle">Strategic Value: Early Training Runway Visualization</div>
        <p><strong>Summary:</strong> An introductory video-based course outlining the core requirements, costs, regulations, and basic physics involved in getting a license.</p>
        <p><strong>Strategic Value:</strong> Acts as an accessible, high-yield introductory funnel for student pilots to visualize their entire training timeline before investing capital.</p>
        <a class="resource-link" href="https://pilotinstitute.com/" target="_blank">Pilot Institute Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#4: Sporty’s Study Buddy Exam Prep Engine</div>
        <div class="card-subtitle">Strategic Value: FAA Written Exam Optimization</div>
        <p><strong>Summary:</strong> A dynamic, database-driven practice test module that generates authentic practice questions mimicking the actual FAA Private Pilot written test.</p>
        <p><strong>Strategic Value:</strong> Optimizes exam readiness through targeted testing, allowing users to identify weak knowledge areas before taking official exams.</p>
        <a class="resource-link" href="https://www.sportys.com/" target="_blank">Sporty's Online Prep →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#5: SkyVector Aeronautical Charts</div>
        <div class="card-subtitle">Strategic Value: Airspace Mastery & Active Routing</div>
        <p><strong>Summary:</strong> A real-time, global digital plotting tool providing VFR Sectionals, IFR High/Low charts, and live weather overlays.</p>
        <p><strong>Strategic Value:</strong> Essential for mastering flight planning, visual tracking, and understanding complex airspace boundaries from a web browser.</p>
        <a class="resource-link" href="https://skyvector.com/" target="_blank">SkyVector Live Map →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#6: King Schools Interactive Flight Exam Modules</div>
        <div class="card-subtitle">Strategic Value: Complex Concept Simplification</div>
        <p><strong>Summary:</strong> Interactive mini-modules focusing on challenging flight concepts like crosswind components, weight and balance, and airspace restrictions.</p>
        <p><strong>Strategic Value:</strong> Simplifies complex mathematical and physics-based aviation principles through proven, memorable visual teaching styles.</p>
        <a class="resource-link" href="https://kingschools.com/" target="_blank">King Schools Free Library →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#7: Boldmethod Flight Training Quizzes</div>
        <div class="card-subtitle">Strategic Value: Critical Aeronautical Decision Making</div>
        <p><strong>Summary:</strong> Highly visual, scenario-based quizzes addressing real-world aviation challenges, from systems failures to tricky weather scenarios.</p>
        <p><strong>Strategic Value:</strong> Sharpens quick critical thinking and Aeronautical Decision Making (ADM) skills by putting users into simulated pilot dilemmas.</p>
        <a class="resource-link" href="https://www.boldmethod.com/" target="_blank">Boldmethod Training Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#8: FAA Airman Certification Standards (ACS)</div>
        <div class="card-subtitle">Strategic Value: Definitive Checkride Evaluation Metric</div>
        <p><strong>Summary:</strong> The official regulatory document detailing the exact parameters, tolerances, and knowledge areas tested during a pilot practical exam.</p>
        <p><strong>Strategic Value:</strong> Serves as the ultimate grading standard, ensuring pilots know exactly what constitutes a passing or failing performance on a checkride.</p>
        <a class="resource-link" href="https://www.faa.gov/training_testing/testing/acs" target="_blank">FAA Airman Testing Standards →</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🎮 Flight Simulation & Cockpit Flow Drills")
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#9: X-Plane Scenery Gateway</div>
        <div class="card-subtitle">Strategic Value: Spatial Layout Familiarization</div>
        <p><strong>Summary:</strong> A collaborative database sharing highly accurate, community-vetted airport layouts and visual environments for flight simulation.</p>
        <p><strong>Strategic Value:</strong> Enables highly realistic airport familiarization and taxi routing practice for students preparing to fly into real-world hubs.</p>
        <a class="resource-link" href="https://gateway.x-plane.com/" target="_blank">X-Plane Scenery Hub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#10: FreeChecklists.net Directory</div>
        <div class="card-subtitle">Strategic Value: Standard Checklist Discipline</div>
        <p><strong>Summary:</strong> A massive crowdsourced directory hosting standard operating checklists for hundreds of general aviation and commercial aircraft.</p>
        <p><strong>Strategic Value:</strong> Teaches structural discipline by getting student pilots into the habit of using verified, sequential safety checklists.</p>
        <a class="resource-link" href="http://www.freechecklists.net/" target="_blank">FreeChecklists Repository →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#11: SimBrief Enterprise Dispatch Engine</div>
        <div class="card-subtitle">Strategic Value: Commercial Logistics Readiness</div>
        <p><strong>Summary:</strong> A professional-grade web utility that generates highly realistic virtual flight plans, fuel calculations, and airline operational release documents.</p>
        <p><strong>Strategic Value:</strong> Introduces students to advanced airline dispatching, flight planning, and route fuel management logistics.</p>
        <a class="resource-link" href="https://www.simbrief.com/" target="_blank">SimBrief Routing Tool →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#12: Little Navmap Open-Source Navigation</div>
        <div class="card-subtitle">Strategic Value: Free Navigational Math Practice</div>
        <p><strong>Summary:</strong> A free, open-source flight planner and moving map display featuring airport diagrams, wind overlays, and elevation profiles.</p>
        <p><strong>Strategic Value:</strong> Perfect for introducing cross-country flight planning, vector tracks, and airspace boundary rules without recurring costs.</p>
        <a class="resource-link" href="https://albar965.github.io/littlenavmap.html" target="_blank">Little Navmap GitHub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#13: VOR Navigation Web App Simulator</div>
        <div class="card-subtitle">Strategic Value: Legacy Instrument Orientation Clarity</div>
        <p><strong>Summary:</strong> An interactive, browser-based graphical utility for understanding how instrument needles move relative to ground stations.</p>
        <p><strong>Strategic Value:</strong> Solves one of the hardest conceptual hurdles for new pilots: visualizing relative orientation using legacy radio navigation tools.</p>
        <a class="resource-link" href="https://www.luizmonteiro.com/" target="_blank">LuizMonteiro VOR Sim →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#14: Garmin G1000 Glass Cockpit Interface Guide</div>
        <div class="card-subtitle">Strategic Value: Advanced Interface Onboarding</div>
        <p><strong>Summary:</strong> Official training handbooks breaking down the structure, flight instrument screens, and map menus of modern integrated glass avionics.</p>
        <p><strong>Strategic Value:</strong> Accelerates situational awareness by allowing pilots to master digital avionics navigation menus before stepped training flights.</p>
        <a class="resource-link" href="https://www.garmin.com/" target="_blank">Garmin Digital Manuals →</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🌤️ Meteorology & Radio Communications")
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#15: NOAA Aviation Weather Center (AWC)</div>
        <div class="card-subtitle">Strategic Value: Primary Operational Weather Sourcing</div>
        <p><strong>Summary:</strong> The central US portal providing METARs, TAFs, SIGMETs, convective outlooks, and satellite imagery for active flights.</p>
        <p><strong>Strategic Value:</strong> The primary operational portal for pulling official pre-flight weather data and learning real-time weather monitoring.</p>
        <a class="resource-link" href="https://aviationweather.gov/" target="_blank">Aviation Weather Live →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#16: Bad Elf METAR/TAF Decoding Tool</div>
        <div class="card-subtitle">Strategic Value: Rapid Weather Code Literacy</div>
        <p><strong>Summary:</strong> A clean web tool that translates condensed, coded text weather statements into plain, easily understood descriptions.</p>
        <p><strong>Strategic Value:</strong> Speeds up weather literacy for beginners learning to decode critical variables like wind speed, ceiling heights, and pressure shifts.</p>
        <a class="resource-link" href="https://bad-elf.com/" target="_blank">Bad Elf Decoder →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#17: LiveATC.net Global Audio Network</div>
        <div class="card-subtitle">Strategic Value: Structural Phraseology Auditing</div>
        <p><strong>Summary:</strong> A network streaming live radio traffic from thousands of air traffic control facilities and towers worldwide.</p>
        <p><strong>Strategic Value:</strong> Helps students bridge the gap between textbook terms and real-world audio comprehension, improving listening habits early on.</p>
        <a class="resource-link" href="https://www.liveatc.net/" target="_blank">LiveATC Global Feeds →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#18: PlaneEnglish: ARSim Free Training Tier</div>
        <div class="card-subtitle">Strategic Value: Microphone Anxiety Reduction</div>
        <p><strong>Summary:</strong> A web-accessible version of an AI-driven sandbox that analyzes and scores radio phrases for rhythm, structure, and accuracy.</p>
        <p><strong>Strategic Value:</strong> Builds vocal muscle memory and reduces microphone anxiety through structured, interactive speaking exercises.</p>
        <a class="resource-link" href="https://planeenglishsim.com/" target="_blank">PlaneEnglish Classroom →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#19: FAA AIM Chapter 4: Air Traffic Control Procedures</div>
        <div class="card-subtitle">Strategic Value: Legal Procedures Framework</div>
        <p><strong>Summary:</strong> The regulatory chapter defining official communication standards, radar services, transponder use, and airport operations.</p>
        <p><strong>Strategic Value:</strong> Provides the legal guidelines for pilot-to-controller communications, establishing the rules of the road for public airspace.</p>
        <a class="resource-link" href="https://www.faa.gov/air_traffic/publications/atpubs/aim_html/" target="_blank">FAA Aeronautical Information Manual →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#20: NASA/Ames Aviation Safety Reporting System (ASRS)</div>
        <div class="card-subtitle">Strategic Value: Human-Error Case Studies</div>
        <p><strong>Summary:</strong> A voluntary, anonymous reporting database detailing real-world flight crew errors, unexpected weather encounters, and aircraft malfunctions.</p>
        <p><strong>Strategic Value:</strong> Allows students to study genuine, unfiltered human-error case studies to foster a culture focused on proactive safety management.</p>
        <a class="resource-link" href="https://asrs.arc.nasa.gov/" target="_blank">NASA ASRS System Database →</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 💰 Scholarships & Specialized Video Ground Schools")
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#21: AOPA High School Flight Training Scholarship Portal</div>
        <div class="card-subtitle">Strategic Value: Capital Burden Mitigation</div>
        <p><strong>Summary:</strong> An annual grant portal offering up to tens of thousands of dollars to high school students chasing primary private pilot certificates.</p>
        <p><strong>Strategic Value:</strong> Directly lowers financial hurdles for young aviators, making it a high-value link for early student users.</p>
        <a class="resource-link" href="https://www.aopa.org/training-and-safety/students/flight-training-scholarships" target="_blank">AOPA Scholarships →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#22: EAA Ray Aviation Scholarship Foundation Database</div>
        <div class="card-subtitle">Strategic Value: Fully Funded Training Loops</div>
        <p><strong>Summary:</strong> A funded grant system run through local experimental aircraft chapters that covers full flight training bills for local youths.</p>
        <p><strong>Strategic Value:</strong> Leverages regional flying clubs to provide mentoring alongside financial assistance, boosting student completion rates.</p>
        <a class="resource-link" href="https://www.eaa.org/eaa/youth/ray-aviation-scholarship" target="_blank">EAA Ray Scholarship Board →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#23: Free Pilot Training Online Ground Academy</div>
        <div class="card-subtitle">Strategic Value: Cost-Free Academic Completeness</div>
        <p><strong>Summary:</strong> Comprehensive, step-by-step video deep-dives going over the entire Private Pilot knowledge blueprint for zero cost.</p>
        <p><strong>Strategic Value:</strong> Offers an excellent free alternative to premium video courses, making ground school accessible to all students.</p>
        <a class="resource-link" href="https://www.youtube.com/c/FreePilotTraining" target="_blank">Free Pilot Training Network →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#24: The Finer Points: Professional Pilot Flight Training</div>
        <div class="card-subtitle">Strategic Value: Advanced Stick-and-Rudder Techniques</div>
        <p><strong>Summary:</strong> Educational videos focusing on flight deck organization, refined piloting techniques, stick-and-rudder feel, and safety tips.</p>
        <p><strong>Strategic Value:</strong> Helps students master flight skills faster through sharp, actionable tips from senior flight instructors.</p>
        <a class="resource-link" href="https://www.learnthefinerpoints.com/" target="_blank">The Finer Points Flight Resource →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#25: MzeroA Flight Training Free Resource Playlists</div>
        <div class="card-subtitle">Strategic Value: Checkride Oral Pass Optimization</div>
        <p><strong>Summary:</strong> Informative videos covering typical oral exam questions, checkride gotchas, and everyday safety procedures.</p>
        <p><strong>Strategic Value:</strong> Excellent for last-minute oral checkride prep, helping turn complex regulations into clear talking points.</p>
        <a class="resource-link" href="https://mzeroa.com/" target="_blank">MzeroA Online Platform →</a>
    </div>
    """, unsafe_allow_html=True)

# PAGE 3: ATC ROADMAP
elif st.session_state.page == "ATC":
    st.markdown("### 🎛️ Section 2: The Air Traffic Control Hub")
    st.markdown("#### 🥇 Virtual ATC Frameworks & Master Rules")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#1: VATSIM S1 Controller Training Syllabus</div>
        <div class="card-subtitle">Strategic Value: Early Ground Control Mastery</div>
        <p><strong>Summary:</strong> The fundamental gateway manual covering clearance formats, airport ground layouts, and taxi safety protocols.</p>
        <p><strong>Strategic Value:</strong> Ideal for teaching the basics of ground management before students move on to active radar sequencing.</p>
        <a class="resource-link" href="https://vatsim.net/" target="_blank">VATSIM United States Training Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#2: FAA Order JO 7110.65 (Air Traffic Control Manual)</div>
        <div class="card-subtitle">Strategic Value: The Absolute Regulatory Blueprint</div>
        <p><strong>Summary:</strong> The absolute legal handbook defining standard US phraseology, separation minimums, and vector guidelines.</p>
        <p><strong>Strategic Value:</strong> The definitive handbook for air traffic control, serving as the core reference source for any ATC training setup.</p>
        <a class="resource-link" href="https://www.faa.gov/air_traffic/publications/" target="_blank">FAA Document Gateway: JO 7110.65BB →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#3: IVAO ATC Online Academy Manuals</div>
        <div class="card-subtitle">Strategic Value: Global Procedures Onboarding</div>
        <p><strong>Summary:</strong> International training handbooks focusing on ICAO terminal rules, transition layer setups, and non-US vector standards.</p>
        <p><strong>Strategic Value:</strong> Provides essential global perspective, teaching students how air traffic control operates outside North America.</p>
        <a class="resource-link" href="https://ivao.aero/" target="_blank">IVAO HQ Training Academy →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#4: Eurocontrol Training Zone Portal</div>
        <div class="card-subtitle">Strategic Value: Multinational Airspace Optimization</div>
        <p><strong>Summary:</strong> Interactive training tracking air traffic flows, sector load balancing, and delay-reduction strategies across Europe.</p>
        <p><strong>Strategic Value:</strong> Introduces high-level airspace management concepts, showing how to handle traffic flows between different countries.</p>
        <a class="resource-link" href="https://www.eurocontrol.int/" target="_blank">Eurocontrol Aviation Training Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#5: EuroScope Radar Client Software Project</div>
        <div class="card-subtitle">Strategic Value: Desktop Radar Simulation Exercises</div>
        <p><strong>Summary:</strong> A highly detailed radar simulator client that replicates real-world European air traffic radar displays and tracker systems.</p>
        <p><strong>Strategic Value:</strong> Gives students hands-on practice with professional-grade radar tools from home without needing expensive academy equipment.</p>
        <a class="resource-link" href="https://www.euroscope.hu/" target="_blank">EuroScope Radar Engine →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#6: OpenRadar Open-Source Tower Tracking Software</div>
        <div class="card-subtitle">Strategic Value: Cost-Free Terminal Scope Operations</div>
        <p><strong>Summary:</strong> An open-source radar simulator focusing on terminal approach control and tower visual sweeps.</p>
        <p><strong>Strategic Value:</strong> Provides an accessible tool for students to practice managing traffic arcs and local terminal arrivals.</p>
        <a class="resource-link" href="https://sourceforge.net/" target="_blank">OpenRadar SourceForge Project →</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🛰️ Radar Vectoring Mechanics & Separation Rules")
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#7: ATC-Sim Browser Radar Vectoring Game</div>
        <div class="card-subtitle">Strategic Value: Practical Spatial Geometry Drills</div>
        <p><strong>Summary:</strong> A 2D browser simulator where players issue headings, altitudes, and speeds to feed arrivals onto final approach paths safely.</p>
        <p><strong>Strategic Value:</strong> A fast, interactive way to practice radar geometry and master vectoring techniques early in training.</p>
        <a class="resource-link" href="https://www.atc-sim.com/" target="_blank">ATC-Sim Browser Radar Engine →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#8: FAA Runway Incursion Prevention Training Simulator</div>
        <div class="card-subtitle">Strategic Value: Surface Movement Risk Mitigation</div>
        <p><strong>Summary:</strong> Interactive training tools designed to spot and prevent ground errors, runway incursions, and vehicle tracking mistakes.</p>
        <p><strong>Strategic Value:</strong> Focuses heavily on ground safety, teaching students how to keep runways clear and prevent close calls on the tarmac.</p>
        <a class="resource-link" href="https://www.faa.gov/airports/runway_safety" target="_blank">FAA Runway Safety Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#9: ICAO Document 4444 (Air Traffic Management Standards)</div>
        <div class="card-subtitle">Strategic Value: Global Treaty Alignment</div>
        <p><strong>Summary:</strong> The master international treaty text standardizing air traffic rules, flight rules, and separation criteria worldwide.</p>
        <p><strong>Strategic Value:</strong> The core reference for international air traffic control, vital for understanding global aviation standards.</p>
        <a class="resource-link" href="https://store.icao.int/" target="_blank">ICAO Store Official Reference Catalog →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#10: Standard Lateral and Vertical Separation Minimums Matrix</div>
        <div class="card-subtitle">Strategic Value: Structural Safety Target Enforcement</div>
        <p><strong>Summary:</strong> Quick-reference tables outlining legal distance limits (3 miles, 5 miles, or 1000 feet vertically) required between planes.</p>
        <p><strong>Strategic Value:</strong> Instills basic safety limits, helping controllers maintain legal margins and prevent separation violations.</p>
        <a class="resource-link" href="https://skybrary.aero/" target="_blank">SKYbrary Separation Standards →</a>
    </div>
    """, unsafe_allow_html=True)

# STANDALONE PLACEHOLDERS FOR REMAINING ORIGINAL PAGES
elif st.session_state.page in ["Crew", "Maintenance", "Drone", "AI"]:
    st.info(f"Welcome to the **{st.session_state.page}** Roadmap section module. Your content databases remain structurally live.")

# ==========================================
# 🌐 THE COMMUNITY & DYNAMIC PROFILE ENGINE
# ==========================================
elif st.session_state.page == "Community":
    st.markdown("### 🌐 AeroLaunch Community Base")
    
    # 🛠️ NICKNAME MODIFICATION & PROFILE EDIT FORM
    st.markdown("#### 🛠️ Edit Your Identity Profile")
    col1, col2 = st.columns([1, 4])
    
    with col1:
        user_avatar_current = get_avatar_url(current_nickname)
        st.image(user_avatar_current, caption="Your Personal Live Avatar", width=110)
        
    with col2:
        with st.form("modify_profile_form"):
            st.write(f"**System Handle ID:** `@{current_username}`")
            st.write(f"**Primary Email Vector:** `{users_data[current_username]['email']}`")
            changed_nickname = st.text_input("Change Your Display Nickname:", value=current_nickname)
            save_profile_btn = st.form_submit_button("Save Changes & Re-roll Avatar 💾")
            
            if save_profile_btn:
                if not changed_nickname.strip():
                    st.error("Nickname cannot be left blank.")
                else:
                    users_data[current_username]["name"] = changed_nickname.strip()
                    save_users(users_data)
                    st.session_state.user_display_name = changed_nickname.strip()
                    st.success("Identity vector updated successfully!")
                    st.rerun()

    st.markdown("---")
    
    # LIVE ACTIVE ROSTER GRID
    st.markdown("#### 👥 Live Active Community Directory")
    st.markdown("Every user's profile image changes in real time based on the letters typed into their nickname field.")
    
    all_current_users = load_users()
    grid_cols = st.columns(4)
    
    for index, (u_handle, u_info) in enumerate(all_current_users.items()):
        target_col = grid_cols[index % 4]
        with target_col:
            display_nick = u_info["name"]
            avatar_render_url = get_avatar_url(display_nick)
            
            st.markdown(f"""
            <div style="background-color: white; border: 1px solid #cbd5e1; border-radius: 10px; padding: 15px; text-align: center; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                <img src="{avatar_render_url}" width="65" style="border-radius: 50%; margin-bottom: 8px; border: 2px solid #1d4ed8; background-color: #f1f5f9;"><br>
                <strong style="color: #0f172a; font-size: 15px;">{display_nick}</strong><br>
                <span style="color: #64748b; font-size: 12px;">@{u_handle}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # GLOBAL LOUNGE BROADCAST FEED (CHAT AREA)
    st.markdown("#### 💬 Global Flight Deck Chat Lounge")
    
    def send_global_message(username, nickname, text):
        history = load_global_chat()
        new_msg = {
            "user": username,
            "nickname": nickname,
            "text": text,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        history.append(new_msg)
        with open(CHAT_DB, "w") as f:
            json.dump(history[-100:], f, indent=4)

    global_messages = load_global_chat()
    chat_container = st.container()
    
    with chat_container:
        if not global_messages:
            st.info("The chat lounge is currently quiet. Be the first to start the conversation!")
        else:
            for msg in global_messages:
                msg_nick = msg.get('nickname', msg['user'])
                msg_avatar = get_avatar_url(msg_nick)
                
                st.markdown(f"""
                <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 10px;">
                    <img src="{msg_avatar}" width="32" style="border-radius: 50%; background: #f1f5f9; border: 1px solid #cbd5e1; margin-top: 3px;">
                    <div>
                        <strong style="color: #1d4ed8;">{msg_nick}</strong> 
                        <span style="color: #64748b; font-size: 11px;">(@{msg['user']})</span> 
                        <span style="color: gray; font-size: 0.75rem;">({msg['timestamp']})</span><br>
                        <span style="font-size: 14px; color: #334155;">{msg['text']}</span>
                    </div>
                </div>
                <div style='margin-bottom: 8px; border-bottom: 1px dashed #e2e8f0;'></div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("community_chat_form", clear_on_submit=True):
        chat_text = st.text_input("Type your broadcast message:", placeholder="Say hello to the crew...")
        submit_chat = st.form_submit_button("Broadcast to Lounge 🛰️", type="primary")
        
        if submit_chat and chat_text.strip():
            send_global_message(current_username, current_nickname, chat_text.strip())
            st.rerun()
