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
    st.write("")


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
    st.markdown("### 🎙️ Air Traffic Control Vector Matrix")
    st.write("Professional simulation tracks and phraseology baselines designed to secure federal placement pathways.")
    st.write("")

    # Tier 1
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

    # Tier 2 - FAA Manuals
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

    # Tier 2 - LiveATC
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

# PAGE 4: AEROBOT GROUND KNOWLEDGE SYSTEM
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
