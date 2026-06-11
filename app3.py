# ==========================================
# 1. CORE IMPORTS (MUST BE FIRST)
# ==========================================
import streamlit as st

# If you have a page config setup, put it right here too:
st.set_page_config(page_title="AeroLaunch", page_icon="✈️", layout="wide")


# ==========================================
# 🔐 AUTHENTICATION GATEWAY (SIGN-IN / LOG-IN)
# ==========================================

# Initialize authentication session state variables if they don't exist
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "login"

# CSS injection to style the login card seamlessly with your AeroLaunch UI
st.markdown("""
    <style>
    .auth-container {
        background-color: #f8fafc;
        padding: 2.5rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        max-width: 480px;
        margin: 2rem auto;
    }
    .auth-title {
        text-align: center;
        color: #1e3a8a;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .auth-subtitle {
        text-align: center;
        color: #64748b;
        margin-bottom: 2rem;
        font-size: 0.9rem;
    }
    .oauth-button {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: white;
        border: 1px solid #cbd5e1;
        padding: 0.6rem;
        border-radius: 8px;
        margin-bottom: 0.75rem;
        cursor: pointer;
        font-weight: 500;
        text-decoration: none;
        color: #334155;
        transition: background-color 0.2s;
    }
    .oauth-button:hover {
        background-color: #f1f5f9;
    }
    .divider {
        display: flex;
        align-items: center;
        text-align: center;
        color: #94a3b8;
        margin: 1.5rem 0;
    }
    .divider::before, .divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid #e2e8f0;
    }
    .divider:not(:empty)::before { margin-right: .5em; }
    .divider:not(:empty)::after { margin-left: .5em; }
    </style>
""", unsafe_allow_html=True)

