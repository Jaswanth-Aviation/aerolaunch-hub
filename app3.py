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
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }
    
    .resource-card p {
        color: #334155 !important;
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

nav_cols = st.columns(6)

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
    if st.button("🤖 AeroBot AI", use_container_width=True, type="primary" if st.session_state.page == "AI" else "secondary"):
        st.session_state.page = "AI"
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

# PAGE 2: PILOT HUB
elif st.session_state.page == "Pilots":
    st.markdown("## 🧭 Section 1: The Pilot Hub (Top 25)")
    st.write("Structured modules built to optimize competitive credentials and accelerate primary flight training timelines.")
    st.write("---")

    # SUBSECTION A
    st.markdown("### 🥇 Foundational Academics & Checkride Essentials")
    
    #1
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#1: FAA Pilot’s Handbook of Aeronautical Knowledge (PHAK)</div>
        <div class="card-subtitle">Category: Regulatory Textbook</div>
        <p style='font-size: 16px;'>The definitive textbook covering aerodynamic principles, aircraft systems, flight instruments, weather theory, and basic navigation.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Forms the absolute bedrock of theoretical knowledge required to pass any aviation written exam or oral checkride globally.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Open Textbook Library Repository ↗️", "https://open.umn.edu/opentextbooks/textbooks/pilot-s-handbook-of-aeronautical-knowledge", use_container_width=True)
    st.write("")

    #2
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#2: FAA Airplane Flying Handbook (AFH)</div>
        <div class="card-subtitle">Category: Operational Manual</div>
        <p style='font-size: 16px;'>A comprehensive guide focusing on the physical mechanics of flight, including maneuvers, takeoffs, landings, and emergency procedures.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Bridges the gap between classroom theory and real-world stick-and-rudder skills, standardizing flight training maneuvers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Document Gateway ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/airplane_handbook", use_container_width=True)
    st.write("")

    #3
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#3: Pilot Institute Free Private Pilot Ground School Primer</div>
        <div class="card-subtitle">Category: Introductory Ground Course</div>
        <p style='font-size: 16px;'>An introductory video-based course outlining the core requirements, costs, regulations, and basic physics involved in getting a license.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Acts as an accessible, high-yield introductory funnel for student pilots to visualize their entire training timeline before investing capital.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Pilot Institute Portal ↗️", "https://pilotinstitute.com/course/free-private-pilot/", use_container_width=True)
    st.write("")

    #4
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#4: Sporty’s Study Buddy Exam Prep Engine</div>
        <div class="card-subtitle">Category: Written Test Prep</div>
        <p style='font-size: 16px;'>A dynamic, database-driven practice test module that generates authentic practice questions mimicking the actual FAA Private Pilot written test.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Optimizes exam readiness through targeted testing, allowing users to identify weak knowledge areas before taking official exams.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Sporty's Online Prep ↗️", "https://www.sportys.com/studybuddy", use_container_width=True)
    st.write("")

    #5
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#5: SkyVector Aeronautical Charts</div>
        <div class="card-subtitle">Category: Flight Planning & Charts</div>
        <p style='font-size: 16px;'>A real-time, global digital plotting tool providing VFR Sectionals, IFR High/Low charts, and live weather overlays.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Essential for mastering flight planning, visual tracking, and understanding complex airspace boundaries from a web browser.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SkyVector Live Map ↗️", "https://skyvector.com/", use_container_width=True)
    st.write("")

    #6
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#6: King Schools Interactive Flight Exam Modules</div>
        <div class="card-subtitle">Category: Conceptual Modules</div>
        <p style='font-size: 16px;'>Interactive mini-modules focusing on challenging flight concepts like crosswind components, weight and balance, and airspace restrictions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Simplifies complex mathematical and physics-based aviation principles through proven, memorable visual teaching styles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to King Schools Free Library ↗️", "https://kingschools.com/free-aviation-courses", use_container_width=True)
    st.write("")

    #7
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#7: Boldmethod Flight Training Quizzes</div>
        <div class="card-subtitle">Category: Scenario Training</div>
        <p style='font-size: 16px;'>Highly visual, scenario-based quizzes addressing real-world aviation challenges, from systems failures to tricky weather scenarios.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Sharpens quick critical thinking and Aeronautical Decision Making (ADM) skills by putting users into simulated pilot dilemmas.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Boldmethod Training Portal ↗️", "https://www.boldmethod.com/blog/quizzes/", use_container_width=True)
    st.write("")

    #8
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#8: FAA Airman Certification Standards (ACS)</div>
        <div class="card-subtitle">Category: Checkride Evaluation Parameters</div>
        <p style='font-size: 16px;'>The official regulatory document detailing the exact parameters, tolerances, and knowledge areas tested during a pilot practical exam.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Serves as the ultimate grading standard, ensuring pilots know exactly what constitutes a passing or failing performance on a checkride.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Airman Testing Standards ↗️", "https://www.faa.gov/training_testing/testing/acs", use_container_width=True)
    st.write("")

    # SUBSECTION B
    st.markdown("### 🎮 Flight Simulation & Cockpit Flow Drills")
    
    #9
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#9: X-Plane Scenery Gateway</div>
        <div class="card-subtitle">Category: Simulation Environments</div>
        <p style='font-size: 16px;'>A collaborative database sharing highly accurate, community-vetted airport layouts and visual environments for flight simulation.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Enables highly realistic airport familiarization and taxi routing practice for students preparing to fly into real-world hubs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to X-Plane Scenery Hub ↗️", "https://gateway.x-plane.com/", use_container_width=True)
    st.write("")

    #10
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#10: FreeChecklists.net Directory</div>
        <div class="card-subtitle">Category: Aircraft Checklists</div>
        <p style='font-size: 16px;'>A massive crowdsourced directory hosting standard operating checklists for hundreds of general aviation and commercial aircraft.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches structural discipline by getting student pilots into the habit of using verified, sequential safety checklists.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FreeChecklists Repository ↗️", "https://www.freechecklists.net/", use_container_width=True)
    st.write("")

    #11
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#11: SimBrief Enterprise Dispatch Engine</div>
        <div class="card-subtitle">Category: Virtual Dispatch & Route Planning</div>
        <p style='font-size: 16px;'>A professional-grade web utility that generates highly realistic virtual flight plans, fuel calculations, and airline operational release documents.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Introduces students to advanced airline dispatching, flight planning, and route fuel management logistics.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SimBrief Routing Tool ↗️", "https://www.simbrief.com/", use_container_width=True)
    st.write("")

    #12
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#12: Little Navmap Open-Source Navigation</div>
        <div class="card-subtitle">Category: Moving Maps & Planning</div>
        <p style='font-size: 16px;'>A free, open-source flight planner and moving map display featuring airport diagrams, wind overlays, and elevation profiles.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Perfect for introducing cross-country flight planning, vector tracks, and airspace boundary rules without recurring costs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Little Navmap GitHub ↗️", "https://github.com/albar965/littlenavmap", use_container_width=True)
    st.write("")

    #13
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#13: VOR Navigation Web App Simulator</div>
        <div class="card-subtitle">Category: Instrumentation Simulation</div>
        <p style='font-size: 16px;'>An interactive, browser-based graphical utility for understanding how instrument needles move relative to ground stations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Solves one of the hardest conceptual hurdles for new pilots: visualizing relative orientation using legacy radio navigation tools.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to LuizMonteiro VOR Sim ↗️", "https://www.luizmonteiro.com/learning_vor.aspx", use_container_width=True)
    st.write("")

    #14
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#14: Garmin G1000 Glass Cockpit Interface Guide</div>
        <div class="card-subtitle">Category: Avionics Frameworks</div>
        <p style='font-size: 16px;'>Official training handbooks breaking down the structure, flight instrument screens, and map menus of modern integrated glass avionics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Accelerates situational awareness by allowing pilots to master digital avionics navigation menus before stepped training flights.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Garmin Digital Manuals ↗️", "https://support.garmin.com/", use_container_width=True)
    st.write("")

    # SUBSECTION C
    st.markdown("### 🌤️ Meteorology & Radio Communications")
    
    #15
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#15: NOAA Aviation Weather Center (AWC)</div>
        <div class="card-subtitle">Category: Live Meteorology Metrics</div>
        <p style='font-size: 16px;'>The central US portal providing METARs, TAFs, SIGMETs, convective outlooks, and satellite imagery for active flights.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> The primary operational portal for pulling official pre-flight weather data and learning real-time weather monitoring.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Aviation Weather Live ↗️", "https://aviationweather.gov/", use_container_width=True)
    st.write("")

    #16
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-foundational">⚓ Tier 4: Foundational Value</span><br>
        <div class="card-title">#16: Bad Elf METAR/TAF Decoding Tool</div>
        <div class="card-subtitle">Category: Weather Coded Text Processing</div>
        <p style='font-size: 16px;'>A clean web tool that translates condensed, coded text weather statements into plain, easily understood descriptions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Speeds up weather literacy for beginners learning to decode critical variables like wind speed, ceiling heights, and pressure shifts.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Bad Elf Decoder ↗️", "https://bad-elf.com/pages/metar-decoder", use_container_width=True)
    st.write("")

    #17
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#17: LiveATC.net Global Audio Network</div>
        <div class="card-subtitle">Category: Live ATC Audio Comms</div>
        <p style='font-size: 16px;'>A network streaming live radio traffic from thousands of air traffic control facilities and towers worldwide.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students bridge the gap between textbook terms and real-world audio comprehension, improving listening habits early on.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to LiveATC Global Feeds ↗️", "https://www.liveatc.net/", use_container_width=True)
    st.write("")

    #18
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#18: PlaneEnglish: ARSim Free Training Tier</div>
        <div class="card-subtitle">Category: Conversational Sandbox Engine</div>
        <p style='font-size: 16px;'>A web-accessible version of an AI-driven sandbox that analyzes and scores radio phrases for rhythm, structure, and accuracy.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Builds vocal muscle memory and reduces microphone anxiety through structured, interactive speaking exercises.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to PlaneEnglish Classroom ↗️", "https://planeenglishsim.com/", use_container_width=True)
    st.write("")

    #19
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#19: FAA AIM Chapter 4: Air Traffic Control Procedures</div>
        <div class="card-subtitle">Category: Communication Regulations</div>
        <p style='font-size: 16px;'>The regulatory chapter defining official communication standards, radar services, transponder use, and airport operations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides the legal guidelines for pilot-to-controller communications, establishing the rules of the road for public airspace.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Aeronautical Information Manual ↗️", "https://www.faa.gov/air_traffic/publications/atpubs/aim_html/", use_container_width=True)
    st.write("")

    #20
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#20: NASA/Ames Aviation Safety Reporting System (ASRS)</div>
        <div class="card-subtitle">Category: Human Factors Error Case Studies</div>
        <p style='font-size: 16px;'>A voluntary, anonymous reporting database detailing real-world flight crew errors, unexpected weather encounters, and aircraft malfunctions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows students to study genuine, unfiltered human-error case studies to foster a culture focused on proactive safety management.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to NASA ASRS System Database ↗️", "https://asrs.arc.nasa.gov/", use_container_width=True)

    # SUBSECTION D
    st.markdown("### 💰 Scholarships & Specialized Video Ground Schools")
    
    #21
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#21: AOPA High School Flight Training Scholarship Portal</div>
        <div class="card-subtitle">Category: Youth Grant Application</div>
        <p style='font-size: 16px;'>An annual grant portal offering up to tens of thousands of dollars to high school students chasing primary private pilot certificates.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Directly lowers financial hurdles for young aviators, making it a high-value link for early student users.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AOPA Scholarships ↗️", "https://youcanfly.aopa.org/scholarships", use_container_width=True)
    st.write("")

    #22
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#22: EAA Ray Aviation Scholarship Foundation Database</div>
        <div class="card-subtitle">Category: Chapter Endowed Funding</div>
        <p style='font-size: 16px;'>A funded grant system run through local experimental aircraft chapters that covers full flight training bills for local youths.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Leverages regional flying clubs to provide mentoring alongside financial assistance, boosting student completion rates.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to EAA Ray Scholarship Board ↗️", "https://www.eaa.org/eaa/youth/ray-aviation-scholarship", use_container_width=True)
    st.write("")

    #23
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#23: Free Pilot Training Online Ground Academy</div>
        <div class="card-subtitle">Category: Video Course Library</div>
        <p style='font-size: 16px;'>Comprehensive, step-by-step video deep-dives going over the entire Private Pilot knowledge blueprint for zero cost.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Offers an excellent free alternative to premium video courses, making ground school accessible to all students.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Free Pilot Training Network ↗️", "https://www.freepilottraining.org/", use_container_width=True)
    st.write("")

    #24
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#24: The Finer Points: Professional Pilot Flight Training</div>
        <div class="card-subtitle">Category: Advanced Flying Insights</div>
        <p style='font-size: 16px;'>Educational videos focusing on flight deck organization, refined piloting techniques, stick-and-rudder feel, and safety tips.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students master flight skills faster through sharp, actionable tips from senior flight instructors.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to The Finer Points Flight Resource ↗️", "https://www.learnthefinerpoints.com/", use_container_width=True)
    st.write("")

    #25
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#25: MzeroA Flight Training Free Resource Playlists</div>
        <div class="card-subtitle">Category: Checkride Prep Media</div>
        <p style='font-size: 16px;'>Informative videos covering typical oral exam questions, checkride gotchas, and everyday safety procedures.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Excellent for last-minute oral checkride prep, helping turn complex regulations into clear talking points.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to MzeroA Online Platform ↗️", "https://mzeroa.com/", use_container_width=True)

# PAGE 3: ATC HUB
elif st.session_state.page == "ATC":
    st.markdown("## 🎙️ Section 2: Air Traffic Control (Top 25)")
    st.write("Professional simulation tracks, metrics, and standard phraseology systems designed to master controller infrastructure.")
    st.write("---")

    # SUBSECTION A
    st.markdown("### 🥇 Virtual ATC Frameworks & Master Rules")

    #1
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#1: VATSIM S1 Controller Training Syllabus</div>
        <div class="card-subtitle">Category: Basic Ground Management</div>
        <p style='font-size: 16px;'>The fundamental gateway manual covering clearance formats, airport ground layouts, and taxi safety protocols.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Ideal for teaching the basics of ground management before students move on to active radar sequencing.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to VATSIM United States Training Portal ↗️", "https://vatsim.net/", use_container_width=True)
    st.write("")

    #2
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#2: FAA Order JO 7110.65 (Air Traffic Control Manual)</div>
        <div class="card-subtitle">Category: Legal Rulebook</div>
        <p style='font-size: 16px;'>The absolute legal handbook defining standard US phraseology, separation minimums, and vector guidelines.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> The definitive handbook for air traffic control, serving as the core reference source for any ATC training setup.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Document Gateway: JO 7110.65 ↗️", "https://www.faa.gov/air_traffic/publications/", use_container_width=True)
    st.write("")

    #3
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#3: IVAO ATC Online Academy Manuals</div>
        <div class="card-subtitle">Category: Global Training System</div>
        <p style='font-size: 16px;'>International training handbooks focusing on ICAO terminal rules, transition layer setups, and non-US vector standards.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides essential global perspective, teaching students how air traffic control operates outside North America.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to IVAO HQ Training Academy ↗️", "https://ivao.aero/", use_container_width=True)
    st.write("")

    #4
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#4: Eurocontrol Training Zone Portal</div>
        <div class="card-subtitle">Category: Airspace Congestion Flows</div>
        <p style='font-size: 16px;'>Interactive training tracking air traffic flows, sector load balancing, and delay-reduction strategies across Europe.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Introduces high-level airspace management concepts, showing how to handle traffic flows between different countries.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Eurocontrol Aviation Training Portal ↗️", "https://www.eurocontrol.int/", use_container_width=True)
    st.write("")

    #5
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#5: EuroScope Radar Client Software Project</div>
        <div class="card-subtitle">Category: Interface Simulation Software</div>
        <p style='font-size: 16px;'>A highly detailed radar simulator client that replicates real-world European air traffic radar displays and tracker systems.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Gives students hands-on practice with professional-grade radar tools from home without needing expensive academy equipment.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to EuroScope Radar Engine ↗️", "https://www.euroscope.hu/", use_container_width=True)
    st.write("")

    #6
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#6: OpenRadar Open-Source Tower Tracking Software</div>
        <div class="card-subtitle">Category: Open-Source Tracking Client</div>
        <p style='font-size: 16px;'>An open-source radar simulator focusing on terminal approach control and tower visual sweeps.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides an accessible tool for students to practice managing traffic arcs and local terminal arrivals.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to OpenRadar SourceForge Project ↗️", "https://sourceforge.net/projects/openradar/", use_container_width=True)
    st.write("")

    # SUBSECTION B
    st.markdown("### 🛰️ Radar Vectoring Mechanics & Separation Rules")

    #7
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#7: ATC-Sim Browser Radar Vectoring Game</div>
        <div class="card-subtitle">Category: Web Vector Sandbox</div>
        <p style='font-size: 16px;'>A 2D browser simulator where players issue headings, altitudes, and speeds to feed arrivals onto final approach paths safely.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> A fast, interactive way to practice radar geometry and master vectoring techniques early in training.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ATC-Sim Browser Radar Engine ↗️", "https://www.atc-sim.com/", use_container_width=True)
    st.write("")

    #8
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#8: FAA Runway Incursion Prevention Training Simulator</div>
        <div class="card-subtitle">Category: Ground Safety Matrix</div>
        <p style='font-size: 16px;'>Interactive training tools designed to spot and prevent ground errors, runway incursions, and vehicle tracking mistakes.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Focuses heavily on ground safety, teaching students how to keep runways clear and prevent close calls on the tarmac.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Runway Safety Portal ↗️", "https://www.faa.gov/airports/runway_safety/", use_container_width=True)
    st.write("")

    #9
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#9: ICAO Document 4444 (Air Traffic Management Standards)</div>
        <div class="card-subtitle">Category: International Protocol Treaty</div>
        <p style='font-size: 16px;'>The master international treaty text standardizing air traffic rules, flight rules, and separation criteria worldwide.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> The core reference for international air traffic control, vital for understand global aviation standards.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ICAO Store Reference Catalog ↗️", "https://store.icao.int/", use_container_width=True)
    st.write("")

    #10
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#10: Standard Lateral and Vertical Separation Minimums Matrix</div>
        <div class="card-subtitle">Category: Separation Minimums Charts</div>
        <p style='font-size: 16px;'>Quick-reference tables outlining legal distance limits ($3\\text{ miles}$, $5\\text{ miles}$, or $1000\\text{ feet}$ vertically) required between planes.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Instills basic safety limits, helping controllers maintain legal margins and prevent separation violations.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SKYbrary Separation Standards ↗️", "https://skybrary.aero/articles/separation-standards", use_container_width=True)
    st.write("")

    #11
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#11: Wake Turbulence Category Separation Requirements</div>
        <div class="card-subtitle">Category: Dynamic Vortex Spacing</div>
        <p style='font-size: 16px;'>Tables outlining required distance buffers behind heavy jets to prevent light planes from hitting dangerous wingtip vortices.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Critical for avoiding wake turbulence accidents, helping controllers space departures safely based on weight class.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Wake Turbulence Mitigation Portal ↗️", "https://www.faa.gov/nextgen/programs/wake_turbulence/", use_container_width=True)
    st.write("")

    #12
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#12: Intercept Angle Mathematics for Instrument Approaches</div>
        <div class="card-subtitle">Category: Mathematical Vectoring Arcs</div>
        <p style='font-size: 16px;'>Guides outlining how to turn planes onto instrument final approaches ($30\\text{-degree}$ maximum limits) without overshooting the line.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Sharpens mental math skills, helping controllers issue smooth turns that align pilots perfectly with instrument approach paths.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Instrument Procedures Handbook ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/", use_container_width=True)
    st.write("")

    # SUBSECTION C
    st.markdown("### 🎙️ Tower Operations & Airspace Infrastructure")

    #13
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#13: FAA Airport Sign and Marking Guide</div>
        <div class="card-subtitle">Category: Tarmac Visual Systems</div>
        <p style='font-size: 16px;'>Visual reference guides illustrating runway hold lines, taxi signs, direction indicators, and displaced threshold markers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Essential for tower operators, helping them guide pilots accurately through complex airport layouts.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Runway Safety Sign Manual ↗️", "https://www.faa.gov/airports/runway_safety/publications/", use_container_width=True)
    st.write("")

    #14
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#14: Land and Hold Short Operations (LAHSO) Safety Limits</div>
        <div class="card-subtitle">Category: Intersecting Capacity Rules</div>
        <p style='font-size: 16px;'>Operating parameters for landing planes on intersecting runways and stopping them before the crossing point.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Increases airport capacity during peak hours while keeping strict safety margins between crossing aircraft.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA LAHSO Directives Matrix ↗️", "https://www.faa.gov/training_testing/testing/", use_container_width=True)
    st.write("")

    #15
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#15: Airspace Classifications Dimensional Metric Matrix</div>
        <div class="card-subtitle">Category: Airspace Sector Dimensions</div>
        <p style='font-size: 16px;'>Dimensional charts illustrating the vertical and lateral boundaries of Class A, B, C, D, E, and G airspaces.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides the basic framework for airspace rules, defining when flights must establish contact with controllers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Airspace Classification Hub ↗️", "https://www.faa.gov/air_traffic/publications/atpubs/aim_html/", use_container_width=True)
    st.write("")

    #16
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#16: Standard Terminal Arrival Route (STAR) Chart Profiles</div>
        <div class="card-subtitle">Category: Standard Arrival Routing</div>
        <p style='font-size: 16px;'>Standard instrument arrival charts detailing predefined routes, speed limits, and altitude restrictions for incoming jets.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Streamlines approach control workloads by automatically organizing arrivals onto standard terminal paths.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Terminal Procedures Publication (d-TPP) ↗️", "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/", use_container_width=True)
    st.write("")

    #17
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#17: Holding Pattern Entry Geometric Calculation Worksheets</div>
        <div class="card-subtitle">Category: Delay Orbit Routing</div>
        <p style='font-size: 16px;'>Math guides detailing direct, parallel, and teardrop entry profiles for holding patterns based on arrival angles.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Essential for managing traffic delays, helping controllers predict airframe paths during holding adjustments.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to CFI Notebook Holding Procedures ↗️", "https://www.cfinotebook.net/", use_container_width=True)
    st.write("")

    #18
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#18: Reduced Vertical Separation Minimum (RVSM) Flight Levels</div>
        <div class="card-subtitle">Category: High-Altitude Space Metrics</div>
        <p style='font-size: 16px;'>Rules reducing standard vertical spacing from $2000\\text{ feet}$ to $1000\\text{ feet}$ for advanced aircraft flying between FL290 and FL410.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Doubles high-altitude airspace capacity, making it vital for modern enroute sequencing training.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA RVSM Documentation Portal ↗️", "https://www.faa.gov/air_traffic/separation/rvsm/", use_container_width=True)
    st.write("")

    # SUBSECTION D
    st.markdown("### 🧠 Aptitude Testing & Emergency Scenarios")

    #19
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#19: ATSA Air Traffic Selection Assessment Prep Guide</div>
        <div class="card-subtitle">Category: Federal Screening Blueprints</div>
        <p style='font-size: 16px;'>Official overviews explaining the structure, sections, and passing scores required for the FAA's entry-level controller aptitude test.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Critical starting point for aspiring controllers, showing them what to expect before taking official entry tests.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA ATC Career Hiring Portal ↗️", "https://www.faa.gov/be-atc", use_container_width=True)
    st.write("")

    #20
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#20: JobTestPrep ATSA Free Practice Modules</div>
        <div class="card-subtitle">Category: Conflict Screening Games</div>
        <p style='font-size: 16px;'>Sample math games and interactive puzzles testing a user's ability to clear intersecting conflicts under tight time limits.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Sharpens early decision-making habits, helping candidates improve their reaction times for the official ATSA test.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to JobTestPrep ATSA Modules ↗️", "https://www.jobtestprep.com/", use_container_width=True)
    st.write("")

    #21
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#21: Transponder Squawk Code Matrix (7500, 7600, 7700)</div>
        <div class="card-subtitle">Category: Emergency Code Matrix</div>
        <p style='font-size: 16px;'>A quick-reference sheet for emergency transponder codes: 7500 (Hijack), 7600 (Radio Failure), and 7700 (General Emergency).</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows controllers to instantly identify flight emergencies on radar screens without needing verbal radio contact.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AOPA Transponder Squawk Guidelines ↗️", "https://www.aopa.org/", use_container_width=True)
    st.write("")

    #22
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-foundational">⚓ Tier 4: Foundational Value</span><br>
        <div class="card-title">#22: FAA Light Gun Signals Reference Chart</div>
        <div class="card-subtitle">Category: Visual Auxiliary Signals</div>
        <p style='font-size: 16px;'>Procedures for using airport light guns and tracking predictable pilot paths when a flight loses all radio contact.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Keeps traffic flowing safely during radio outages by providing a reliable backup communication method.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Light Gun Reference Chart ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/", use_container_width=True)
    st.write("")

    # SUBSECTION E
    st.markdown("### 📊 Historical Case Studies & Safety Logs")

    #23
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#23: Tenerife Airport Disaster Systemic Breakdown Analysis</div>
        <div class="card-subtitle">Category: Phraseology Human Factors Study</div>
        <p style='font-size: 16px;'>A safety review of the 1977 runway collision, highlighting how vague phrasing, radio blockages, and stress led to error.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> The premier lesson on radio safety, showing why the industry shifted to strict, unambiguous phraseology.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SKYbrary Tenerife Collision Analysis ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    #24
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#24: Uberlingen Mid-Air Collision TCAS Priority Study</div>
        <div class="card-subtitle">Category: Ground vs. Automation Priority Logic</div>
        <p style='font-size: 16px;'>An analysis of a mid-air crash caused when a controller's vectors directly contradicted automated onboard collision alerts (TCAS).</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches critical system priorities, establishing that automated cockpit warnings always override ground instructions during alerts.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SKYbrary Uberlingen Review ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    #25
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#25: Flight Safety Foundation: Continuous ATC Integrity Reports</div>
        <div class="card-subtitle">Category: Real-Time Active Risk Metrics</div>
        <p style='font-size: 16px;'>Regular safety reports tracking modern near-miss statistics, systemic software glitches, and controller fatigue risks.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Keeps curriculum content up to date with modern safety trends and active systemic air traffic risks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Flight Safety Foundation Safety Digest Logs ↗️", "https://flightsafety.org/", use_container_width=True)

# PAGE 4: FLIGHT ATTENDANT HUB
elif st.session_state.page == "Crew":
    st.markdown("## 🛒 Section 3: Flight Attendant / Air Hostess Hub (Top 25)")
    st.write("Comprehensive training modules, service protocols, and career toolkits designed to master cabin environment dynamics.")
    st.write("---")

    # SUBSECTION A
    st.markdown("### 🥇 Cabin Safety Protocols & Emergency Command")

    #1
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#1: ICAO Cabin Safety Training Manual (Doc 10002)</div>
        <div class="card-subtitle">Category: Global Safety Textbook</div>
        <p style='font-size: 16px;'>The global master manual detailing emergency commands, slide use, raft parameters, and survival gear layouts.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> The primary textbook for cabin safety, ensuring student training meets international airline criteria.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ICAO Store Official Reference Catalog ↗️", "https://store.icao.int/", use_container_width=True)
    st.write("")

    #2
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#2: FAA Advisory Circular 121-24C (Passenger Safety Briefings)</div>
        <div class="card-subtitle">Category: Regulatory Briefing Standards</div>
        <p style='font-size: 16px;'>Legal standards detailing what must be included in passenger briefings and exit row instructions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Ensures cabin safety presentations meet all legal criteria, preparing crews to handle safety checks confidently.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Advisory Circular Repository ↗️", "https://www.faa.gov/regulations_policies/advisory_circulars/", use_container_width=True)
    st.write("")

    #3
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#3: Skybrary Cabin Safety Compendium</div>
        <div class="card-subtitle">Category: Safety Response Database</div>
        <p style='font-size: 16px;'>An open aviation safety database cataloging best responses for severe turbulence, cabin smoke, and sudden decompressions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides an excellent reference source for building practical cabin safety guides and response workflows.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SKYbrary Cabin Safety Gateway ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    #4
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#4: Aircraft Emergency Evacuation Slide System Mechanics</div>
        <div class="card-subtitle">Category: Evacuation System Hardware</div>
        <p style='font-size: 16px;'>Technical overviews detailing door slide arming, pressure checks, and deployment triggers for various exit doors.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Eliminates door operation errors, ensuring slides are armed correctly for flight and disarmed safely for arrival.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SKYbrary Emergency Evacuation Slides ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    #5
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#5: IATA Dangerous Goods Regulations (DGR) Quick Reference</div>
        <div class="card-subtitle">Category: Hazardous Material Matrix</div>
        <p style='font-size: 16px;'>Identification charts showing restricted items, lithium battery fire hazards, and spill control steps for cabins.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps crews spot and neutralize hidden hazardous materials in carry-on bags before departure.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to IATA Dangerous Goods Documentation ↗️", "https://www.iata.org/", use_container_width=True)
    st.write("")

    # SUBSECTION B
    st.markdown("### 💼 Recruitment, Resumes & Interview Prep")

    #6
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#6: Canva Flight Attendant Resume Layout Templates</div>
        <div class="card-subtitle">Category: Visual Application Layouts</div>
        <p style='font-size: 16px;'>Visual, professional resume layouts tailored to highlight customer service skills and safety certifications for airline applications.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps candidates format their experience clearly, matching the visual styles preferred by airline hiring teams.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Canva Professional Flight Attendant Templates ↗️", "https://www.canva.com/", use_container_width=True)
    st.write("")

    #7
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#7: Indeed Career Guide: Flight Attendant Interview Steps</div>
        <div class="card-subtitle">Category: Behavioral Strategy Systems</div>
        <p style='font-size: 16px;'>Behavioral interview questions structured around Situation, Task, Action, and Result (STAR) formats used by airlines during recruitment.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prepares applicants to give structured, professional answers that demonstrate real-world problem-solving skills.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Indeed Career Guide: Flight Attendant Interview Steps ↗️", "https://www.indeed.com/", use_container_width=True)
    st.write("")

    #8
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#8: Verbal De-escalation Techniques for Confined Spaces</div>
        <div class="card-subtitle">Category: Passenger Command Strategy</div>
        <p style='font-size: 16px;'>Practical guides on diffusing passenger arguments, calming upset travelers, and resolving seating disputes peacefully.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Gives crew members the communication skills needed to handle arguments before they escalate into serious safety risks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SKYbrary Managing Disruptive Passengers ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    #9
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#9: Public Announcement (PA) Reading Script Database</div>
        <div class="card-subtitle">Category: Vocal Delivery Scripts</div>
        <p style='font-size: 16px;'>Practice scripts covering welcome messages, turbulence warnings, and customs instructions to practice clear speaking habits.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Improves vocal tone and clarity, helping crews deliver clear, professional announcements under pressure.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Flight Attendant PA Scripts Directory ↗️", "https://www.flightattendantcentral.com/", use_container_width=True)
    st.write("")

    #10
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#10: DOT Airline Accessibility Guidelines</div>
        <div class="card-subtitle">Category: Inclusive Service Protocols</div>
        <p style='font-size: 16px;'>Regulatory service guides showing how to assist solo young travelers, elderly passengers, and disabled flyers safely.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Ensures full compliance with passenger accessibility rules, providing professional, empathetic care for every flyer.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to DOT Airline Accessibility Guidelines ↗️", "https://www.transportation.gov/airconsumer", use_container_width=True)

    # SUBSECTION C
    st.markdown("### 🍽️ Catering Logic & Galley Management")

    #11
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#11: IATA Special Meal (SPML) Universal Code Matrix</div>
        <div class="card-subtitle">Category: Catering Identity Coding</div>
        <p style='font-size: 16px;'>Standardized codes used to identify special passenger meals, including vegan, kosher, halal, and allergen-free options.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents catering mix-ups, helping crews distribute specialized meals accurately to the right passengers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to IATA Passenger Special Meal Specifications ↗️", "https://www.iata.org/", use_container_width=True)
    st.write("")

    #12
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#12: Widebody Aircraft Galley Latches & Safety Standards</div>
        <div class="card-subtitle">Category: Secure Infrastructure Standards</div>
        <p style='font-size: 16px;'>Operating guides for locking meal carts, latching galley doors, and securing electrical ovens before take-off.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents cart rollaways and injury risks by ensuring all galley gear is locked down tight during turbulence.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SKYbrary Galley Safety Standards ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    #13
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#13: FDA Retail & Food Service Regulation Logs</div>
        <div class="card-subtitle">Category: Clinical Preservation Metrics</div>
        <p style='font-size: 16px;'>Health guidelines defining safe temperature ranges for holding and serving prepared meals on commercial routes.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents food spoilage, ensuring all passenger meals remain safe and healthy throughout long journeys.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FDA Retail & Food Service Regulation Logs ↗️", "https://www.fda.gov/food/", use_container_width=True)
    st.write("")

    #14
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-foundational">⚓ Tier 4: Foundational Value</span><br>
        <div class="card-title">#14: IATA Aircraft Cabin Waste Reduction Portal</div>
        <div class="card-subtitle">Category: Eco-Compliance Processing</div>
        <p style='font-size: 16px;'>International rules covering cabin sorting, recycling, and disposing of international bio-waste upon arrival.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps airlines comply with green target goals and international garbage disposal rules at global hubs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to IATA Aircraft Cabin Waste Reduction Portal ↗️", "https://www.iata.org/", use_container_width=True)

    # SUBSECTION D
    st.markdown("### 🌐 IATA Geography & Flight Wellness")

    #15
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#15: IATA Official Coding Engine Search</div>
        <div class="card-subtitle">Category: Aerodromic Location Codes</div>
        <p style='font-size: 16px;'>Search tools and reference guides designed to help students master three-letter city codes like JFK, LHR, and DXB.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Fundamental skill that prevents luggage routing mistakes and speeds up check-in logistics.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to IATA Official Coding Engine Search ↗️", "https://www.iata.org/en/publications/directories/code-search/", use_container_width=True)
    st.write("")

    #16
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#16: TimeAndDate Global Zone Converter Maps</div>
        <div class="card-subtitle">Category: Chronometric Tracking Maps</div>
        <p style='font-size: 16px;'>Time zone charts showing how to calculate local arrival times and track day changes when crossing the International Date Line.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps crews manage flight logs accurately and schedule rest blocks properly on long multi-stop trips.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to TimeAndDate Global Zone Converter Maps ↗️", "https://www.timeanddate.com/worldclock/converter.html", use_container_width=True)
    st.write("")

    #17
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#17: IATA Travel Centre Passport and Visa Requirements</div>
        <div class="card-subtitle">Category: Customs Border Verification</div>
        <p style='font-size: 16px;'>Border rules showing passport validity requirements, mandatory visas, and crew entry rules for different countries.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps crews cross international borders smoothly, avoiding customs issues or entry delays during layovers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to IATA Travel Centre Passport and Visa Requirements ↗️", "https://www.iatatravelcentre.com/", use_container_width=True)
    st.write("")

    #18
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#18: Sterile Flight Deck Rule Operational Compliance</div>
        <div class="card-subtitle">Category: Flight Deck Interaction Integrity</div>
        <p style='font-size: 16px;'>Regulations banning all non-safety communications with the cockpit during low-altitude taxiing, takeoffs, and landings.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents pilot distractions during critical phases of flight, ensuring the flight deck stays completely focused on safety.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Advisory Circular AC 121-32: Sterile Flight Deck ↗️", "https://www.faa.gov/regulations_policies/advisory_circulars/", use_container_width=True)
    st.write("")

    #19
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#19: ICAO Fatigue Risk Management Portal</div>
        <div class="card-subtitle">Category: Human Metrics Risk Assessment</div>
        <p style='font-size: 16px;'>System tracking sheets outlining legal duty limits, minimum rest breaks, and fatigue reporting tools for international crews.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents extreme exhaustion risks by ensuring airline schedules comply with legal safety rest margins.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ICAO Fatigue Risk Management Portal ↗️", "https://www.icao.int/", use_container_width=True)
    st.write("")

    #20
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#20: CDC Traveler's Health Blood Clots Guide</div>
        <div class="card-subtitle">Category: Operational Circulatory Wellness</div>
        <p style='font-size: 16px;'>Leg movement guides and compression advice designed to maintain good blood flow on long-haul segments to prevent DVT.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Lowers blood clot risks from long sitting times, keeping crews safe and healthy across extended flights.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to CDC Traveler's Health Blood Clots Guide ↗️", "https://wwwnc.cdc.gov/travel", use_container_width=True)

    # SUBSECTION E
    st.markdown("### ### 🏥 High-Altitude Medicine & Crash Case Studies")

    #21
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#21: Aerospace Medical Association (AsMA) Publications</div>
        <div class="card-subtitle">Category: High-Altitude Clinical Reference</div>
        <p style='font-size: 16px;'>Clinical reference manuals tracking altitude strains on wounds, heart issues, asthma attacks, and stroke symptoms in pressurized cabins.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Gives crews the medical knowledge needed to treat serious health crises effectively at high cruise altitudes.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Aerospace Medical Association (AsMA) Publications ↗️", "https://www.asma.org/", use_container_width=True)
    st.write("")

    #22
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#22: British Airtours Flight 28M Evacuation Analysis</div>
        <div class="card-subtitle">Category: Hardware Egress Evacuation Study</div>
        <p style='font-size: 16px;'>A safety review of a 1985 engine fire that caused smoke to quickly fill the cabin, slowing down passenger evacuation steps.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Drove major updates in interior safety design, leading to wider exit row paths, clear floor lighting, and fire-resistant seat covers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to UK AAIB Historical Accident Investigation Vault ↗️", "https://www.gov.uk/government/organisations/air-accidents-investigation-branch", use_container_width=True)
    st.write("")

    #23
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#23: Air Canada Flight 797 Technical Evaluation Archive</div>
        <div class="card-subtitle">Category: Structural Lavatory Fire Mitigation</div>
        <p style='font-size: 16px;'>A study of a hidden bathroom fire that spread through wall panels, knocking out power and filling the cabin with thick smoke.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Drove major cabin updates, making lavatory smoke alarms, automatic extinguishers, and path lights mandatory on all planes.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to NTSB Air Canada 797 Technical Evaluation Archive ↗️", "https://www.ntsb.gov/", use_container_width=True)
    st.write("")

    #24
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#24: US Airways Flight 1549 Hudson River Ditching Evacuation</div>
        <div class="card-subtitle">Category: Emergency Command Ditching Matrix</div>
        <p style='font-size: 16px;'>A review of a dual-engine bird strike ditching, showing how fast, orderly cabin teams emptied the plane onto river rafts.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Proves the value of structured training drills, illustrating how perfect command loops make fast water evacuations possible.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to NTSB Hudson Ditching Operational Review ↗️", "https://www.ntsb.gov/", use_container_width=True)
    st.write("")

    #25
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#25: Flight Safety Foundation Cabin Crew Safety Digests</div>
        <div class="card-subtitle">Category: Evolving Structural Safety Analysis</div>
        <p style='font-size: 16px;'>A compilation of modern safety briefings tracking exit injuries, galley cart hazards, and changing cabin equipment standards.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Keeps safety training fresh, ensuring crew knowledge aligns with modern airline safety updates and research.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Flight Safety Foundation Cabin Crew Safety Digests ↗️", "https://flightsafety.org/", use_container_width=True)

# PAGE 5: AIRCRAFT MAINTENANCE HUB
elif st.session_state.page == "Aircraft Maintenance Roadmap":
    st.markdown("## 🛠️ Section 4: Aircraft Maintenance & Engineering (AMT) Hub")
    st.write("Technical manuals, regulatory rulebooks, and student apprenticeship training networks designed to build certified engineering profiles.")
    st.write("---")

    # SUBSECTION A
    st.markdown("### 🥇 Strategic Youth Frameworks & Scholarships")

    #1
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#1: FAA Aviation Handbooks & Manuals (General, Airframe, & Powerplant)</div>
        <div class="card-subtitle">Category: Regulatory Textbooks</div>
        <p style='font-size: 16px;'>The core technical textbooks covering aerodynamics, structural sheet metal, and turbine engine mechanics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Forms the foundational reading material for anyone learning aircraft maintenance and structural engineering.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Handbooks Gateway ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/", use_container_width=True)
    st.write("")

    #2
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#2: EAA AeroEducate Portal</div>
        <div class="card-subtitle">Category: STEM Activity Matrix</div>
        <p style='font-size: 16px;'>An interactive, youth-focused STEM tracking system designed to log hands-on engineering activities.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Connects high schoolers to local manufacturing projects and youth engineering mentors.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to EAA AeroEducate ↗️", "https://www.aeroeducate.org/", use_container_width=True)
    st.write("")

    #3
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#3: Aircraft Electronics Association (AEA) Educational Foundation</div>
        <div class="card-subtitle">Category: Avionics Endowment Grants</div>
        <p style='font-size: 16px;'>A dedicated association platform providing thousands of dollars in scholarships explicitly for high schoolers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Directly offsets the cost of avionics, wiring, and electronics training programs for teens.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AEA Foundation Portal ↗️", "https://aea.net/educationalfoundation/", use_container_width=True)
    st.write("")

    #4
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#4: SkillsUSA Aviation Maintenance Trades</div>
        <div class="card-subtitle">Category: Professional Workforce Pipelines</div>
        <p style='font-size: 16px;'>A structured workforce program providing technical framework guidelines and competitive events for student mechanics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows 16-year-olds to compete in high school divisions for precision assembly and safety wiring.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SkillsUSA Main Site ↗️", "https://www.skillsusa.org/", use_container_width=True)
    st.write("")

    #5
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#5: FAA Safety Team (FAASTeam) Learning Center</div>
        <div class="card-subtitle">Category: Safety Clearance Certificates</div>
        <p style='font-size: 16px;'>The official safety portal hosting hundreds of free courses on human error, tool management, and parts inspections.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Earns teens official industry safety certificates to boost their resumes before turning 18.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAASTeam Online ↗️", "https://www.faasafety.gov/", use_container_width=True)

    # SUBSECTION B
    st.markdown("### 🔩 Core Technical & Industry Resources")

    #6
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#6: Aviation Mechanic Practical Test Standards (PTS)</div>
        <div class="card-subtitle">Category: License Evaluation Parameters</div>
        <p style='font-size: 16px;'>The official testing blueprint detailing the exact practical projects required to clear a mechanic license.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides the direct grading criteria for passing hands-on oral and practical technician exams.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Testing Library ↗️", "https://www.faa.gov/training_testing/testing/", use_container_width=True)
    st.write("")

    #7
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#7: Dynamic Regulatory System (DRS)</div>
        <div class="card-subtitle">Category: Airworthiness Search Protocols</div>
        <p style='font-size: 16px;'>The FAA’s central legal search engine for standard airworthiness certificates, directives, and component limits.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Introduces students to regulatory maintenance law and how to research mandatory aircraft safety recalls.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA DRS System ↗️", "https://drs.faa.gov/", use_container_width=True)
    st.write("")

    #8
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#8: Aviation Maintenance Magazine</div>
        <div class="card-subtitle">Category: Fleet Overhaul Media</div>
        <p style='font-size: 16px;'>A professional trade journal covering automated tooling, composites, and global fleet overhaul trends.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Keeps students updated on commercial MRO (Maintenance, Repair, and Overhaul) corporate operations.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AMTSociety News ↗️", "https://www.aviationmaint.com/", use_container_width=True)
    st.write("")

    #9
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#9: National Aviation Academy (NAA) Training Blog</div>
        <div class="card-subtitle">Category: Operational Hangar Logs</div>
        <p style='font-size: 16px;'>Informative visual breakdowns showing daily life inside turbine maintenance hangars and tool control stations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps teens visualize the daily career workflow of an active heavy-jet maintenance technician.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to NAA Training Portal ↗️", "https://www.naa.edu/", use_container_width=True)
    st.write("")

    #10
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#10: AMT Society Knowledge Center</div>
        <div class="card-subtitle">Category: Physical Craft Practice</div>
        <p style='font-size: 16px;'>A professional forum network detailing industry standard practices for safety wire patterns and sheet metal rivets.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Serves as a peer-vetted knowledge base for perfecting physical trade craft skills.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AMTSociety Hub ↗️", "https://www.aviationmx.org/", use_container_width=True)
    st.write("")

    #11
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#11: Aircraft Component Type Certificate Data Sheets (TCDS)</div>
        <div class="card-subtitle">Category: Structural Build Constraints</div>
        <p style='font-size: 16px;'>The official weight, fuel, and engine limit sheets used to certify exact aircraft build specifications.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Vital for teaching students how to verify if an aircraft modification is legally airworthy.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA TCDS Database ↗️", "https://rgl.faa.gov/", use_container_width=True)
    st.write("")

    #12
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#12: Electronic Code of Federal Regulations (eCFR) Part 43</div>
        <div class="card-subtitle">Category: Maintenance Legality Codes</div>
        <p style='font-size: 16px;'>The baseline federal law defining what constitutes legal maintenance, rebuild alterations, and preventive tasks.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Gives 16-year-olds a clear understanding of what basic fixes a private pilot can legally perform themselves.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to eCFR Part 43 Portal ↗️", "https://www.ecfr.gov/", use_container_width=True)
    st.write("")

    #13
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#13: Aircraft Electronics Association Avionics Magazine</div>
        <div class="card-subtitle">Category: Electrical Computational Systems</div>
        <p style='font-size: 16px;'>Tech tracking articles breaking down modern glass cockpits, wiring setups, and digital radar components.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Focuses heavily on the electrical and computational side of modern avionics engineering.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AEA Avionics News ↗️", "https://www.avionicsnews.com/", use_container_width=True)
    st.write("")

    #14
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#14: Choose Aerospace Curriculum Network</div>
        <div class="card-subtitle">Category: Secondary Training Blueprints</div>
        <p style='font-size: 16px;'>A dedicated high school training network framework providing direct entry paths into certified mechanic academies.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps high schools incorporate standardized aviation maintenance classes directly into teenage class schedules.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Choose Aerospace ↗️", "https://www.chooseaerospace.org/", use_container_width=True)
    st.write("")

    #15
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#15: Northrop Rice Aviation Foundation Grants</div>
        <div class="card-subtitle">Category: Tooling Capital Endowments</div>
        <p style='font-size: 16px;'>A funding system offering specialized tool grants and avionic system scholarships for student technicians.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students buy expensive starting toolsets required for entry-level hangar apprenticeships.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to NRAF Foundation ↗️", "https://www.northropricefoundation.org/", use_container_width=True)
    st.write("")

    #16
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#16: Boeing Technical Apprenticeship Program</div>
        <div class="card-subtitle">Category: Manufacturing Corporate Entry</div>
        <p style='font-size: 16px;'>Corporate outreach pathways showing how high school graduates step directly into assembly line careers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides an actionable alternative to a traditional 4-year degree via direct aerospace manufacturer training.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Boeing Careers Portal ↗️", "https://jobs.boeing.com/", use_container_width=True)
    st.write("")

    #17
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#17: AOPA AMT Career Guide</div>
        <div class="card-subtitle">Category: Industry Deployment Guides</div>
        <p style='font-size: 16px;'>A comprehensive breakdown showing the intersection of general aviation maintenance and commercial airline operations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students choose between working on small flight-school trainers or massive commercial airliners.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AOPA Mechanic Paths ↗️", "https://www.aopa.org/news-and-media/all-index/aviation-maintenance-technician", use_container_width=True)
    st.write("")

    #18
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-foundational">⚓ Tier 4: Foundational Value</span><br>
        <div class="card-title">#18: Aviation Maintenance Technician Society Awards</div>
        <div class="card-subtitle">Category: Continuous Competency Records</div>
        <p style='font-size: 16px;'>A specialized rewards program that logs continuous training milestones for apprentice technicians.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Encourages a culture of lifelong learning by tracking voluntary safety training credits.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA William O'Brien Program ↗️", "https://www.faasafety.gov/AMT/amtinfo/", use_container_width=True)
    st.write("")

    #19
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#19: Engine Components Inc. (ECI) Technical Library</div>
        <div class="card-subtitle">Category: Piston Clearance Mechanics</div>
        <p style='font-size: 16px;'>Free graphic heavy manuals tracking piston engine wear, cylinder rebuilding, and piston clearances.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Excellent visual resource for understanding how internal combustion aircraft engines operate.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ECI Component Guides ↗️", "https://www.asoverhaul.com/", use_container_width=True)
    st.write("")

    #20
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#20: Aviation Institute of Maintenance (AIM) High School Hub</div>
        <div class="card-subtitle">Category: Secondary Academic Matriculation</div>
        <p style='font-size: 16px;'>Offers dual-enrollment class tracking and summer camp options for 16-year-olds exploring technical trades.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows high school juniors to earn college credits toward an airframe license early.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AIM Aviation Hangar ↗️", "https://aviationmaintenance.edu/", use_container_width=True)
    st.write("")

    #21
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#21: Aircraft Mechanics Fraternal Association (AMFA) Education</div>
        <div class="card-subtitle">Category: Professional Guild Connections</div>
        <p style='font-size: 16px;'>Trade union portal providing student mentoring connections with active airline line maintenance mechanics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Connects student technicians with industry professionals to build career networks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AMFA Union System ↗️", "https://www.amfanational.org/", use_container_width=True)
    st.write("")

    #22
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#22: Women in Aviation International (WAI) Technical Scholarships</div>
        <div class="card-subtitle">Category: Targeted Diversity Endowments</div>
        <p style='font-size: 16px;'>Dedicated scholarship network awarding specialized funding blocks for airframe and avionics ratings.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Promotes diversity in the hangar by funding technical training for young women.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to WAI Scholarships Hub ↗️", "https://www.wai.org/scholarships", use_container_width=True)
    st.write("")

    #23
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#23: JSFirm Aviation Maintenance Job Board</div>
        <div class="card-subtitle">Category: Labor Index Metrics</div>
        <p style='font-size: 16px;'>A real-time hiring search engine showing what specific tool proficiencies and certificates are actively in high demand.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows students to spot current market wage trends and identify highly valued technical skills.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to JSFirm Hangar Search ↗️", "https://www.jsfirm.com/", use_container_width=True)
    st.write("")

    #24
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#24: ATP Flight School AMT Pipeline</div>
        <div class="card-subtitle">Category: Fast-Track Infrastructure</div>
        <p style='font-size: 16px;'>Accelerating training program outlines tracking commercial airline fleet support logistics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Illustrates how fast-track training setups transition students rapidly from school to airline careers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ATP AMT Career Program ↗️", "https://atpflightschool.com/amt/", use_container_width=True)
    st.write("")

    #25
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#25: Professional Aviation Maintenance Association (PAMA)</div>
        <div class="card-subtitle">Category: Global Safety Clearinghouses</div>
        <p style='font-size: 16px;'>Core professional network hosting trade webinars and connecting high school chapters to active field events.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Keeps young technicians informed on changing global licensing and regulatory safety updates.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to PAMA National Portal ↗️", "https://www.pama.org/", use_container_width=True)

# PAGE 6: AEROBOT GROUND KNOWLEDGE SYSTEM
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
