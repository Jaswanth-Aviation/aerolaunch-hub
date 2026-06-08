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

# PAGE 2: PILOT HUB (Expanded with ranks #1 to #50)
elif st.session_state.page == "Pilots":
    st.markdown("### 🧭 Student Pilot Flight Matrix")
    st.write("Structured resources built to optimize competitive college applications and accelerate flight training timelines.")
    st.write("")

    # --- TIER 1: FOUNDATIONAL ACADEMICS & CHECKRIDE ESSENTIALS (Ranks #1–10) ---
    st.markdown("#### 🥇 Tier 1: Foundational Academics & Checkride Essentials (Ranks #1–10)")
    
    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #1</span><br>
        <div class="card-title">FAA Pilot’s Handbook of Aeronautical Knowledge (PHAK)</div>
        <div class="card-subtitle">Category: Core Ground School</div>
        <p style='font-size: 16px;'>The definitive textbook covering aerodynamic principles, aircraft systems, flight instruments, weather theory, and basic navigation.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Forms the absolute bedrock of theoretical knowledge required to pass any aviation written exam or oral checkride globally.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Open Textbook Library Repository ↗️", "https://open.umn.edu/opentextbooks", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #2</span><br>
        <div class="card-title">FAA Airplane Flying Handbook (AFH)</div>
        <div class="card-subtitle">Category: Flight Maneuvers</div>
        <p style='font-size: 16px;'>A comprehensive guide focusing on the physical mechanics of flight, including maneuvers, takeoffs, landings, and emergency procedures.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Bridges the gap between classroom theory and real-world stick-and-rudder skills, standardizing flight training maneuvers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Document Gateway ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #3</span><br>
        <div class="card-title">Pilot Institute Free Private Pilot Ground School Primer</div>
        <div class="card-subtitle">Category: Video Course</div>
        <p style='font-size: 16px;'>An introductory video-based course outlining the core requirements, costs, regulations, and basic physics involved in getting a license.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Acts as an accessible, high-yield introductory funnel for student pilots to visualize their entire training timeline before investing capital.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Pilot Institute Portal ↗️", "https://pilotinstitute.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #4</span><br>
        <div class="card-title">Sporty’s Study Buddy Exam Prep Engine</div>
        <div class="card-subtitle">Category: Written Prep</div>
        <p style='font-size: 16px;'>A dynamic, database-driven practice test module that generates authentic practice questions mimicking the actual FAA Private Pilot written test.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Optimizes exam readiness through targeted testing, allowing users to identify weak knowledge areas before taking official exams.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Sporty's Online Prep ↗️", "https://www.sportys.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #5</span><br>
        <div class="card-title">SkyVector Aeronautical Charts</div>
        <div class="card-subtitle">Category: Electronic Navigation</div>
        <p style='font-size: 16px;'>A real-time, global digital plotting tool providing VFR Sectionals, IFR High/Low charts, and live weather overlays.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Essential for mastering flight planning, visual tracking, and understanding complex airspace boundaries from a web browser.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SkyVector Live Map ↗️", "https://skyvector.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #6</span><br>
        <div class="card-title">EASA Private Pilot Syllabus Framework</div>
        <div class="card-subtitle">Category: Global Training Blueprints</div>
        <p style='font-size: 16px;'>The regulatory training blueprint detailing the European Union Aviation Safety Agency's cross-border requirements for flight training.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides international perspective, allowing developers to build curricula compatible with both American and European regulatory bodies.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to EASA Regulations Directory ↗️", "https://www.easa.europa.eu/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #7</span><br>
        <div class="card-title">King Schools Interactive Flight Exam Modules</div>
        <div class="card-subtitle">Category: Interactive Theory</div>
        <p style='font-size: 16px;'>Interactive mini-modules focusing on challenging flight concepts like crosswind components, weight and balance, and airspace restrictions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Simplifies complex mathematical and physics-based aviation principles through proven, memorable visual teaching styles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to King Schools Free Library ↗️", "https://kingschools.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #8</span><br>
        <div class="card-title">Boldmethod Flight Training Quizzes</div>
        <div class="card-subtitle">Category: Scenario Training</div>
        <p style='font-size: 16px;'>Highly visual, scenario-based quizzes addressing real-world aviation challenges, from systems failures to tricky weather scenarios.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Sharpens quick critical thinking and Aeronautical Decision Making (ADM) skills by putting users into simulated pilot dilemmas.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Boldmethod Training Portal ↗️", "https://www.boldmethod.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #9</span><br>
        <div class="card-title">MIT OpenCourseWare: Introduction to Aerospace Engineering</div>
        <div class="card-subtitle">Category: Higher Education STEM</div>
        <p style='font-size: 16px;'>An academic, undergraduate-level course breaking down fluid dynamics, structural engineering, and propulsion physics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides an excellent academic extension for students aiming to understand the advanced engineering principles behind aircraft design.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to MIT OpenCourseWare ↗️", "https://ocw.mit.edu/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-highest">🏆 Rank #10</span><br>
        <div class="card-title">FAA Airman Certification Standards (ACS)</div>
        <div class="card-subtitle">Category: Testing Regulations</div>
        <p style='font-size: 16px;'>The official regulatory document detailing the exact parameters, tolerances, and knowledge areas tested during a pilot practical exam.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Serves as the ultimate grading standard, ensuring pilots know exactly what constitutes a passing or failing performance on a checkride.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FAA Airman Testing Standards ↗️", "https://www.faa.gov/training_testing/testing/acs", use_container_width=True)
    st.write("")


    # --- TIER 2: FLIGHT SIMULATION & COCKPIT FLOW DRILLS (Ranks #11–20) ---
    st.markdown("#### 🎮 Tier 2: Flight Simulation & Cockpit Flow Drills (Ranks #11–20)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #11</span><br>
        <div class="card-title">FlightSim.Com Freeware Aircraft Archive</div>
        <div class="card-subtitle">Category: Virtual Fleet Add-ons</div>
        <p style='font-size: 16px;'>A historic repository offering community-created aircraft models, panels, and realistic custom flight dynamics for desktop simulators.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows students to practice flight decks and cockpit flows for specialized aircraft without purchasing expensive software add-ons.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FlightSim Portal ↗️", "https://www.flightsim.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #12</span><br>
        <div class="card-title">X-Plane Scenery Gateway</div>
        <div class="card-subtitle">Category: Ground Layout Mapping</div>
        <p style='font-size: 16px;'>A collaborative database sharing highly accurate, community-vetted airport layouts and visual environments for flight simulation.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Enables highly realistic airport familiarization and taxi routing practice for students preparing to fly into real-world hubs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to X-Plane Scenery Hub ↗️", "https://gateway.x-plane.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #13</span><br>
        <div class="card-title">FSLTL Live Real-Time Traffic Injection</div>
        <div class="card-subtitle">Category: Airspace Density Injection</div>
        <p style='font-size: 16px;'>An advanced utility that injects real-world, real-time airline traffic and flight tracks directly into flight simulator environments.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Simulates highly realistic, high-density traffic environments to build scan patterns and visual collision-avoidance awareness.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FSLTL Live Traffic Engine ↗️", "https://www.fsltl.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #14</span><br>
        <div class="card-title">SmartCopilot Configurations</div>
        <div class="card-subtitle">Category: Multi-Crew Networks</div>
        <p style='font-size: 16px;'>A software plugin framework enabling shared cockpit operations, letting two users control the same flight simulator aircraft online.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Facilitates virtual multi-crew coordination (MCC) and remote flight instruction exercises with zero hardware footprint.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SmartCopilot Desk ↗️", "https://smartcopilot.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #15</span><br>
        <div class="card-title">FreeChecklists.net Directory</div>
        <div class="card-subtitle">Category: Standard Operating Procedures</div>
        <p style='font-size: 16px;'>A massive crowdsourced directory hosting standard operating checklists for hundreds of general aviation and commercial aircraft.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches structural discipline by getting student pilots into the habit of using verified, sequential safety checklists.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FreeChecklists Repository ↗️", "https://www.freechecklists.net/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #16</span><br>
        <div class="card-title">SimBrief Enterprise Dispatch Engine</div>
        <div class="card-subtitle">Category: Operational Flight Planning</div>
        <p style='font-size: 16px;'>A professional-grade web utility that generates highly realistic virtual flight plans, fuel calculations, and airline operational release documents.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Introduces students to advanced airline dispatching, flight planning, and route fuel management logistics.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SimBrief Routing Tool ↗️", "https://www.simbrief.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #17</span><br>
        <div class="card-title">SimToolkitPro Flight Ecosystem</div>
        <div class="card-subtitle">Category: Virtual Electronic Flight Bag</div>
        <p style='font-size: 16px;'>An all-in-one electronic flight bag (EFB) simulator app that tracks virtual flights, maps live legs, and stores training history data.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides students with a free tool that acts like an interactive navigation log and flight analyzer.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to SimToolkitPro App ↗️", "https://simtoolkitpro.co.uk/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #18</span><br>
        <div class="card-title">Little Navmap Open-Source Navigation</div>
        <div class="card-subtitle">Category: Open Mapping Tools</div>
        <p style='font-size: 16px;'>A free, open-source flight planner and moving map display featuring airport diagrams, wind overlays, and elevation profiles.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Perfect for introducing cross-country flight planning, vector tracks, and airspace boundary rules without recurring costs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Little Navmap GitHub ↗️", "https://github.com/albar965/littlenavmap", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #19</span><br>
        <div class="card-title">VOR Navigation Web App Simulator</div>
        <div class="card-subtitle">Category: Instrument Ground Training</div>
        <p style='font-size: 16px;'>An interactive, browser-based graphical utility for understanding how instrument needles move relative to ground stations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Solves one of the hardest conceptual hurdles for new pilots: visualizing relative orientation using old-school radio navigation tools.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to LuizMonteiro VOR Sim ↗️", "https://www.luizmonteiro.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-high">⚡ Rank #20</span><br>
        <div class="card-title">Garmin G1000 Glass Cockpit Interface Guide</div>
        <div class="card-subtitle">Category: Avionics Frameworks</div>
        <p style='font-size: 16px;'>Official training handbooks breaking down the structure, flight instrument screens, and map menus of modern integrated glass avionics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Accelerates situational awareness by allowing pilots to master digital avionics navigation menus before stepped training flights.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Garmin Digital Manuals ↗️", "https://www.garmin.com/support/manuals/", use_container_width=True)
    st.write("")


    # --- TIER 3: AVIATION METEOROLOGY & WEATHER TRACKING (Ranks #21–30) ---
    st.markdown("#### 🌤️ Tier 3: Aviation Meteorology & Weather Tracking (Ranks #21–30)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #21</span><br>
        <div class="card-title">NOAA Aviation Weather Center (AWC)</div>
        <div class="card-subtitle">Category: Live Telemetry Metrics</div>
        <p style='font-size: 16px;'>The central US portal providing METARs, TAFs, SIGMETs, convective outlooks, and satellite imagery for active flights.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> The primary operational portal for pulling official pre-flight weather data and learning real-time weather monitoring.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Aviation Weather Live ↗️", "https://aviationweather.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #22</span><br>
        <div class="card-title">FAA Aviation Weather Handbook (FAA-H-8083-28)</div>
        <div class="card-subtitle">Category: Theoretical Meteorology</div>
        <p style='font-size: 16px;'>A consolidated textbook on weather theory, atmospheric circulation, icing, wind shear, and weather observation systems.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Combines multiple technical weather advisories into one master textbook for comprehensive ground study.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Regulatory Handbooks ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #23</span><br>
        <div class="card-title">Bad Elf METAR/TAF Decoding Tool</div>
        <div class="card-subtitle">Category: Code Translation Utilities</div>
        <p style='font-size: 16px;'>A clean web tool that translates condensed, coded text weather statements into plain, easily understood descriptions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Speeds up weather literacy for beginners learning to decode critical variables like wind speed, ceiling heights, and pressure shifts.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Bad Elf Decoder ↗️", "https://bad-elf.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #24</span><br>
        <div class="card-title">Windy.com Advanced Weather Interface</div>
        <div class="card-subtitle">Category: Global Dynamic Visualization</div>
        <p style='font-size: 16px;'>A highly detailed global weather visualizer displaying live wind vector fields, cloud ceilings, fronts, and radar layers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Excellent for showing students how micro-weather structures, jet streams, and wind patterns cross vast geographic lines.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Windy Interactive Radar ↗️", "https://www.windy.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #25</span><br>
        <div class="card-title">National Weather Service JetStream Online Academy</div>
        <div class="card-subtitle">Category: Systemic Climatology</div>
        <p style='font-size: 16px;'>An online training dashboard explaining atmospheric structure, jet stream paths, storms, and severe weather risks.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Breaks down complex planetary weather systems into simple, digestible training visuals for basic self-study.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("NWS JetStream Portal ↗️", "https://www.weather.gov/jetstream/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #26</span><br>
        <div class="card-title">Skew-T Log-P Atmospheric Diagram Guide</div>
        <div class="card-subtitle">Category: Advanced Thermodynamics</div>
        <p style='font-size: 16px;'>Technical learning modules detailing how to read complex vertical thermodynamic atmospheric sounding charts.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches advanced pilots and dispatchers how to predict cloud formations, icing levels, and convective stability trends.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("MetEd COMET Modules ↗️", "https://www.meted.ucar.edu/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #27</span><br>
        <div class="card-title">University of Wyoming Weather Data Archives</div>
        <div class="card-subtitle">Category: Research Telemetry Data</div>
        <p style='font-size: 16px;'>A repository of raw atmospheric soundings and historical upper-air weather data collected via global weather balloons.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Useful for research assignments analyzing past weather anomalies or creating historical flight-planning challenges.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("UWyo Sounding Directory ↗️", "http://weather.uwyo.edu/upperair/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #28</span><br>
        <div class="card-title">Coordinated Icing & Turbulence Forecast Models</div>
        <div class="card-subtitle">Category: Hazard Vector Prediction</div>
        <p style='font-size: 16px;'>Interactive graphical models mapping structural icing hazards, clear-air turbulence, and cloud boundaries by altitude.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Vital for teaching instrument-rated pilots how to safely map out altitude changes to avoid structural icing hazards.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("AWC Forecast Models ↗️", "https://aviationweather.gov/gfa", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #29</span><br>
        <div class="card-title">Climate & Micro-Meteorology Aviation Guides</div>
        <div class="card-subtitle">Category: Microclimatic Safety Matrices</div>
        <p style='font-size: 16px;'>A structured reference library highlighting specialized local weather hazards like mountain waves, coastal fog, and microbursts.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Builds localized safety awareness, preventing terrain-induced flight incidents during cross-country training.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Meteorology Hub ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #30</span><br>
        <div class="card-title">NASA/Ames Aviation Safety Reporting System (ASRS)</div>
        <div class="card-subtitle">Category: Risk Management Logs</div>
        <p style='font-size: 16px;'>A voluntary, anonymous reporting database detailing real-world flight crew errors, unexpected weather encounters, and aircraft malfunctions.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows students to study genuine, unfiltered human-error case studies to foster a culture focused on proactive safety management.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("NASA ASRS System Database ↗️", "https://asrs.arc.nasa.gov/", use_container_width=True)
    st.write("")


    # --- TIER 4: RADIO TELEPHONY & COMMUNICATION FRAMEWORKS (Ranks #31–40) ---
    st.markdown("#### 🎙️ Tier 4: Radio Telephony & Communication Frameworks (Ranks #31–40)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #31</span><br>
        <div class="card-title">LiveATC.net Global Audio Network</div>
        <div class="card-subtitle">Category: Real-time Audio Monitoring</div>
        <p style='font-size: 16px;'>A network streaming live radio traffic from thousands of air traffic control facilities and towers worldwide.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students bridge the gap between textbook terms and real-world audio comprehension, improving listening habits early on.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("LiveATC Global Feeds ↗️", "https://www.liveatc.net/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #32</span><br>
        <div class="card-title">PlaneEnglish: ARSim Free Training Tier</div>
        <div class="card-subtitle">Category: Audio Analysis Modules</div>
        <p style='font-size: 16px;'>A web-accessible version of an AI-driven sandbox that analyzes and scores radio phrases for rhythm, structure, and accuracy.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Builds vocal muscle memory and reduces microphone anxiety through structured, interactive speaking exercises.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("PlaneEnglish Classroom ↗️", "https://planeenglishsim.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #33</span><br>
        <div class="card-title">PilotEdge Public Training Workshops</div>
        <div class="card-subtitle">Category: Strategic Phraseology Archives</div>
        <p style='font-size: 16px;'>Comprehensive video recordings and webinars focusing on radio communications, instrument departures, and busy airspace routing.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Explains why controllers use specific phrases, teaching pilots how to communicate clearly and efficiently.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("PilotEdge Video Archive ↗️", "https://www.pilotedge.net/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #34</span><br>
        <div class="card-title">VATSIM Pilot Academy Phrasing Guide</div>
        <div class="card-subtitle">Category: Practical Simulation Logs</div>
        <p style='font-size: 16px;'>A curriculum path that walks virtual pilots through standard ICAO/FAA phraseology, from clearance delivery to complex ground maneuvers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Standardizes basic radio habits, helping students practice on online simulation networks before flying for real.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("VATSIM Pilot Training Academy ↗️", "https://my.vatsim.net/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #35</span><br>
        <div class="card-title">FAA AIM Chapter 4: Air Traffic Control Procedures</div>
        <div class="card-subtitle">Category: Federal Regulatory Manuals</div>
        <p style='font-size: 16px;'>The regulatory chapter defining official communication standards, radar services, transponder use, and airport operations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides the legal guidelines for pilot-to-controller communications, establishing the rules of the road for public airspace.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Aeronautical Information Manual ↗️", "https://www.faa.gov/air_traffic/publications/atpubs/aim_html/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #36</span><br>
        <div class="card-title">CAA CAP 413 Radiotelephony Manual (UK/Europe)</div>
        <div class="card-subtitle">Category: International Standardization Matrices</div>
        <p style='font-size: 16px;'>The definitive guide for UK and European radio procedures, illustrating the exact verbal sequences used outside the US.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Crucial for students seeking an international career, highlighting major differences between American and European radio terms.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("UK CAA Publication Library ↗️", "https://www.caa.co.uk/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #37</span><br>
        <div class="card-title">SayIntentions.AI Free Trial Module</div>
        <div class="card-subtitle">Category: AI Synthesizer Sandboxes</div>
        <p style='font-size: 16px;'>A conversational sandbox tool utilizing artificial intelligence to simulate real-time, unstructured conversations with controllers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides a safe, pressure-free environment to practice speaking with air traffic control from home.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SayIntentions Web Simulator ↗️", "https://sayintentions.ai/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #38</span><br>
        <div class="card-title">LiveATC Audio Archive Transcription Worksheets</div>
        <div class="card-subtitle">Category: Transcription Exercise Repositories</div>
        <p style='font-size: 16px;'>A searchable database where users can download archived audio clips from notable aviation events and traffic peaks.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Allows teachers to build listening comprehension exercises using real historical air traffic recordings.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("LiveATC Audio Archive Search ↗️", "https://www.liveatc.net/archive.php", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #39</span><br>
        <div class="card-title">Aviation Phonetic Alphabet & Numeric Pronunciation Decks</div>
        <div class="card-subtitle">Category: Baseline Articulation Utilities</div>
        <p style='font-size: 16px;'>A specialized learning guide focused on the alpha-numeric pronunciation standards used to prevent miscommunications.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Instills basic communication habits, ensuring alphanumeric values remain clear over noisy radio channels.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("AOPA Phonetic Study Cards ↗️", "https://www.aopa.org/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #40</span><br>
        <div class="card-title">Lost Communications Procedures Manual</div>
        <div class="card-subtitle">Category: Backup Systems Failures</div>
        <p style='font-size: 16px;'>A structured reference outline detailing pilot actions, transponder codes, and route tracking when two-way radio contact is lost.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prepares pilots for electrical or radio failures, ensuring safe routing under regulatory backup frameworks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Lost Communications ↗️", "https://skybrary.aero/articles/lost-communications", use_container_width=True)
    st.write("")


    # --- TIER 5: NAVIGATION, FLIGHT PLANNING & DEAD RECKONING (Ranks #41–50) ---
    st.markdown("#### 📐 Tier 5: Navigation, Flight Planning & Dead Reckoning (Ranks #41–50)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #41</span><br>
        <div class="card-title">Open-Source Digital E6B Flight Computer</div>
        <div class="card-subtitle">Category: Vector Math Software</div>
        <p style='font-size: 16px;'>A browser-based version of the traditional circular slide rule used to calculate wind corrections, fuel burn, and groundspeed.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students master manual navigation math without forcing them to buy physical equipment right away.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Online E6B Emulator ↗️", "https://onlinee6b.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #42</span><br>
        <div class="card-title">SkyVector Flight Plan Matrix Developer</div>
        <div class="card-subtitle">Category: Virtual Navigation Logs</div>
        <p style='font-size: 16px;'>An interactive navigation log tool that automatically calculates headings, leg times, and distances along a customized vector path.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Introduces the core layout of standard navigation logs, showing how wind vectors shift magnetic courses.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SkyVector Flight Planner ↗️", "https://skyvector.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #43</span><br>
        <div class="card-title">FAA Navigation Handbook (FAA-H-8083-16A)</div>
        <div class="card-subtitle">Category: Foundational Plotting Methods</div>
        <p style='font-size: 16px;'>A specialized textbook covering pilotage, dead reckoning, ground based radio aids, and modern global satellite networks.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Offers an all-in-one guide to legacy and modern navigation methods, building a strong conceptual foundation.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Nav Operational Manual ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #44</span><br>
        <div class="card-title">Great Circle Mapper Navigation Tool</div>
        <div class="card-subtitle">Category: Curved Earth Projections</div>
        <p style='font-size: 16px;'>A path visualizer that plots the geometrically shortest route across the Earth's curved surface between any two global airports.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students understand long-range routing mechanics, showing why high-latitude global paths curve on flat maps.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("GCMap Engine ↗️", "http://www.gcmap.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #45</span><br>
        <div class="card-title">Time-Distance-Speed Calculation Sheets</div>
        <div class="card-subtitle">Category: Operational Geometry Layouts</div>
        <p style='font-size: 16px;'>A collection of structured navigation logs designed to help students manually calculate fuel consumption, groundspeed, and arrival times.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Builds underlying safety habits by ensuring pilots can manually calculate flight telemetry if digital tools fail.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("CFI Notebook Nav Logs ↗️", "https://www.cfinotebook.net/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #46</span><br>
        <div class="card-title">Pilotage Landmark Identification Guides</div>
        <div class="card-subtitle">Category: Terrestrial Feature Reference</div>
        <p style='font-size: 16px;'>A visual handbook explaining how to identify physical land features, towers, roads, and waterways on sectional charts.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Improves basic VFR visual navigation skills, preventing students from becoming overly dependent on GPS readouts.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA VFR Chart Guide ↗️", "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/vfr/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #47</span><br>
        <div class="card-title">IFR Low Altitude Enroute Navigation Manuals</div>
        <div class="card-subtitle">Category: Enroute Airway Fixes</div>
        <p style='font-size: 16px;'>Detailed reference manuals explaining low-altitude enroute airway tracks, intersection fixes, and minimum instrument altitudes.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prepares advanced students to transition from visual flight rules to structured instrument enroute environments.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Digital IFR Products ↗️", "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/ifr/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #48</span><br>
        <div class="card-title">Magnetic Compass Error Simulation Web Tool</div>
        <div class="card-subtitle">Category: Kinematic Deviation Simulators</div>
        <p style='font-size: 16px;'>An online tracking sheet and guide illustrating compass errors like variation, deviation, dip, and turning anomalies.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Demystifies old-school backup compass issues, teaching students how to read actual headings during steep turns.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Magnetic Compass ↗️", "https://skybrary.aero/articles/magnetic-compass", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #49</span><br>
        <div class="card-title">Airspace Boundary Distance & Safe Vertical Buffers</div>
        <div class="card-subtitle">Category: Regulatory Vector Clearance</div>
        <p style='font-size: 16px;'>An illustrated guide breaking down the minimum clearance requirements and vertical safety buffers around busy controlled airspaces.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps prevent costly regulatory violations by teaching students how to steer clear of major commercial corridors.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Airspace Design Classifications ↗️", "https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap3_section_1.html", use_container_width=True)

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