# Render Authentication UI if user is not verified
if not st.session_state.logged_in:
    
    st.markdown("""
        <div style="background-color: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 1rem; text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #1d4ed8; font-family: sans-serif; margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px;">
                AeroLaunch <span style="font-size: 1.2rem; vertical-align: middle;"></span>
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.auth_mode == "login":
        st.markdown('<h2 class="auth-title">Welcome to AeroLaunch</h2>', unsafe_allow_html=True)
        st.markdown('<p class="auth-subtitle">Sign in to access your aviation roadmaps</p>', unsafe_allow_html=True)
        
        # OAuth Single Sign-On Buttons
        # Note: In production, these links point to your OAuth backend setup (e.g., Supabase, Firebase, or custom endpoints)
               
        email = st.text_input("Email Address", placeholder="name@domain.com")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Sign In →", use_container_width=True, type="primary"):
            if email and password: # Replace with your real DB credential check logic
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Please enter both email and password credentials.")
                
        st.markdown("---")
        if st.button("New to AeroLaunch? Create an account", use_container_width=True):
            st.session_state.auth_mode = "signup"
            st.rerun()

    else:
        st.markdown('<h2 class="auth-title">Create Account</h2>', unsafe_allow_html=True)
        st.markdown('<p class="auth-subtitle">Join the AeroLaunch aviation track</p>', unsafe_allow_html=True)
                
        new_name = st.text_input("Full Name", placeholder="Alex Mercer")
        new_email = st.text_input("Email Address", placeholder="name@domain.com")
        new_password = st.text_input("Password", type="password", placeholder="Create a strong password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Complete Registration 🎉", use_container_width=True, type="primary"):
            if new_name and new_email and new_password:
                st.success("Account created successfully!")
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Please complete all registration fields.")
                
        st.markdown("---")
        if st.button("Already have an account? Sign In", use_container_width=True):
            st.session_state.auth_mode = "login"
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop() # Prevents the rest of the application code from rendering until logged_in is True

# ==========================================
# END OF AUTHENTICATION COUPLING
# ==========================================

import streamlit as st

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
    /* Targeted clean typography */
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
    
    .app-header h1 {
        margin: 0; 
        color: #1d4ed8; 
        font-size: 38px; 
        font-weight: 800; 
        letter-spacing: -0.03em;
    }
    
    /* Crisp Pearl White Cards */
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
    
    /* Vibrant Contrast Titles */
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
st.markdown("""
<div class="app-header">
    <h1>AeroLaunch</h1>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION DECK ---
if "page" not in st.session_state:
    st.session_state.page = "Feed"

# Step 1: Force allocate exactly 8 clear slots in a grid row
nav_cols = st.columns(8)

# Step 2: Safely map all 8 buttons to slots 0 through 7
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
    if st.button("💁‍♀️ Crew Roadmap", use_container_width=True, type="primary" if st.session_state.page == "Crew" else "secondary"):
        st.session_state.page = "Crew"
        st.rerun()

with nav_cols[4]:
    if st.button("🔧 Maintenance", use_container_width=True, type="primary" if st.session_state.page == "Maintenance" else "secondary"):
        st.session_state.page = "Maintenance"
        st.rerun()

with nav_cols[5]:
    if st.button("🛸 Drone Logistics", use_container_width=True, type="primary" if st.session_state.page == "Drone" else "secondary"):
        st.session_state.page = "Drone"
        st.rerun()

with nav_cols[6]:
    if st.button("🤖 AeroBot AI", use_container_width=True, type="primary" if st.session_state.page == "AIChatbot" else "secondary"):
        st.session_state.page = "AIChatbot"
        st.rerun()

with nav_cols[7]:
    if st.button("🌐 Community", use_container_width=True, type="primary" if st.session_state.page == "Community" else "secondary"):
        st.session_state.page = "Community"
        st.rerun()

st.write("")

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

# PAGE 2: PILOT ROADMAP (THE PILOT HUB - TOP 25)
elif st.session_state.page == "Pilots":
    st.markdown("### ✈️ Section 1: The Pilot Hub")
    
    # Category 1
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

    # Category 2
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

    # Category 3
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

    # Category 4
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

# PAGE 3: ATC ROADMAP (THE AIR TRAFFIC CONTROL HUB - TOP 25)
elif st.session_state.page == "ATC":
    st.markdown("### 🎛️ Section 2: The Air Traffic Control Hub")
    
    # Category 1
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

    # Category 2
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

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#11: Wake Turbulence Category Separation Requirements</div>
        <div class="card-subtitle">Strategic Value: Structural Flow Management Safety</div>
        <p><strong>Summary:</strong> Tables outlining required distance buffers behind heavy jets to prevent light planes from hitting dangerous wingtip vortices.</p>
        <p><strong>Strategic Value:</strong> Critical for avoiding wake turbulence accidents, helping controllers space departures safely based on weight class.</p>
        <a class="resource-link" href="https://www.faa.gov/" target="_blank">FAA Wake Turbulence Mitigation Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#12: Intercept Angle Mathematics for Instrument Approaches</div>
        <div class="card-subtitle">Strategic Value: Approach Glidepath Entry Optimization</div>
        <p><strong>Summary:</strong> Guides outlining how to turn planes onto instrument final approaches (30-degree maximum limits) without overshooting the line.</p>
        <p><strong>Strategic Value:</strong> Sharpens mental math skills, helping controllers issue smooth turns that align pilots perfectly with instrument approach paths.</p>
        <a class="resource-link" href="https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/instrument_procedures_handbook" target="_blank">FAA Instrument Procedures Handbook →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 3
    st.markdown("#### 🎙️ Tower Operations & Airspace Infrastructure")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#13: FAA Airport Sign and Marking Guide</div>
        <div class="card-subtitle">Strategic Value: Local Airfield Visual Awareness</div>
        <p><strong>Summary:</strong> Visual reference guides illustrating runway hold lines, taxi signs, direction indicators, and displaced threshold markers.</p>
        <p><strong>Strategic Value:</strong> Essential for tower operators, helping them guide pilots accurately through complex airport layouts.</p>
        <a class="resource-link" href="https://www.faa.gov/airports/runway_safety/publications" target="_blank">FAA Runway Safety Sign Manual →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#14: Land and Hold Short Operations (LAHSO) Safety Limits</div>
        <div class="card-subtitle">Strategic Value: Advanced Capacity Engineering</div>
        <p><strong>Summary:</strong> Operating parameters for landing planes on intersecting runways and stopping them before the crossing point.</p>
        <p><strong>Strategic Value:</strong> Increases airport capacity during peak hours while keeping strict safety margins between crossing aircraft.</p>
        <a class="resource-link" href="https://www.faa.gov/" target="_blank">FAA LAHSO Directives Matrix →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#15: Airspace Classifications Dimensional Metric Matrix</div>
        <div class="card-subtitle">Strategic Value: Regulatory Boundaries Identification</div>
        <p><strong>Summary:</strong> Dimensional charts illustrating the vertical and lateral boundaries of Class A, B, C, D, E, and G airspaces.</p>
        <p><strong>Strategic Value:</strong> Provides the basic framework for airspace rules, defining when flights must establish contact with controllers.</p>
        <a class="resource-link" href="https://www.faa.gov/" target="_blank">FAA Airspace Classification Hub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#16: Standard Terminal Arrival Route (STAR) Chart Profiles</div>
        <div class="card-subtitle">Strategic Value: Arrival Sequence Profiling Efficiency</div>
        <p><strong>Summary:</strong> Standard instrument arrival charts detailing predefined routes, speed limits, and altitude restrictions for incoming jets.</p>
        <p><strong>Strategic Value:</strong> Streamlines approach control workloads by automatically organizing arrivals onto standard terminal paths.</p>
        <a class="resource-link" href="https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/" target="_blank">FAA Terminal Procedures Publication (d-TPP) →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#17: Holding Pattern Entry Geometric Calculation Worksheets</div>
        <div class="card-subtitle">Strategic Value: Traffic Delay Sequencing Control</div>
        <p><strong>Summary:</strong> Math guides detailing direct, parallel, and teardrop entry profiles for holding patterns based on arrival angles.</p>
        <p><strong>Strategic Value:</strong> Essential for managing traffic delays, helping controllers predict airframe paths during holding adjustments.</p>
        <a class="resource-link" href="https://www.andreasnotebook.com/" target="_blank">CFI Notebook Holding Procedures →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#18: Reduced Vertical Separation Minimum (RVSM) Flight Levels</div>
        <div class="card-subtitle">Strategic Value: High-Altitude Route Capacity Engineering</div>
        <p><strong>Summary:</strong> Rules reducing standard vertical spacing from 2000 feet to 1000 feet for advanced aircraft flying between FL290 and FL410.</p>
        <p><strong>Strategic Value:</strong> Doubles high-altitude airspace capacity, making it vital for modern enroute sequencing training.</p>
        <a class="resource-link" href="https://www.faa.gov/air_traffic/separation/rvsm" target="_blank">FAA RVSM Documentation Portal →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 4
    st.markdown("#### 🧠 Aptitude Testing & Emergency Scenarios")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#19: ATSA Air Traffic Selection Assessment Prep Guide</div>
        <div class="card-subtitle">Strategic Value: Federal Screening Evaluation Preparedness</div>
        <p><strong>Summary:</strong> Official overviews explaining the structure, sections, and passing scores required for the FAA's entry-level controller aptitude test.</p>
        <p><strong>Strategic Value:</strong> Critical starting point for aspiring controllers, showing them what to expect before taking official entry tests.</p>
        <a class="resource-link" href="https://www.faa.gov/be-atc" target="_blank">FAA ATC Career Hiring Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#20: JobTestPrep ATSA Free Practice Modules</div>
        <div class="card-subtitle">Strategic Value: Dynamic Interactive Testing Calibration</div>
        <p><strong>Summary:</strong> Sample math games and interactive puzzles testing a user's ability to clear intersecting conflicts under tight time limits.</p>
        <p><strong>Strategic Value:</strong> Sharpens early decision-making habits, helping candidates improve their reaction times for the official ATSA test.</p>
        <a class="resource-link" href="https://www.jobtestprep.com/" target="_blank">JobTestPrep ATSA Free Practice Modules →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#21: Transponder Squawk Code Matrix (7500, 7600, 7700)</div>
        <div class="card-subtitle">Strategic Value: Silent Risk Vector Identification</div>
        <p><strong>Summary:</strong> A quick-reference sheet for emergency transponder codes: 7500 (Hijack), 7600 (Radio Failure), and 7700 (General Emergency).</p>
        <p><strong>Strategic Value:</strong> Allows controllers to instantly identify flight emergencies on radar screens without needing verbal radio contact.</p>
        <a class="resource-link" href="https://www.aopa.org/" target="_blank">AOPA Transponder Squawk Guidelines →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#22: FAA Light Gun Signals Reference Chart</div>
        <div class="card-subtitle">Strategic Value: Fail-Safe Visual Backups Execution</div>
        <p><strong>Summary:</strong> Procedures for using airport light guns and tracking predictable pilot paths when a flight loses all radio contact.</p>
        <p><strong>Strategic Value:</strong> Keeps traffic flowing safely during radio outages by providing a reliable backup communication method.</p>
        <a class="resource-link" href="https://www.faa.gov/" target="_blank">FAA Light Gun Signals Reference Chart →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 5
    st.markdown("#### 📊 Historical Case Studies & Safety Logs")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#23: Tenerife Airport Disaster Systemic Breakdown Analysis</div>
        <div class="card-subtitle">Strategic Value: Master Phraseology Safety Standard</div>
        <p><strong>Summary:</strong> A safety review of the 1977 runway collision, highlighting how vague phrasing, radio blockages, and stress led to error.</p>
        <p><strong>Strategic Value:</strong> The premier lesson on radio safety, showing why the industry shifted to strict, unambiguous phraseology.</p>
        <a class="resource-link" href="https://skybrary.aero/articles/tenerife-airport-disaster-1977" target="_blank">SKYbrary Tenerife Collision Analysis →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#24: Uberlingen Mid-Air Collision TCAS Priority Study</div>
        <div class="card-subtitle">Strategic Value: Dynamic Cockpit Automation Logic Priority</div>
        <p><strong>Summary:</strong> An analysis of a mid-air crash caused when a controller's vectors directly contradicted automated onboard collision alerts (TCAS).</p>
        <p><strong>Strategic Value:</strong> Teaches critical system priorities, establishing that automated cockpit warnings always override ground instructions during alerts.</p>
        <a class="resource-link" href="https://skybrary.aero/" target="_blank">SKYbrary Uberlingen Structural Safety Review →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#25: Flight Safety Foundation: Continuous ATC Integrity Reports</div>
        <div class="card-subtitle">Strategic Value: Active Real-World Systemic Risk Monitoring</div>
        <p><strong>Summary:</strong> Regular safety reports tracking modern near-miss statistics, systemic software glitches, and controller fatigue risks.</p>
        <p><strong>Strategic Value:</strong> Keeps curriculum content up to date with modern safety trends and active systemic air traffic risks.</p>
        <a class="resource-link" href="https://flightsafety.org/" target="_blank">Flight Safety Foundation Safety Digest Logs →</a>
    </div>
    """, unsafe_allow_html=True)

# PAGE 4: CREW ROADMAP (THE FLIGHT ATTENDANT HUB - TOP 25)
elif st.session_state.page == "Crew":
    st.markdown("### 💁‍♀️ Section 3: Flight Attendant / Air Hostess Hub")
    
    # Category 1
    st.markdown("#### 🥇 Cabin Safety Protocols & Emergency Command")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#1: ICAO Cabin Safety Training Manual (Doc 10002)</div>
        <div class="card-subtitle">Strategic Value: Global Safety Criteria Alignment</div>
        <p><strong>Summary:</strong> The global master manual detailing emergency commands, slide use, raft parameters, and survival gear layouts.</p>
        <p><strong>Strategic Value:</strong> The primary textbook for cabin safety, ensuring student training meets international airline criteria.</p>
        <a class="resource-link" href="https://store.icao.int/" target="_blank">ICAO Store Official Reference Catalog →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#2: FAA Advisory Circular 121-24C (Passenger Safety Briefings)</div>
        <div class="card-subtitle">Strategic Value: Legal Briefing Compliance</div>
        <p><strong>Summary:</strong> Legal standards detailing what must be included in passenger briefings and exit row instructions.</p>
        <p><strong>Strategic Value:</strong> Ensures cabin safety presentations meet all legal criteria, preparing crews to handle safety checks confidently.</p>
        <a class="resource-link" href="https://www.faa.gov/regulations_policies/advisory_circulars/" target="_blank">FAA Advisory Circular Repository →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#3: Skybrary Cabin Safety Compendium</div>
        <div class="card-subtitle">Strategic Value: Dynamic Workflow Reference</div>
        <p><strong>Summary:</strong> An open aviation safety database cataloging best responses for severe turbulence, cabin smoke, and sudden decompressions.</p>
        <p><strong>Strategic Value:</strong> Provides an excellent reference source for building practical cabin safety guides and response workflows.</p>
        <a class="resource-link" href="https://skybrary.aero/" target="_blank">SKYbrary Cabin Safety Gateway →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#4: Aircraft Emergency Evacuation Slide System Mechanics</div>
        <div class="card-subtitle">Strategic Value: Operational Door Safety</div>
        <p><strong>Summary:</strong> Technical overviews detailing door slide arming, pressure checks, and deployment triggers for various exit doors.</p>
        <p><strong>Strategic Value:</strong> Eliminates door operation errors, ensuring slides are armed correctly for flight and disarmed safely for arrival.</p>
        <a class="resource-link" href="https://skybrary.aero/" target="_blank">SKYbrary Emergency Evacuation Slides →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#5: IATA Dangerous Goods Regulations (DGR) Quick Reference</div>
        <div class="card-subtitle">Strategic Value: Cabin Risk Hazard Neutralization</div>
        <p><strong>Summary:</strong> Identification charts showing restricted items, lithium battery fire hazards, and spill control steps for cabins.</p>
        <p><strong>Strategic Value:</strong> Helps crews spot and neutralize hidden hazardous materials in carry-on bags before departure.</p>
        <a class="resource-link" href="https://www.iata.org/" target="_blank">IATA Dangerous Goods Documentation →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 2
    st.markdown("#### 💼 Recruitment, Resumes & Interview Prep")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#6: Canva Flight Attendant Resume Layout Templates</div>
        <div class="card-subtitle">Strategic Value: Resume Presentation Optimization</div>
        <p><strong>Summary:</strong> Visual, professional resume layouts tailored to highlight customer service skills and safety certifications for airline applications.</p>
        <p><strong>Strategic Value:</strong> Helps candidates format their experience clearly, matching the visual styles preferred by airline hiring teams.</p>
        <a class="resource-link" href="https://www.canva.com/" target="_blank">Canva Professional Flight Attendant Templates →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#7: Indeed Career Guide: Flight Attendant Interview Steps</div>
        <div class="card-subtitle">Strategic Value: STAR Formatted Interview Preparation</div>
        <p><strong>Summary:</strong> Behavioral interview questions structured around Situation, Task, Action, and Result (STAR) formats used by airlines during recruitment.</p>
        <p><strong>Strategic Value:</strong> Prepares applicants to give structured, professional answers that demonstrate real-world problem-solving skills.</p>
        <a class="resource-link" href="https://www.indeed.com/" target="_blank">Indeed Career Guide: Flight Attendant Interview Steps →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#8: Verbal De-escalation Techniques for Confined Spaces</div>
        <div class="card-subtitle">Strategic Value: Conflict Threat Resolution</div>
        <p><strong>Summary:</strong> Practical guides on diffusing passenger arguments, calming upset travelers, and resolving seating disputes peacefully.</p>
        <p><strong>Strategic Value:</strong> Gives crew members the communication skills needed to handle arguments before they escalate into serious safety risks.</p>
        <a class="resource-link" href="https://skybrary.aero/" target="_blank">SKYbrary Managing Disruptive Passengers →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#9: Public Announcement (PA) Reading Script Database</div>
        <div class="card-subtitle">Strategic Value: Professional Vocal Clarity Drills</div>
        <p><strong>Summary:</strong> Practice scripts covering welcome messages, turbulence warnings, and customs instructions to practice clear speaking habits.</p>
        <p><strong>Strategic Value:</strong> Improves vocal tone and clarity, helping crews deliver clear, professional announcements under pressure.</p>
        <a class="resource-link" href="https://www.flightattendantcentral.com/" target="_blank">Flight Attendant PA Scripts Directory →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#10: DOT Airline Accessibility Guidelines</div>
        <div class="card-subtitle">Strategic Value: Empathetic Compliance Framework</div>
        <p><strong>Summary:</strong> Regulatory service guides showing how to assist solo young travelers, elderly passengers, and disabled flyers safely.</p>
        <p><strong>Strategic Value:</strong> Ensures full compliance with passenger accessibility rules, providing professional, empathetic care for every flyer.</p>
        <a class="resource-link" href="https://www.transportation.gov/" target="_blank">DOT Airline Accessibility Guidelines →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 3
    st.markdown("#### 🍽️ Catering Logic & Galley Management")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#11: IATA Special Meal (SPML) Universal Code Matrix</div>
        <div class="card-subtitle">Strategic Value: Catering Distribution Accuracy</div>
        <p><strong>Summary:</strong> Standardized codes used to identify special passenger meals, including vegan, kosher, halal, and allergen-free options.</p>
        <p><strong>Strategic Value:</strong> Prevents catering mix-ups, helping crews distribute specialized meals accurately to the right passengers.</p>
        <a class="resource-link" href="https://www.iata.org/" target="_blank">IATA Passenger Special Meal Specifications →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#12: Widebody Aircraft Galley Latches & Safety Standards</div>
        <div class="card-subtitle">Strategic Value: Mechanical Lockdown Securing</div>
        <p><strong>Summary:</strong> Operating guides for locking meal carts, latching galley doors, and securing electrical ovens before take-off.</p>
        <p><strong>Strategic Value:</strong> Prevents cart rollaways and injury risks by ensuring all galley gear is locked down tight during turbulence.</p>
        <a class="resource-link" href="https://skybrary.aero/" target="_blank">SKYbrary Galley Safety Standards →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#13: FDA Retail & Food Service Regulation Logs</div>
        <div class="card-subtitle">Strategic Value: Consumable Temperature Safety</div>
        <p><strong>Summary:</strong> Health guidelines defining safe temperature ranges for holding and serving prepared meals on commercial routes.</p>
        <p><strong>Strategic Value:</strong> Prevents food spoilage, ensuring all passenger meals remain safe and healthy throughout long journeys.</p>
        <a class="resource-link" href="https://www.fda.gov/" target="_blank">FDA Retail & Food Service Regulation Logs →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#14: IATA Aircraft Cabin Waste Reduction Portal</div>
        <div class="card-subtitle">Strategic Value: Bio-Waste Hub Disposal Regulatory Compliance</div>
        <p><strong>Summary:</strong> International rules covering cabin sorting, recycling, and disposing of international bio-waste upon arrival.</p>
        <p><strong>Strategic Value:</strong> Helps airlines comply with green target goals and international garbage disposal rules at global hubs.</p>
        <a class="resource-link" href="https://www.iata.org/" target="_blank">IATA Aircraft Cabin Waste Reduction Portal →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 4
    st.markdown("#### 🌐 IATA Geography & Flight Wellness")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#15: IATA Official Coding Engine Search</div>
        <div class="card-subtitle">Strategic Value: Core Airport Coding Literacy</div>
        <p><strong>Summary:</strong> Search tools and reference guides designed to help students master three-letter city codes like JFK, LHR, and DXB.</p>
        <p><strong>Strategic Value:</strong> Fundamental skill that prevents luggage routing mistakes and speeds up check-in logistics.</p>
        <a class="resource-link" href="https://www.iata.org/en/publications/directories/code-search/" target="_blank">IATA Official Coding Engine Search →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#16: TimeAndDate Global Zone Converter Maps</div>
        <div class="card-subtitle">Strategic Value: Log Tracking & Rest Optimization</div>
        <p><strong>Summary:</strong> Time zone charts showing how to calculate local arrival times and track day changes when crossing the International Date Line.</p>
        <p><strong>Strategic Value:</strong> Helps crews manage flight logs accurately and schedule rest blocks properly on long multi-stop trips.</p>
        <a class="resource-link" href="https://www.timeanddate.com/" target="_blank">TimeAndDate Global Zone Converter Maps →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#17: IATA Travel Centre Passport and Visa Requirements</div>
        <div class="card-subtitle">Strategic Value: International Border Clearance Processing</div>
        <p><strong>Summary:</strong> Border rules showing passport validity requirements, mandatory visas, and crew entry rules for different countries.</p>
        <p><strong>Strategic Value:</strong> Helps crews cross international borders smoothly, avoiding customs issues or entry delays during layovers.</p>
        <a class="resource-link" href="https://www.iatatravelcentre.com/" target="_blank">IATA Travel Centre Passport and Visa Requirements →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#18: Sterile Flight Deck Rule Operational Compliance</div>
        <div class="card-subtitle">Strategic Value: Critical Focus Isolation</div>
        <p><strong>Summary:</strong> Regulations banning all non-safety communications with the cockpit during low-altitude taxiing, takeoffs, and landings.</p>
        <p><strong>Strategic Value:</strong> Prevents pilot distractions during critical phases of flight, ensuring the flight deck stays completely focused on safety.</p>
        <a class="resource-link" href="https://www.faa.gov/" target="_blank">FAA Advisory Circular AC 121-32: Sterile Flight Deck →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#19: ICAO Fatigue Risk Management Portal</div>
        <div class="card-subtitle">Strategic Value: Exhaustion Management Calibration</div>
        <p><strong>Summary:</strong> System tracking sheets outlining legal duty limits, minimum rest breaks, and fatigue reporting tools for international crews.</p>
        <p><strong>Strategic Value:</strong> Prevents extreme exhaustion risks by ensuring airline schedules comply with legal safety rest margins.</p>
        <a class="resource-link" href="https://www.icao.int/" target="_blank">ICAO Fatigue Risk Management Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#20: CDC Traveler's Health Blood Clots Guide</div>
        <div class="card-subtitle">Strategic Value: Long-Haul Physiological Protection</div>
        <p><strong>Summary:</strong> Leg movement guides and compression advice designed to maintain good blood flow on long-haul segments to prevent DVT.</p>
        <p><strong>Strategic Value:</strong> Lowers blood clot risks from long sitting times, keeping crews safe and healthy across extended flights.</p>
        <a class="resource-link" href="https://wwwnc.cdc.gov/travel" target="_blank">CDC Traveler's Health Blood Clots Guide →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 5
    st.markdown("#### 🏥 High-Altitude Medicine & Crash Case Studies")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#21: Aerospace Medical Association (AsMA) Publications</div>
        <div class="card-subtitle">Strategic Value: High-Altitude Crisis Management</div>
        <p><strong>Summary:</strong> Clinical reference manuals tracking altitude strains on wounds, heart issues, asthma attacks, and stroke symptoms in pressurized cabins.</p>
        <p><strong>Strategic Value:</strong> Gives crews the medical knowledge needed to treat serious health crises effectively at high cruise altitudes.</p>
        <a class="resource-link" href="https://www.asma.org/" target="_blank">Aerospace Medical Association (AsMA) Publications →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#22: British Airtours Flight 28M Evacuation Analysis</div>
        <div class="card-subtitle">Strategic Value: Structural Cabin Path Optimization</div>
        <p><strong>Summary:</strong> A safety review of a 1985 engine fire that caused smoke to quickly fill the cabin, slowing down passenger evacuation steps.</p>
        <p><strong>Strategic Value:</strong> Drove major updates in interior safety design, leading to wider exit row paths, clear floor lighting, and fire-resistant seat covers.</p>
        <a class="resource-link" href="https://www.gov.uk/government/organisations/air-accidents-investigation-branch" target="_blank">UK AAIB Historical Accident Investigation Vault →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#23: Air Canada Flight 797 Technical Evaluation Archive</div>
        <div class="card-subtitle">Strategic Value: Automated Fire Protection Standards</div>
        <p><strong>Summary:</strong> A study of a hidden bathroom fire that spread through wall panels, knocking out power and filling the cabin with thick smoke.</p>
        <p><strong>Strategic Value:</strong> Drove major cabin updates, making lavatory smoke alarms, automatic extinguishers, and path lights mandatory on all planes.</p>
        <a class="resource-link" href="https://www.ntsb.gov/" target="_blank">NTSB Air Canada 797 Technical Evaluation Archive →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#24: US Airways Flight 1549 Hudson River Ditching Evacuation</div>
        <div class="card-subtitle">Strategic Value: Command Loop Drills Validation</div>
        <p><strong>Summary:</strong> A review of a dual-engine bird strike ditching, showing how fast, orderly cabin teams emptied the plane onto river rafts.</p>
        <p><strong>Strategic Value:</strong> Proves the value of structured training drills, illustrating how perfect command loops make fast water evacuations possible.</p>
        <a class="resource-link" href="https://www.ntsb.gov/" target="_blank">NTSB Hudson Ditching Operational Review →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#25: Flight Safety Foundation Cabin Crew Safety Digests</div>
        <div class="card-subtitle">Strategic Value: Modern Cabin Asset Modernization Tracking</div>
        <p><strong>Summary:</strong> A compilation of modern safety briefings tracking exit injuries, galley cart hazards, and changing cabin equipment standards.</p>
        <p><strong>Strategic Value:</strong> Keeps safety training fresh, ensuring crew knowledge aligns with modern airline safety updates and research.</p>
        <a class="resource-link" href="https://flightsafety.org/" target="_blank">Flight Safety Foundation Cabin Crew Safety Digests →</a>
    </div>
    """, unsafe_allow_html=True)

