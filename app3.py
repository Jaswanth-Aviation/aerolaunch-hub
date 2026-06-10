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

nav_cols = st.columns(7)

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
    
    # --- ADDED: ABOUT THE FOUNDER SECTION ---
    st.markdown("### 🧑‍✈️ About the Founder")
    
    # Create two columns to separate your image and description neatly
    about_col1, about_col2 = st.columns([1, 4])
    
    with about_col1:
        # Renders your uploaded image securely
        st.image("IMG_5663.jpg", use_container_width=True)
        
    with about_col2:
        # Formatted narrative statement next to the image matching the theme
        st.markdown("""
        <div class="resource-card" style="margin-bottom: 0px; height: 100%;">
            <div class="card-title" style="color: #0f172a !important; font-size: 24px;">Jaswanth Mallareddi</div>
            <div class="card-subtitle">Founder & Developer</div>
            <p style='font-size: 17px; line-height: 1.6;'>
                I am Jaswanth Mallareddi, a 16-year-old who is deeply interested in aviation! I wanted to give 
                valuable opportunities to other future aviation industry students who will turn 16 soon. 
                I have set up 25 high-quality websites for each section of the aviation industry provided, 
                so I hope it is helpful for all you future aviation students!
            </p>
        </div>
        """, unsafe_allow_html=True)

# PAGE 2: PILOT HUB
elif st.session_state.page == "Pilots":
    st.markdown("## 🧭 Section 1: The Pilot Hub")
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
    st.markdown("## 🎙️ Section 2: Air Traffic Control")
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
    st.markdown("## 🛒 Section 3: Flight Attendant / Air Hostess Hub")
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

# PAGE 5: AIRCRAFT MAINTENANCE HUB
elif st.session_state.page == "Maintenance":
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