# PAGE 5: MAINTENANCE (AIRCRAFT MAINTENANCE & ENGINEERING (AMT) HUB - TOP 25)
elif st.session_state.page == "Maintenance":
    st.markdown("### 🔧 🛠️ Section 4: Aircraft Maintenance & Engineering (AMT) Hub")
    
    # Category 1
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#1: FAA Aviation Handbooks & Manuals (General, Airframe, & Powerplant)</div>
        <div class="card-subtitle">Strategic Value: Core Structural Reading Bedrock</div>
        <p><strong>Summary:</strong> The core technical textbooks covering aerodynamics, structural sheet metal, and turbine engine mechanics.</p>
        <p><strong>Strategic Value:</strong> Forms the foundational reading material for anyone learning aircraft maintenance and structural engineering.</p>
        <a class="resource-link" href="https://www.faa.gov/regulations_policies/handbooks_manuals/aviation" target="_blank">FAA Handbooks Gateway →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#2: EAA AeroEducate Portal</div>
        <div class="card-subtitle">Strategic Value: Youth STEM Activity Tracking</div>
        <p><strong>Summary:</strong> An interactive, youth-focused STEM tracking system designed to log hands-on engineering activities.</p>
        <p><strong>Strategic Value:</strong> Connects high schoolers to local manufacturing projects and youth engineering mentors.</p>
        <a class="resource-link" href="https://www.aeroeducate.org/" target="_blank">EAA AeroEducate →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#3: Aircraft Electronics Association (AEA) Educational Foundation</div>
        <div class="card-subtitle">Strategic Value: Avionics Capital Cost Mitigation</div>
        <p><strong>Summary:</strong> A dedicated association platform providing thousands of dollars in scholarships explicitly for high schoolers.</p>
        <p><strong>Strategic Value:</strong> Directly offsets the cost of avionics, wiring, and electronics training programs for teens.</p>
        <a class="resource-link" href="https://aea.net/foundation/" target="_blank">AEA Foundation Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#4: SkillsUSA Aviation Maintenance Trades</div>
        <div class="card-subtitle">Strategic Value: Teenage Technical Skills Competition</div>
        <p><strong>Summary:</strong> A structured workforce program providing technical framework guidelines and competitive events for student mechanics.</p>
        <p><strong>Strategic Value:</strong> Allows 16-year-olds to compete in high school divisions for precision assembly and safety wiring.</p>
        <a class="resource-link" href="https://www.skillsusa.org/" target="_blank">SkillsUSA Main Site →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#5: FAA Safety Team (FAASTeam) Learning Center</div>
        <div class="card-subtitle">Strategic Value: Industry Resume Credentialing</div>
        <p><strong>Summary:</strong> The official safety portal hosting hundreds of free courses on human error, tool management, and parts inspections.</p>
        <p><strong>Strategic Value:</strong> Earns teens official industry safety certificates to boost their resumes before turning 18.</p>
        <a class="resource-link" href="https://www.faasafety.gov/" target="_blank">FAASTeam Online →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 2
    st.markdown("#### 🔩 Core Technical & Industry Resources")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#6: Aviation Mechanic Practical Test Standards (PTS)</div>
        <div class="card-subtitle">Strategic Value: Practical Certification Standard Blueprint</div>
        <p><strong>Summary:</strong> The official testing blueprint detailing the exact practical projects required to clear a mechanic license.</p>
        <p><strong>Strategic Value:</strong> Provides the direct grading criteria for passing hands-on oral and practical technician exams.</p>
        <a class="resource-link" href="https://www.faa.gov/training_testing/testing/pts" target="_blank">FAA Testing Library →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#7: Dynamic Regulatory System (DRS)</div>
        <div class="card-subtitle">Strategic Value: Airworthiness Directive Direct Auditing</div>
        <p><strong>Summary:</strong> The FAA’s central legal search engine for standard airworthiness certificates, directives, and component limits.</p>
        <p><strong>Strategic Value:</strong> Introduces students to regulatory maintenance law and how to research mandatory aircraft safety recalls.</p>
        <a class="resource-link" href="https://drs.faa.gov/" target="_blank">FAA DRS System →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#8: Aviation Maintenance Magazine</div>
        <div class="card-subtitle">Strategic Value: Commercial Sector Trends Tracking</div>
        <p><strong>Summary:</strong> A professional trade journal covering automated tooling, composites, and global fleet overhaul trends.</p>
        <p><strong>Strategic Value:</strong> Keeps students updated on commercial MRO (Maintenance, Repair, and Overhaul) corporate operations.</p>
        <a class="resource-link" href="https://www.aviationmaintenance.edu/" target="_blank">AMTSociety News →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#9: National Aviation Academy (NAA) Training Blog</div>
        <div class="card-subtitle">Strategic Value: Hangar Lifecycle Operational Insight</div>
        <p><strong>Summary:</strong> Informative visual breakdowns showing daily life inside turbine maintenance hangars and tool control stations.</p>
        <p><strong>Strategic Value:</strong> Helps teens visualize the daily career workflow of an active heavy-jet maintenance technician.</p>
        <a class="resource-link" href="https://www.naa.edu/" target="_blank">NAA Training Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#10: AMT Society Knowledge Center</div>
        <div class="card-subtitle">Strategic Value: Peer-Vetted Craft Perfection</div>
        <p><strong>Summary:</strong> A professional forum network detailing industry standard practices for safety wire patterns and sheet metal rivets.</p>
        <p><strong>Strategic Value:</strong> Serves as a peer-vetted knowledge base for perfecting physical trade craft skills.</p>
        <a class="resource-link" href="https://www.aviationmaintenance.edu/" target="_blank">AMTSociety Hub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#11: Aircraft Component Type Certificate Data Sheets (TCDS)</div>
        <div class="card-subtitle">Strategic Value: Operational Modifications Legality Verification</div>
        <p><strong>Summary:</strong> The official weight, fuel, and engine limit sheets used to certify exact aircraft build specifications.</p>
        <p><strong>Strategic Value:</strong> Vital for teaching students how to verify if an aircraft modification is legally airworthy.</p>
        <a class="resource-link" href="https://www.faa.gov/aircraft/safety/certs/tdsn" target="_blank">FAA TCDS Database →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#12: Electronic Code of Federal Regulations (eCFR) Part 43</div>
        <div class="card-subtitle">Strategic Value: Structural Regulatory Limitations Identification</div>
        <p><strong>Summary:</strong> The baseline federal law defining what constitutes legal maintenance, rebuild alterations, and preventive tasks.</p>
        <p><strong>Strategic Value:</strong> Gives 16-year-olds a clear understanding of what basic fixes a private pilot can legally perform themselves.</p>
        <a class="resource-link" href="https://www.ecfr.gov/" target="_blank">eCFR Part 43 Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#13: Aircraft Electronics Association Avionics Magazine</div>
        <div class="card-subtitle">Strategic Value: Next-Gen System Hardware Tracking</div>
        <p><strong>Summary:</strong> Tech tracking articles breaking down modern glass cockpits, wiring setups, and digital radar components.</p>
        <p><strong>Strategic Value:</strong> Focuses heavily on the electrical and computational side of modern avionics engineering.</p>
        <a class="resource-link" href="https://aea.net/avionicsnews/" target="_blank">AEA Avionics News →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#14: Choose Aerospace Curriculum Network</div>
        <div class="card-subtitle">Strategic Value: Secondary Education Program Architecture</div>
        <p><strong>Summary:</strong> A dedicated high school training network framework providing direct entry paths into certified mechanic academies.</p>
        <p><strong>Strategic Value:</strong> Helps high schools incorporate standardized aviation maintenance classes directly into teenage class schedules.</p>
        <a class="resource-link" href="https://www.chooseaerospace.org/" target="_blank">Choose Aerospace →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#15: Northrop Rice Aviation Foundation Grants</div>
        <div class="card-subtitle">Strategic Value: Entry Equipment Capital Allocation</div>
        <p><strong>Summary:</strong> A funding system offering specialized tool grants and avionic system scholarships for student technicians.</p>
        <p><strong>Strategic Value:</strong> Helps students buy expensive starting toolsets required for entry-level hangar apprenticeships.</p>
        <a class="resource-link" href="http://www.nrafoundation.org/" target="_blank">NRAF Foundation →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#16: Boeing Technical Apprenticeship Program</div>
        <div class="card-subtitle">Strategic Value: Alternative Workforce Entry Fast-Tracking</div>
        <p><strong>Summary:</strong> Corporate outreach pathways showing how high school graduates step directly into assembly line careers.</p>
        <p><strong>Strategic Value:</strong> Provides an actionable alternative to a traditional 4-year degree via direct aerospace manufacturer training.</p>
        <a class="resource-link" href="https://jobs.boeing.com/" target="_blank">Boeing Careers Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#17: AOPA AMT Career Guide</div>
        <div class="card-subtitle">Strategic Value: Fleet Domain Segment Planning</div>
        <p><strong>Summary:</strong> A comprehensive breakdown showing the intersection of general aviation maintenance and commercial airline operations.</p>
        <p><strong>Strategic Value:</strong> Helps students choose between working on small flight-school trainers or massive commercial airliners.</p>
        <a class="resource-link" href="https://www.aopa.org/" target="_blank">AOPA Mechanic Paths →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#18: Aviation Maintenance Technician Society Awards</div>
        <div class="card-subtitle">Strategic Value: Lifetime Learning Credit Tracking</div>
        <p><strong>Summary:</strong> A specialized rewards program that logs continuous training milestones for apprentice technicians.</p>
        <p><strong>Strategic Value:</strong> Encourages a culture of lifelong learning by tracking voluntary safety training credits.</p>
        <a class="resource-link" href="https://www.faa.gov/mechanics/aviation_mechanic_awards" target="_blank">FAA William O'Brien Program →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#19: Engine Components Inc. (ECI) Technical Library</div>
        <div class="card-subtitle">Strategic Value: Dynamic Piston Internal Mechanics Clarity</div>
        <p><strong>Summary:</strong> Free graphic heavy manuals tracking piston engine wear, cylinder rebuilding, and piston clearances.</p>
        <p><strong>Strategic Value:</strong> Excellent visual resource for understanding how internal combustion aircraft engines operate.</p>
        <a class="resource-link" href="https://www.asoverhaul.com/" target="_blank">ECI Component Guides →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#20: Aviation Institute of Maintenance (AIM) High School Hub</div>
        <div class="card-subtitle">Strategic Value: Early License Academic Acceleration</div>
        <p><strong>Summary:</strong> Offers dual-enrollment class tracking and summer camp options for 16-year-olds exploring technical trades.</p>
        <p><strong>Strategic Value:</strong> Allows high school juniors to earn college credits toward an airframe license early.</p>
        <a class="resource-link" href="https://aviationmaintenance.edu/" target="_blank">AIM Aviation Hangar →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#21: Aircraft Mechanics Fraternal Association (AMFA) Education</div>
        <div class="card-subtitle">Strategic Value: Active Network Mentorship Connection</div>
        <p><strong>Summary:</strong> Trade union portal providing student mentoring connections with active airline line maintenance mechanics.</p>
        <p><strong>Strategic Value:</strong> Connects student technicians with industry professionals to build career networks.</p>
        <a class="resource-link" href="https://www.amfanational.org/" target="_blank">AMFA Union System →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#22: Women in Aviation International (WAI) Technical Scholarships</div>
        <div class="card-subtitle">Strategic Value: Specialized Tech Block Equity</div>
        <p><strong>Summary:</strong> Dedicated scholarship network awarding specialized funding blocks for airframe and avionics ratings.</p>
        <p><strong>Strategic Value:</strong> Promotes diversity in the hangar by funding technical training for young women.</p>
        <a class="resource-link" href="https://www.wai.org/scholarships" target="_blank">WAI Scholarships Hub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#23: JSFirm Aviation Maintenance Job Board</div>
        <div class="card-subtitle">Strategic Value: Live Hangar Proficiencies Demand Analysis</div>
        <p><strong>Summary:</strong> A real-time hiring search engine showing what specific tool proficiencies and certificates are actively in high demand.</p>
        <p><strong>Strategic Value:</strong> Allows students to spot current market wage trends and identify highly valued technical skills.</p>
        <a class="resource-link" href="https://www.jsfirm.com/" target="_blank">JSFirm Hangar Search →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#24: ATP Flight School AMT Pipeline</div>
        <div class="card-subtitle">Strategic Value: Fast-Track Logistics Deployment Outlines</div>
        <p><strong>Summary:</strong> Accelerating training program outlines tracking commercial airline fleet support logistics.</p>
        <p><strong>Strategic Value:</strong> Illustrates how fast-track training setups transition students rapidly from school to airline careers.</p>
        <a class="resource-link" href="https://atpflightschool.com/" target="_blank">ATP AMT Career Program →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#25: Professional Aviation Maintenance Association (PAMA)</div>
        <div class="card-subtitle">Strategic Value: Global Safety Updates Monitoring</div>
        <p><strong>Summary:</strong> Core professional network hosting trade webinars and connecting high school chapters to active field events.</p>
        <p><strong>Strategic Value:</strong> Keeps young technicians informed on changing global licensing and regulatory safety updates.</p>
        <a class="resource-link" href="https://www.pama.org/" target="_blank">PAMA National Portal →</a>
    </div>
    """, unsafe_allow_html=True)
    
# PAGE 6: DRONE LOGISTICS (UNCREWED AERIAL SYSTEMS (UAS) & DRONE LOGISTICS HUB - TOP 25)
elif st.session_state.page == "Drone":
    st.markdown("### 🛸 Section 5: Uncrewed Aerial Systems (UAS) & Drone Logistics Hub")
    
    # Category 1
    st.markdown("#### 🥇 Cross-Section Overlap & Baseline Frameworks")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#1: EAA AeroEducate Portal</div>
        <div class="card-subtitle">Strategic Value: High School Engineering Integration</div>
        <p><strong>Summary:</strong> High school STEM activity tracker focusing on drone structural assemblies and programmatic flight paths.</p>
        <p><strong>Strategic Value:</strong> Integrates uncrewed flight logic into foundational high school engineering tasks.</p>
        <a class="resource-link" href="https://www.aeroeducate.org/" target="_blank">EAA AeroEducate →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#2: Aircraft Electronics Association (AEA) Educational Foundation</div>
        <div class="card-subtitle">Strategic Value: Autonomous Radio Telemetry Funding</div>
        <p><strong>Summary:</strong> Funding portal expanding into drone avionics, sensor arrays, and remote frequency tracking certifications.</p>
        <p><strong>Strategic Value:</strong> Provides unique funding for students building custom autonomous radio telemetry hardware.</p>
        <a class="resource-link" href="https://aea.net/foundation/" target="_blank">AEA Foundation Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#3: NOAA Aviation Weather Center (AWC)</div>
        <div class="card-subtitle">Strategic Value: Micro-Meteorological Risk Mitigation</div>
        <p><strong>Summary:</strong> Real-time wind velocity, icing levels, and cloud ceiling tracker required for safe low-altitude drone operations.</p>
        <p><strong>Strategic Value:</strong> Critical for avoiding micro-meteorological wind shear that could crash light consumer drones.</p>
        <a class="resource-link" href="https://aviationweather.gov/" target="_blank">Aviation Weather Live →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#4: SkyVector Aeronautical Charts</div>
        <div class="card-subtitle">Strategic Value: Airspace Classification Literacy</div>
        <p><strong>Summary:</strong> Interactive digital VFR charts mapping out airport airspace rings that commercial drones must avoid or clear.</p>
        <p><strong>Strategic Value:</strong> Essential for learning how to read airspace classes to prevent illegal drone flights near airports.</p>
        <a class="resource-link" href="https://skyvector.com/" target="_blank">SkyVector Live Map →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#5: NTSB Aviation Investigation Search</div>
        <div class="card-subtitle">Strategic Value: Regulatory Impact Trends Tracking</div>
        <p><strong>Summary:</strong> The federal incident database tracking commercial drone flyaways, systemic battery failures, and airspace near-misses.</p>
        <p><strong>Strategic Value:</strong> Teaches students how hardware failure trends directly alter commercial drone flight regulations.</p>
        <a class="resource-link" href="https://www.ntsb.gov/" target="_blank">NTSB CAROL Query →</a>
    </div>
    """, unsafe_allow_html=True)

    # Category 2
    st.markdown("#### 🎮 Drone Flight Rules & Programming")
    
    st.markdown("""
    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#6: FAA Recreational UAS Safety Test (TRUST)</div>
        <div class="card-subtitle">Strategic Value: Legal Recreational Entry Credential</div>
        <p><strong>Summary:</strong> The mandatory federal safety test that 16-year-olds can take online for free to legalize recreational flights.</p>
        <p><strong>Strategic Value:</strong> The immediate, legal entry-level credential needed before a teenager can fly any hobby drone outside.</p>
        <a class="resource-link" href="https://www.faa.gov/uas/recreational_pilots/safety_test" target="_blank">FAA TRUST Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#7: FAA Part 107 Small UAS Remote Pilot Study Guide</div>
        <div class="card-subtitle">Strategic Value: Commercial Pilot License Earning</div>
        <p><strong>Summary:</strong> The official government framework covering radio signals, loading limits, and airspace restrictions for drone pilots.</p>
        <p><strong>Strategic Value:</strong> Serves as the master study text for earning a commercial drone license at the legal minimum age of 16.</p>
        <a class="resource-link" href="https://www.faa.gov/uas" target="_blank">FAA Uncrewed Systems Hub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#8: Drone Pilot Ground School Free Resources</div>
        <div class="card-subtitle">Strategic Value: High-Yield Exam Calibration</div>
        <p><strong>Summary:</strong> High-yield visual flashcards and practice quizzes prepping high schoolers for the official Part 107 commercial test.</p>
        <p><strong>Strategic Value:</strong> Speeds up exam prep through specialized practice tools designed for young learners.</p>
        <a class="resource-link" href="https://uavcoach.com/" target="_blank">UAV Coach Training →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#9: QGroundControl Autonomous Mission Planner</div>
        <div class="card-subtitle">Strategic Value: Automated Delivery System Mapping</div>
        <p><strong>Summary:</strong> The open-source manual teaching students how to code automatic waypoint flight maps and geographic boundary fences.</p>
        <p><strong>Strategic Value:</strong> Builds programmatic skills in autonomous delivery mapping and automated grid survey flying.</p>
        <a class="resource-link" href="http://qgroundcontrol.com/" target="_blank">QGroundControl Project →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#10: UAV Coach Community Forums</div>
        <div class="card-subtitle">Strategic Value: Managed Peer-to-Enterprise Networking</div>
        <p><strong>Summary:</strong> A safe, moderated network where young operators ask hardware optimization questions and discuss camera setups.</p>
        <p><strong>Strategic Value:</strong> Connects hobbyists with seasoned commercial remote pilots running active mapping businesses.</p>
        <a class="resource-link" href="https://uavcoach.com/community/" target="_blank">UAV Coach Community →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#11: FAA DroneZone Portal</div>
        <div class="card-subtitle">Strategic Value: Federal Asset Registration Workflow</div>
        <p><strong>Summary:</strong> The official dashboard used to register hardware assets, apply for altitude waivers, and report operations.</p>
        <p><strong>Strategic Value:</strong> Teaches regulatory discipline by introducing students to official government asset registration systems.</p>
        <a class="resource-link" href="https://faadronezone-access.faa.gov/" target="_blank">FAA DroneZone →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#12: Aloft Air Control (LAANC Authorization)</div>
        <div class="card-subtitle">Strategic Value: Real-Time Air Traffic Digital Interface</div>
        <p><strong>Summary:</strong> A live platform used to request near-instant automated clearances to fly inside airport airspace rings.</p>
        <p><strong>Strategic Value:</strong> Demonstrates how modern digital automation interfaces with air traffic control systems in real-time.</p>
        <a class="resource-link" href="https://www.aloft.ai/" target="_blank">Aloft Remote Ops →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#13: Pix4D Drone Mapping Academy</div>
        <div class="card-subtitle">Strategic Value: Industrial Terrain Modeling Data Skills</div>
        <p><strong>Summary:</strong> Free entry-level guides explaining how drones stitch together aerial photographs to construct 3D terrain models.</p>
        <p><strong>Strategic Value:</strong> Bridges the gap between basic stick-and-rudder flying and high-paying industrial data mapping careers.</p>
        <a class="resource-link" href="https://www.pix4d.com/" target="_blank">Pix4D Training →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#14: DroneDeploy Educational Resources</div>
        <div class="card-subtitle">Strategic Value: Trans-Industrial Sector Applications Analysis</div>
        <p><strong>Summary:</strong> Classroom layout modules tracking drone data use across modern agriculture, surveying, and thermal rescue tasks.</p>
        <p><strong>Strategic Value:</strong> Shows students how uncrewed aviation is actively transforming traditional non-aviation industries.</p>
        <a class="resource-link" href="https://www.dronedeploy.com/" target="_blank">DroneDeploy System →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#15: ArduPilot Open-Source Autopilot Software</div>
        <div class="card-subtitle">Strategic Value: Hardware Stabilization Coding Logic</div>
        <p><strong>Summary:</strong> Comprehensive software documentation teaching teens how to configure open-source code for custom drone frames.</p>
        <p><strong>Strategic Value:</strong> Promotes hands-on robotics skills by demonstrating how software logic stabilizes multi-rotor systems.</p>
        <a class="resource-link" href="https://ardupilot.org/" target="_blank">ArduPilot Project Site →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#16: MultiGP Drone Racing League</div>
        <div class="card-subtitle">Strategic Value: High-Speed Reflex and Frequency Coordination</div>
        <p><strong>Summary:</strong> The global competitive network tracking local FPV (First Person View) racing clubs and custom-built frame events.</p>
        <p><strong>Strategic Value:</strong> Sharpens high-speed reflex coordination and deepens understanding of radio frequency management.</p>
        <a class="resource-link" href="https://www.multigp.com/" target="_blank">MultiGP League Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#17: Commercial UAV News</div>
        <div class="card-subtitle">Strategic Value: Cargo Network Sector Identification</div>
        <p><strong>Summary:</strong> Industry news tracking cargo delivery networks, automated flight laws, and medical drone distribution systems.</p>
        <p><strong>Strategic Value:</strong> Helps students identify active market sectors, such as package delivery logistics and infrastructure inspection.</p>
        <a class="resource-link" href="https://www.commercialuavnews.com/" target="_blank">Commercial UAV Portal →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#18: ASTM International Uncrewed Systems Standards</div>
        <div class="card-subtitle">Strategic Value: Global Manufacturing Quality Validation</div>
        <p><strong>Summary:</strong> Universal manufacturing criteria covering drone parachute safety systems, remote tracking signals, and build limits.</p>
        <p><strong>Strategic Value:</strong> Teaches engineering students the standardization rules required to sell consumer hardware globally.</p>
        <a class="resource-link" href="https://www.astm.org/" target="_blank">ASTM UAS Catalog →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-foundational">Tier 1: Foundational</div>
        <div class="card-title">#19: FAA B4UFLY Airspace Awareness App</div>
        <div class="card-subtitle">Strategic Value: GPS Pre-Flight Safety Verification</div>
        <p><strong>Summary:</strong> An interactive map tool that uses your phone's GPS to show local flight rules and temporary flight restrictions.</p>
        <p><strong>Strategic Value:</strong> Provides an immediate pre-flight safety check to prevent accidental violations of temporary airspace bans.</p>
        <a class="resource-link" href="https://www.faa.gov/uas/recreational_pilots/b4ufly" target="_blank">FAA Safety Geofencing →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#20: Association for Unmanned Vehicle Systems International (AUVSI)</div>
        <div class="card-subtitle">Strategic Value: Cross-Domain Autonomous Systems Research</div>
        <p><strong>Summary:</strong> The primary trade association tracking drone logistics jobs, legal frameworks, and global autonomy breakthroughs.</p>
        <p><strong>Strategic Value:</strong> Offers a broad view of international uncrewed robotics trends across air, land, and sea.</p>
        <a class="resource-link" href="https://www.auvsi.org/" target="_blank">AUVSI Network →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-highest">Tier 4: Highest</div>
        <div class="card-title">#21: Women and Drones Education Platform</div>
        <div class="card-subtitle">Strategic Value: Gender Diversity Development Outreach</div>
        <p><strong>Summary:</strong> Focuses on STEM high school outreach, offering specialized scholarships and professional flight mentoring for girls.</p>
        <p><strong>Strategic Value:</strong> Supports gender diversity in autonomous aviation through targeted youth development programs.</p>
        <a class="resource-link" href="https://womenanddrones.com/" target="_blank">Women and Drones Hub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#22: Center for the Study of the Drone at Bard</div>
        <div class="card-subtitle">Strategic Value: Ethical & Surveillance Analytical Thinking</div>
        <p><strong>Summary:</strong> An academic tracking clearinghouse posting deep research on how military and consumer drones impact global safety.</p>
        <p><strong>Strategic Value:</strong> Encourages critical thinking regarding the ethical, legal, and privacy implications of drone surveillance.</p>
        <a class="resource-link" href="https://dronecenter.bard.edu/" target="_blank">Bard Drone Center →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#23: Drone-Made Global Mapping Regulations</div>
        <div class="card-subtitle">Strategic Value: Cross-Border Content Creation Verification</div>
        <p><strong>Summary:</strong> A comprehensive index listing drone travel rules and legal pilot parameters for nearly every country.</p>
        <p><strong>Strategic Value:</strong> Vital for travel content creators and international drone operators checking foreign legal limits.</p>
        <a class="resource-link" href="https://www.drone-made.com/" target="_blank">Drone-Made Travel Hub →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-high">Tier 3: High</div>
        <div class="card-title">#24: InterDrone Educational Archive</div>
        <div class="card-subtitle">Strategic Value: Fleet Trajectory Machine Vision Insights</div>
        <p><strong>Summary:</strong> Access to recorded panels discussing autonomous drone fleets, machine vision tracking, and engineering setups.</p>
        <p><strong>Strategic Value:</strong> Exposes high schoolers to expert opinions on the future trajectory of drone fleet logistics.</p>
        <a class="resource-link" href="https://www.interdrone.com/" target="_blank">InterDrone Platform →</a>
    </div>

    <div class="resource-card">
        <div class="tier-badge-medium">Tier 2: Medium</div>
        <div class="card-title">#25: DartDrone Training Resources</div>
        <div class="card-subtitle">Strategic Value: Enterprise Business Architecture Diagnostic</div>
        <p><strong>Summary:</strong> Free diagnostic test tracks and industry briefs analyzing commercial drone business setups and insurance options.</p>
        <p><strong>Strategic Value:</strong> Teaches young entrepreneurs how to structure a legal drone photography or inspection business safely.</p>
        <a class="resource-link" href="https://www.dartdrones.com/" target="_blank">DartDrones Online →</a>
    </div>
    """, unsafe_allow_html=True)
    
# PAGE 7: AEROBOT GROUND KNOWLEDGE SYSTEM
elif st.session_state.page == "AI":
    st.markdown("### 🤖 AeroBot: Avionics Ground Instructor")
    
    st.markdown("""
    <div class="resource-card">
        <div class="card-title">AeroBot Training Terminal</div>
        <div class="card-subtitle">Powered by Zapier AI Engine</div>
        <p style='font-size: 16px;'>To provide a completely secure, unrestricted learning environment for young aviators, the AeroBot training core is hosted within our age-approved Zapier cloud network. Click the button below to clear tracking blocks and boot up the interactive flight instructor terminal.</p>
        <div class="guidance-box">
            <strong>📋 Student Note:</strong> You can quiz AeroBot on airspace tiers, weather codes, or aircraft weight balances. It will immediately generate precise FAA instruction patterns.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Launch AeroBot Training Interface 🚀", "https://schoolaichatbot.zapier.app/", use_container_width=True)

# PAGE 8: GLOBAL COMMUNITY CHAT
elif st.session_state.page == "Community":
    st.markdown("### 🌐 AeroLaunch Global Community Hub")
    st.write("Welcome to the community chat! Share updates, coordinate projects, or talk aviation with your peers.")
    
    st.markdown("---")
    
    import json
    import os
    from datetime import datetime

    # File-based database path to persist chat history globally
    CHAT_DB = "community_chat_history.json"

    # Helper functions to handle global chat I/O files safely
    def load_global_chat():
        if os.path.exists(CHAT_DB):
            try:
                with open(CHAT_DB, "r") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_global_message(username, text):
        history = load_global_chat()
        new_msg = {
            "user": username,
            "text": text,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        history.append(new_msg)
        # Cap the history log at the last 100 messages to prevent bloated text files
        with open(CHAT_DB, "w") as f:
            json.dump(history[-100:], f, indent=4)

    # 1. Load Current Shared Log History
    global_messages = load_global_chat()

    # 2. Display Chat Container Layout Window
    chat_container = st.container()
    
    with chat_container:
        if not global_messages:
            st.info("The chat lounge is currently quiet. Be the first to start the conversation!")
        else:
            for msg in global_messages:
                # Format layout cleanly inside your chat container box space
                st.markdown(f"**💬 {msg['user']}** <span style='color:gray; font-size:0.8rem;'>({msg['timestamp']})</span>", unsafe_allow_html=True)
                st.markdown(f"*{msg['text']}*")
                st.markdown("<div style='margin-bottom: 12px; border-bottom: 1px dashed #e2e8f0;'></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Message Input Interaction Tool
    # Automatically pulls the user's register data or assigns a clean fallback handle
    default_handle = st.session_state.get("user_email", "Anonymous Pilot")
    
    with st.form("community_chat_form", clear_on_submit=True):
        chat_text = st.text_input("Type your broadcast message:", placeholder="Say hello to the crew...")
        submit_chat = st.form_submit_button("Broadcast to Runway 🚀", use_container_width=True)
        
        if submit_chat and chat_text.strip():
            save_global_message(default_handle, chat_text.strip())
            st.rerun()