# PAGE 6: DRONE LOGISTICS HUB
elif st.session_state.page == "Drone":
    st.markdown("## 🛸 Section 5: Uncrewed Aerial Systems (UAS) & Drone Logistics Hub")
    st.write("Autonomous systems programming, remote flight rules, and logistics clearinghouses engineered to deploy unmanned commercial solutions.")
    st.write("---")

    # SUBSECTION A
    st.markdown("### 🥇 Strategic Foundational Core Assets")

    #1
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#1: EAA AeroEducate Portal</div>
        <div class="card-subtitle">Category: Secondary Academic Tracking</div>
        <p style='font-size: 16px;'>High school STEM activity tracker focusing on drone structural assemblies and programmatic flight paths.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Integrates uncrewed flight logic into foundational high school engineering tasks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to EAA AeroEducate Portal ↗️", "https://www.aeroeducate.org/", use_container_width=True)
    st.write("")

    #2
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#2: Aircraft Electronics Association (AEA) Educational Foundation</div>
        <div class="card-subtitle">Category: Technical Avionics Grants</div>
        <p style='font-size: 16px;'>Funding portal expanding into drone avionics, sensor arrays, and remote frequency tracking certifications.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides unique funding for students building custom autonomous radio telemetry hardware.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AEA Foundation Portal ↗️", "https://aea.net/educationalfoundation/", use_container_width=True)
    st.write("")

    #3
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#3: NOAA Aviation Weather Center (AWC)</div>
        <div class="card-subtitle">Category: Low-Altitude Micro-Meteorology</div>
        <p style='font-size: 16px;'>Real-time wind velocity, icing levels, and cloud ceiling tracker required for safe low-altitude drone operations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Critical for avoiding micro-meteorological wind shear that could crash light consumer drones.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Aviation Weather Live Map ↗️", "https://aviationweather.gov/", use_container_width=True)
    st.write("")

    #4
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#4: SkyVector Aeronautical Charts</div>
        <div class="card-subtitle">Category: Low-Altitude Airspace Boundaries</div>
        <p style='font-size: 16px;'>Interactive digital VFR charts mapping out airport airspace rings that commercial drones must avoid or clear.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Essential for learning how to read airspace classes to prevent illegal drone flights near airports.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SkyVector Plotter ↗️", "https://skyvector.com/", use_container_width=True)
    st.write("")

    #5
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#5: NTSB Aviation Investigation Search</div>
        <div class="card-subtitle">Category: Incident Case Studies</div>
        <p style='font-size: 16px;'>The federal incident database tracking commercial drone flyaways, systemic battery failures, and airspace near-misses.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches students how hardware failure trends directly alter commercial drone flight regulations.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to NTSB CAROL Query System ↗️", "https://www.ntsb.gov/", use_container_width=True)

    # SUBSECTION B
    st.markdown("### 🎮 Drone Flight Rules & Programming")

    #6
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#6: FAA Recreational UAS Safety Test (TRUST)</div>
        <div class="card-subtitle">Category: Basic Safety Certifications</div>
        <p style='font-size: 16px;'>The mandatory federal safety test that 16-year-olds can take online for free to legalize recreational flights.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> The immediate, legal entry-level credential needed before a teenager can fly any hobby drone outside.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA TRUST Gateway ↗️", "https://www.faa.gov/uas/recreational_flyers/knowledge_test_updates", use_container_width=True)
    st.write("")

    #7
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#7: FAA Part 107 Small UAS Remote Pilot Study Guide</div>
        <div class="card-subtitle">Category: Commercial License Frameworks</div>
        <p style='font-size: 16px;'>The official government framework covering radio signals, loading limits, and airspace restrictions for drone pilots.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Serves as the master study text for earning a commercial drone license at the legal minimum age of 16.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Uncrewed Systems Hub ↗️", "https://www.faa.gov/uas", use_container_width=True)
    st.write("")

    #8
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#8: Drone Pilot Ground School Free Resources</div>
        <div class="card-subtitle">Category: Commercial Test Preparation</div>
        <p style='font-size: 16px;'>High-yield visual flashcards and practice quizzes prepping high schoolers for the official Part 107 commercial test.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Speeds up exam prep through specialized practice tools designed for young learners.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to UAV Coach Training ↗️", "https://uavcoach.com/", use_container_width=True)
    st.write("")

    #9
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#9: QGroundControl Autonomous Mission Planner</div>
        <div class="card-subtitle">Category: Open-Source Mission Logic</div>
        <p style='font-size: 16px;'>The open-source manual teaching students how to code automatic waypoint flight maps and geographic boundary fences.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Builds programmatic skills in autonomous delivery mapping and automated grid survey flying.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to QGroundControl Project ↗️", "https://qgroundcontrol.com/", use_container_width=True)
    st.write("")

    #10
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#10: UAV Coach Community Forums</div>
        <div class="card-subtitle">Category: Moderated Operator Ecosystems</div>
        <p style='font-size: 16px;'>A safe, moderated network where young operators ask hardware optimization questions and discuss camera setups.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Connects hobbyists with seasoned commercial remote pilots running active mapping businesses.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to UAV Coach Community ↗️", "https://community.uavcoach.com/", use_container_width=True)
    st.write("")

    #11
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#11: FAA DroneZone Portal</div>
        <div class="card-subtitle">Category: Asset Registry Infrastructure</div>
        <p style='font-size: 16px;'>The official dashboard used to register hardware assets, apply for altitude waivers, and report operations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches regulatory discipline by introducing students to official government asset registration systems.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA DroneZone ↗️", "https://faadronezone-access.faa.gov/", use_container_width=True)
    st.write("")

    #12
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#12: Aloft Air Control (LAANC Authorization)</div>
        <div class="card-subtitle">Category: Real-Time Airspace Clearance</div>
        <p style='font-size: 16px;'>A live platform used to request near-instant automated clearances to fly inside airport airspace rings.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Demonstrates how modern digital automation interfaces with air traffic control systems in real-time.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Aloft Remote Ops ↗️", "https://www.aloft.ai/", use_container_width=True)
    st.write("")

    #13
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#13: Pix4D Drone Mapping Academy</div>
        <div class="card-subtitle">Category: Industrial Geolocation Data</div>
        <p style='font-size: 16px;'>Free entry-level guides explaining how drones stitch together aerial photographs to construct 3D terrain models.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Bridges the gap between basic stick-and-rudder flying and high-paying industrial data mapping careers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Pix4D Training ↗️", "https://www.pix4d.com/education", use_container_width=True)
    st.write("")

    #14
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#14: DroneDeploy Educational Resources</div>
        <div class="card-subtitle">Category: Structural Sector Applications</div>
        <p style='font-size: 16px;'>Classroom layout modules tracking drone data use across modern agriculture, surveying, and thermal rescue tasks.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Shows students how uncrewed aviation is actively transforming traditional non-aviation industries.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to DroneDeploy System ↗️", "https://www.dronedeploy.com/", use_container_width=True)
    st.write("")

    #15
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#15: ArduPilot Open-Source Autopilot Software</div>
        <div class="card-subtitle">Category: Flight Controller Logic</div>
        <p style='font-size: 16px;'>Comprehensive software documentation teaching teens how to configure open-source code for custom drone frames.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Promotes hands-on robotics skills by demonstrating how software logic stabilizes multi-rotor systems.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ArduPilot Project Site ↗️", "https://ardupilot.org/", use_container_width=True)
    st.write("")

    #16
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#16: MultiGP Drone Racing League</div>
        <div class="card-subtitle">Category: Avionics Flight Maneuvers</div>
        <p style='font-size: 16px;'>The global competitive network tracking local FPV (First Person View) racing clubs and custom-built frame events.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Sharpens high-speed reflex coordination and deepens understanding of radio frequency management.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to MultiGP League Portal ↗️", "https://www.multigp.com/", use_container_width=True)
    st.write("")

    #17
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#17: Commercial UAV News</div>
        <div class="card-subtitle">Category: Uncrewed Fleet Overviews</div>
        <p style='font-size: 16px;'>Industry news tracking cargo delivery networks, automated flight laws, and medical drone distribution systems.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students identify active market sectors, such as package delivery logistics and infrastructure inspection.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Commercial UAV Portal ↗️", "https://www.commercialuavnews.com/", use_container_width=True)
    st.write("")

    #18
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-foundational">⚓ Tier 4: Foundational Value</span><br>
        <div class="card-title">#18: ASTM International Uncrewed Systems Standards</div>
        <div class="card-subtitle">Category: Hardware Quality Controls</div>
        <p style='font-size: 16px;'>Universal manufacturing criteria covering drone parachute safety systems, remote tracking signals, and build limits.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches engineering students the standardization rules required to sell consumer hardware globally.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to ASTM UAS Catalog ↗️", "https://www.astm.org/", use_container_width=True)
    st.write("")

    #19
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Tier 1: Highest Value</span><br>
        <div class="card-title">#19: FAA B4UFLY Airspace Awareness App</div>
        <div class="card-subtitle">Category: Structural Safety Geofencing</div>
        <p style='font-size: 16px;'>An interactive map tool that uses your phone's GPS to show local flight rules and temporary flight restrictions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides an immediate pre-flight safety check to prevent accidental violations of temporary airspace bans.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Safety Geofencing ↗️", "https://www.faa.gov/uas/recreational_flyers/b4ufly", use_container_width=True)
    st.write("")

    #20
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#20: Association for Unmanned Vehicle Systems International (AUVSI)</div>
        <div class="card-subtitle">Category: Professional Guild Connections</div>
        <p style='font-size: 16px;'>The primary trade association tracking drone logistics jobs, legal frameworks, and global autonomy breakthroughs.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Offers a broad view of international uncrewed robotics trends across air, land, and sea.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AUVSI Network ↗️", "https://www.auvsi.org/", use_container_width=True)
    st.write("")

    #21
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#21: Women and Drones Education Platform</div>
        <div class="card-subtitle">Category: Targeted Diversity Endowments</div>
        <p style='font-size: 16px;'>Focuses on STEM high school outreach, offering specialized scholarships and professional flight mentoring for girls.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Supports gender diversity in autonomous aviation through targeted youth development programs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Women and Drones Hub ↗️", "https://womenanddrones.com/", use_container_width=True)
    st.write("")

    #22
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#22: Center for the Study of the Drone at Bard</div>
        <div class="card-subtitle">Category: Academic Policy Research</div>
        <p style='font-size: 16px;'>An academic tracking clearinghouse posting deep research on how military and consumer drones impact global safety.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Encourages critical thinking regarding the ethical, legal, and privacy implications of drone surveillance.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Bard Drone Center ↗️", "https://dronecenter.bard.edu/", use_container_width=True)
    st.write("")

    #23
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-foundational">⚓ Tier 4: Foundational Value</span><br>
        <div class="card-title">#23: Drone-Made Global Mapping Regulations</div>
        <div class="card-subtitle">Category: Transnational Legal Indices</div>
        <p style='font-size: 16px;'>A comprehensive index listing drone travel rules and legal pilot parameters for nearly every country.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Vital for travel content creators and international drone operators checking foreign legal limits.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Drone-Made Travel Hub ↗️", "https://www.drone-made.com/", use_container_width=True)
    st.write("")

    #24
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Tier 3: Medium Value</span><br>
        <div class="card-title">#24: InterDrone Educational Archive</div>
        <div class="card-subtitle">Category: Strategic Expert Panels</div>
        <p style='font-size: 16px;'>Access to recorded panels discussing autonomous drone fleets, machine vision tracking, and engineering setups.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Exposes high schoolers to expert opinions on the future trajectory of drone fleet logistics.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to InterDrone Platform ↗️", "https://interdrone.com/", use_container_width=True)
    st.write("")

    #25
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Tier 2: High Value</span><br>
        <div class="card-title">#25: DartDrone Training Resources</div>
        <div class="card-subtitle">Category: Enterprise Structural Operations</div>
        <p style='font-size: 16px;'>Free diagnostic test tracks and industry briefs analyzing commercial drone business setups and insurance options.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches young entrepreneurs how to structure a legal drone photography or inspection business safely.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to DartDrones Online ↗️", "https://www.dartdrones.com/", use_container_width=True)

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
