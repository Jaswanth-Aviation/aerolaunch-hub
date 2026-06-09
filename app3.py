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

# PAGE 2: PILOT HUB
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
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #50</span><br>
        <div class="card-title">Alternate Airport Selection Rubrics</div>
        <div class="card-subtitle">Category: Alternative Strategic Landing Sites</div>
        <p style='font-size: 16px;'>A regulatory decision matrix defining when an alternate airport is legally required due to poor weather forecasts at the primary destination.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Instills a proactive safety mindset by teaching students how to plan safe, legal backup landing sites for every trip.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Federal Aviation Regulations Part 91 ↗️", "https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-91", use_container_width=True)
    st.write("")

    # --- TIER 6: AERODYNAMICS & PRINCIPLES OF FLIGHT (Ranks #51–60) ---
    st.markdown("#### 📐 Tier 6: Aerodynamics & Principles of Flight (Ranks #51–60)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #51</span><br>
        <div class="card-title">NASA Glenn Research Center: Aerodynamics Portal</div>
        <div class="card-subtitle">Category: Lift Production Physics</div>
        <p style='font-size: 16px;'>A collection of educational guides and digital model tools covering lift production, drag equations, and fluid mechanics.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides high-quality, scientifically sound resources to help students understand the physics behind wing lift generation.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("NASA Beginner's Guide to Aerodynamics ↗️", "https://www.nasa.gov/glenn-research-center/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #52</span><br>
        <div class="card-title">The Science of Stalls & Angle of Attack (AoA)</div>
        <div class="card-subtitle">Category: Critical Envelope Protection</div>
        <p style='font-size: 16px;'>Safety bulletins and technical briefs explaining air separation physics when an airframe exceeds its critical angle of attack.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Critical for loss-of-control prevention, teaching pilots how to spot and recover from stalls before safety is compromised.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Aviation Safety Stall Manuals ↗️", "https://www.faa.gov/pilots/safety", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #53</span><br>
        <div class="card-title">Lift-to-Drag ($L/D\\text{ Max}$) Ratio Calculation Guides</div>
        <div class="card-subtitle">Category: Optimal Glide Kinematics</div>
        <p style='font-size: 16px;'>An engineering breakdown showing the sweet spot between lift and total drag, which determines an aircraft's best glide speed.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches pilots how to squeeze out maximum glide distance during unexpected engine failures, maximizing emergency landing options.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Principles of Flight ↗️", "https://skybrary.aero/articles/principles-of-flight", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #54</span><br>
        <div class="card-title">Left-Turning Tendencies Training Systems</div>
        <div class="card-subtitle">Category: Asymmetric Torque Matrices</div>
        <p style='font-size: 16px;'>Technical guides analyzing the four aerodynamic forces (torque, p-factor, gyroscopic precession, spiraling slipstream) that pull propeller planes left.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Improves physical stick-and-rudder handling, teaching pilots how to apply timely rudder inputs during high-power climbs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA PHAK Aerodynamics Chapter ↗️", "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #55</span><br>
        <div class="card-title">Boundary Layer Control & Wing Design Textbooks</div>
        <div class="card-subtitle">Category: Fluid Dynamics Structural Files</div>
        <p style='font-size: 16px;'>Research reports examining laminar flow, wing vortex drag, and how flaps and slats alter overall aerodynamic profiles.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Connects airplane handling directly to structural wing engineering, deepening mechanical knowledge.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("NASA Technical Reports Server ↗️", "https://ntrs.nasa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #56</span><br>
        <div class="card-title">Maneuvering Speed ($V_A$) & Structural Load Limits</div>
        <div class="card-subtitle">Category: Stress Envelope Tolerances</div>
        <p style='font-size: 16px;'>Safety materials explaining how structural load factors change with gross weight, airspeed, and sharp control inputs.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents structural failures by teaching pilots never to exceed calculated maneuvering speeds in turbulent air.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("AOPA Structural Envelope Tracking ↗️", "https://www.aopa.org/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #57</span><br>
        <div class="card-title">Ground Effect Aerodynamic Matrix Models</div>
        <div class="card-subtitle">Category: Ground Buffer Vortices</div>
        <p style='font-size: 16px;'>Explains the reduction in vortex drag when an airplane flies close to the runway surface, which can cause floating during landings.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents premature takeoffs and long runway floating by teaching students how ground cushion dynamics change lift.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Ground Effect Physics ↗️", "https://skybrary.aero/articles/ground-effect", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #58</span><br>
        <div class="card-title">Longitudinal, Lateral, and Directional Stability Files</div>
        <div class="card-subtitle">Category: Equilibrium Center Profiles</div>
        <p style='font-size: 16px;'>Analyses covering how center of gravity placement changes an airframe's natural pitch, roll, and yaw stability.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches the safety risks of improper cargo loading, showing how tail-heavy configurations degrade stall recovery options.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Aircraft Stability Profiles ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #59</span><br>
        <div class="card-title">Supersonic Mach Wave & Shockwave Aero Manuals</div>
        <div class="card-subtitle">Category: Transonic Wave Transitions</div>
        <p style='font-size: 16px;'>Advanced manuals exploring transonic airflow transitions, wave drag, sonic booms, and supersonic flight configurations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Expands curriculum options for advanced students aiming to move beyond basic propeller layouts toward high-speed jet systems.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("NASA High Speed Aerodynamics ↗️", "https://www.nasa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #60</span><br>
        <div class="card-title">Induced vs. Parasite Drag Interception Profiles</div>
        <div class="card-subtitle">Category: Cruise Profile Optimization</div>
        <p style='font-size: 16px;'>Graphical deep-dives mapping how airspeed changes lift-induced drag versus parasite structural drag components.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Shows how fuel efficiency shifts across speed ranges, helping crew members optimize long-range cruise profiles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("CFI Notebook Drag Physics ↗️", "https://www.cfinotebook.net/", use_container_width=True)
    st.write("")

    # --- TIER 7: AIRCRAFT SYSTEMS, PROPULSION & TURBINE THEORY (Ranks #61–70) ---
    st.markdown("#### ⚙️ Tier 7: Aircraft Systems, Propulsion & Turbine Theory (Ranks #61–70)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #61</span><br>
        <div class="card-title">Lycoming Reciprocating Aircraft Engine Overviews</div>
        <div class="card-subtitle">Category: Internal Combustion Modules</div>
        <p style='font-size: 16px;'>Technical training manuals detailing internal combustion systems, oil distributions, and valve sequences in piston aircraft.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students master standard four-stroke engine layouts, facilitating quicker mechanical troubleshooting during pre-flight checks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Lycoming Engine Resource Library ↗️", "https://www.lycoming.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #62</span><br>
        <div class="card-title">Aircraft Carburetor Ice & Fuel Injection Frameworks</div>
        <div class="card-subtitle">Category: Induction Blockage Control</div>
        <p style='font-size: 16px;'>Informative bulletins outlining venturi temperature drops that cause intake icing, along with fuel injection alternatives.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Crucial for power-loss prevention, teaching students to spot and fix induction icing before engine performance drops.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Safety Advisory: Carb Ice Protection ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #63</span><br>
        <div class="card-title">Constant-Speed Propeller Governor Operational Manuals</div>
        <div class="card-subtitle">Category: Hydro-Mechanical Governors</div>
        <p style='font-size: 16px;'>Engineering diagrams explaining how oil pressure shifts propeller pitch angles to maintain stable engine speeds.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Demystifies complex complex-aircraft systems, helping pilots transition smoothly into higher-performance airframes.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("McCauley Propeller Documents ↗️", "https://mccauley.txtav.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #64</span><br>
        <div class="card-title">Dual-Bus Alternator Electrical Grid Schematics</div>
        <div class="card-subtitle">Category: Backup Bus Architecture</div>
        <p style='font-size: 16px;'>Wiring diagrams explaining master switches, primary alternators, essential buses, and emergency battery systems.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Gives pilots the system knowledge needed to manage electrical failures and keep critical instruments running during emergencies.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Cessna 172 POH Reference Archives ↗️", "https://txtav.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #65</span><br>
        <div class="card-title">Hydraulic Landing Gear & Braking System Checklists</div>
        <div class="card-subtitle">Category: High-Pressure Actuators</div>
        <p style='font-size: 16px;'>System layouts showcasing actuators, accumulator systems, fluid paths, and manual emergency backup pumps.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Outlines safety backups for gear extension failures, preparing pilots for manual emergency landing extensions.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Hydraulic Aircraft Systems ↗️", "https://skybrary.aero/articles/hydraulic-systems", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #66</span><br>
        <div class="card-title">Basic Jet Engine Turbine Theory (Axial & Centrifugal)</div>
        <div class="card-subtitle">Category: Compressor Flow Distribution</div>
        <p style='font-size: 16px;'>Multimedia training tracking airflow through compressor stages, combustion chambers, turbine fins, and exhaust nozzles.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Essential foundation for commercial applicants transitioning from light general aviation toward commercial airline turbine systems.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Rolls-Royce Journey Through a Jet Engine ↗️", "https://www.rolls-royce.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #67</span><br>
        <div class="card-title">Pitot-Static Instrument System Plumbing Frameworks</div>
        <div class="card-subtitle">Category: Diaphragm Line Calibration</div>
        <p style='font-size: 16px;'>Overviews tracing air pressure lines connecting pitot tubes and static ports to altimeters, airspeeds, and vertical speed needles.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches pilots how to spot instrument errors caused by blocked air lines, preventing dangerous attitude or speed misreadings.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Flight Instrument Operational Handbooks ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #68</span><br>
        <div class="card-title">Environmental Cabin Pressurization System Layouts</div>
        <div class="card-subtitle">Category: Environmental Bleed Outflows</div>
        <p style='font-size: 16px;'>Engineering outlines explaining outflow valves, bleed-air distributions, and cabin pressure controllers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps pilots prevent altitude decompression incidents, building a solid understanding of high-altitude environmental safety backups.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Cabin Pressurization Systems ↗️", "https://skybrary.aero/articles/cabin-pressurization-system", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #69</span><br>
        <div class="card-title">Fuel System Siphoning & Cross-Feed Valve Protocols</div>
        <div class="card-subtitle">Category: Dynamic Starvation Preventions</div>
        <p style='font-size: 16px;'>Systems drawings covering gravity-fed setups, fuel pump loops, ventilation paths, and cross-feed line management.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Critical for preventing fuel starvation, teaching crews how to safely balance asymmetric fuel weights across wing tanks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Aircraft Systems Manual Directory ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #70</span><br>
        <div class="card-title">Aircraft Anti-Deicing Boot & Heated Leading Edge Outlines</div>
        <div class="card-subtitle">Category: Pneumatic Deicing Boot Frameworks</div>
        <p style='font-size: 16px;'>Overviews comparing pneumatic wing boots, weeping-wing fluid loops, and electrical engine anti-ice systems.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Outlines systemic aircraft options for handling winter weather hazards, helping crews manage clear ice accumulation risks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("NASA In-Flight Icing Branch ↗️", "https://www.nasa.gov/", use_container_width=True)
    st.write("")

    # --- TIER 8: AEROMEDICAL FACTORS & FITNESS PREPARATION (Ranks #71–80) ---
    st.markdown("#### 🏥 Tier 8: Aeromedical Factors & Fitness Preparation (Ranks #71–80)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #71</span><br>
        <div class="card-title">FAA Pilot Safety: Aeromedical Factors Handbook</div>
        <div class="card-subtitle">Category: Physiological Stress Profiles</div>
        <p style='font-size: 16px;'>A text compiling medical concerns like hypoxia, hyperventilation, carbon monoxide poisoning, and motion sickness.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Standard safety reference explaining physical strains on pilots, directly supporting required aeromedical ground training.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Medical Certification Portal ↗️", "https://www.faa.gov/pilots/medical_certification", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #72</span><br>
        <div class="card-title">Spatial Disorientation Night Flight Illusion Manuals</div>
        <div class="card-subtitle">Category: Somatogravic Balance Illusions</div>
        <p style='font-size: 16px;'>Analysis documents breaking down inner-ear balance errors and visual illusions that compromise perception during night flights.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Saves lives by teaching pilots to trust cockpit flight instruments over personal bodily sensations in low-visibility environments.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Spatial Disorientation Resource Page ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #73</span><br>
        <div class="card-title">FAA Third-Class Medical Examination Checklist Standards</div>
        <div class="card-subtitle">Category: Primary Clearance Thresholds</div>
        <p style='font-size: 16px;'>The regulatory handbook defining vision metrics, hearing limits, and cardiovascular thresholds required for pilot medical clearances.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides students with a clear view of health standards early on, preventing unexpected snags during licensing checks.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Guide for Aviation Medical Examiners ↗️", "https://www.faa.gov/ame_guide", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #74</span><br>
        <div class="card-title">Hypoxia Time of Useful Consciousness (TUC) Matrix Tables</div>
        <div class="card-subtitle">Category: Altitude Decompression Horizons</div>
        <p style='font-size: 16px;'>Charts showing how fast a pilot loses clear decision-making capacity across different cruising altitudes following decompression.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Highlights the urgent need for quick emergency mask deployments during rapid high-altitude decompressions.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SKYbrary Hypoxia Assessment ↗️", "https://skybrary.aero/articles/hypoxia", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #75</span><br>
        <div class="card-title">Vestibular Inner-Ear Motion Illusion Simulators</div>
        <div class="card-subtitle">Category: Graveyard Spiral Simulators</div>
        <p style='font-size: 16px;'>Multimedia guides demonstrating how prolonged banking turns can trick the human ear into experiencing deceptive somatogravic sensations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Visually demystifies graveyard spirals, showing how easily physical senses can lead to dangerous flying errors.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Human Factors Training Modules ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #76</span><br>
        <div class="card-title">IM SAFE Personal Pre-Flight Fitness Rubric</div>
        <div class="card-subtitle">Category: Fatigue Risk Assessments</div>
        <p style='font-size: 16px;'>A self-assessment checklist tracking Illness, Medication, Stress, Alcohol, Fatigue, and Emotion before flight operations.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Standardizes personal fitness checks, building a self-monitoring habit to prevent impaired crew operations.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("AOPA Personal Flight Readiness Tool ↗️", "https://www.aopa.org/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #77</span><br>
        <div class="card-title">High-Altitude Vision Accommodation & Scanning Tactics</div>
        <div class="card-subtitle">Category: Night Blind-Spot Identification</div>
        <p style='font-size: 16px;'>Training handbooks showing scanning techniques to find distant traffic and avoid night blind-spot errors.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Enhances collision avoidance by replacing random glances with structured, effective visual sweep patterns.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Visual Scanning Techniques Page ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #78</span><br>
        <div class="card-title">Decompression Sickness & Nitrogen Bubble Prohibitions</div>
        <div class="card-subtitle">Category: Scuba Bubble Prohibitions</div>
        <p style='font-size: 16px;'>Health bulletins detailing how underwater scuba diving changes blood nitrogen levels, posing bends risks during climbs.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Establishes safe wait times between diving and flying, preventing sudden bubble issues in the air.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Divers Alert Network (DAN) Scuba Guidelines ↗️", "https://dan.org/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #79</span><br>
        <div class="card-title">Aviation Noise Induced Hearing Loss & Protection Science</div>
        <div class="card-subtitle">Category: Auditory Decibel Protections</div>
        <p style='font-size: 16px;'>Industrial research evaluating cockpit decibel levels and the long-term protection provided by active noise-canceling headsets.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Encourages early hearing protection habits among students, preventing long-term occupational hearing loss.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("CDC NIOSH Hearing Conservation Hub ↗️", "https://www.cdc.gov/niosh/index.html", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #80</span><br>
        <div class="card-title">OTC Medication Interaction Safety Guidelines</div>
        <div class="card-subtitle">Category: Impairment Hazard Screening</div>
        <p style='font-size: 16px;'>A database specifying which everyday cold or allergy medicines are banned due to hidden drowsy side effects.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Prevents unintended pilot impairment by providing a clear list of flight-safe medication options.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("FAA Do Not Fly/Do Not Issue Medication List ↗️", "https://www.faa.gov/", use_container_width=True)
    st.write("")

    # --- TIER 9: HIGH SCHOOL CADET FUNDING & SCHOLARSHIP MATRICES (Ranks #81–90) ---
    st.markdown("#### 💰 Tier 9: High School Cadet Funding & Scholarship Matrices (Ranks #81–90)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #81</span><br>
        <div class="card-title">AOPA High School Flight Training Scholarship Portal</div>
        <div class="card-subtitle">Category: Primary Certificate Allocation</div>
        <p style='font-size: 16px;'>An annual grant portal offering up to tens of thousands of dollars to high school students chasing primary private pilot certificates.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Directly lowers financial hurdles for young aviators, making it a high-value link for early high school users.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("AOPA Scholarships ↗️", "https://www.aopa.org/training-and-safety/students/scholarships", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #82</span><br>
        <div class="card-title">EAA Ray Aviation Scholarship Foundation Database</div>
        <div class="card-subtitle">Category: Regional Club Sponsorships</div>
        <p style='font-size: 16px;'>A funded grant system run through local experimental aircraft chapters that covers full flight training bills for local youths.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Leverages regional flying clubs to provide mentoring alongside financial assistance, boosting student completion rates.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("EAA Ray Scholarship Board ↗️", "https://www.eaa.org/eaa/youth/ray-aviation-scholarship", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #83</span><br>
        <div class="card-title">Women in Aviation International (WAI) Grant Matrix</div>
        <div class="card-subtitle">Category: Cross-Disciplinary Endowments</div>
        <p style='font-size: 16px;'>A massive annual scholarship fund helping women pursue dispatch, engineering, maintenance, and multi-engine pilot licenses.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Essential for supporting student diversity, offering accessible paths to high-value career funding.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("WAI Scholarship Hub ↗️", "https://www.wai.org/scholarships", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #84</span><br>
        <div class="card-title">Organization of Black Aerospace Professionals (OBAP) Scholarships</div>
        <div class="card-subtitle">Category: Corporate-Backed Career Pipelines</div>
        <p style='font-size: 16px;'>Financial support pipelines designed to help underrepresented minority students cover type-ratings and commercial pilot fees.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps reduce systemic industry entry barriers, providing corporate-backed career pathways into major airlines.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("OBAP Flight Funding ↗️", "https://obap.org/scholarships/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #85</span><br>
        <div class="card-title">National Gay Pilots Association (NGPA) Education Funds</div>
        <div class="card-subtitle">Category: Advanced Rating Grants</div>
        <p style='font-size: 16px;'>An education board offering thousands in flight funding annually to LGBTQ+ community members and supportive allies globally.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Fosters inclusive networking and provides strong financial backing for advanced commercial pilot ratings.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("NGPA Flight Training Grants ↗️", "https://www.ngpa.org/scholarships", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #86</span><br>
        <div class="card-title">Air Force JROTC Flight Academy Portal</div>
        <div class="card-subtitle">Category: Funded Collegiate Summer Residencies</div>
        <p style='font-size: 16px;'>A fully funded summer program allowing selected high school cadets to earn private pilot certificates at partner universities.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Highly prestigious pipeline covering all housing and flight costs, making it a premier opportunity for young cadets.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("AFJROTC Flight Academy ↗️", "https://www.airforce.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #87</span><br>
        <div class="card-title">Captain Barney Conrath Aviation Scholarship Funds</div>
        <div class="card-subtitle">Category: Regional Memorial Endowments</div>
        <p style='font-size: 16px;'>Dedicated flight training memorial funds targeting regional students aiming for professional aviation careers.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Provides valuable alternative funding leads for students who may miss out on broader national scholarship deadlines.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Aviation Scholarship Board ↗️", "https://www.aopa.org/training-and-safety/students/scholarships", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #88</span><br>
        <div class="card-title">The Ninety-Nines International Women Pilots Funding Systems</div>
        <div class="card-subtitle">Category: Female Career Development Pathways</div>
        <p style='font-size: 16px;'>Comprehensive flying awards, including the notable Amelia Earhart Memorial fund, covering advanced flight ratings for female pilots.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Connects female students with historical global support networks, backing long-term career growth.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to The Ninety-Nines Scholarships ↗️", "https://www.ninety-nines.org/scholarships.htm", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #89</span><br>
        <div class="card-title">Regional Airline Association (RAA) Academic Scholarship Boards</div>
        <div class="card-subtitle">Category: Institutional Hour-Building Funding</div>
        <p style='font-size: 16px;'>Higher-education scholarships tailored for collegiate aviators working toward regional airline entry.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Directly connects advanced students to potential employers, helping ease the financial burden of hour-building stages.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to RAA Aviation Awards ↗️", "https://www.raa.org/scholarships/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #90</span><br>
        <div class="card-title">Aircraft Electronics Association (AEA) Technology Grants</div>
        <div class="card-subtitle">Category: Avionics and Engineering Maintenance</div>
        <p style='font-size: 16px;'>Specialized funding focused on avionics repair, electronics engineering, and instrument maintenance training.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Offers a solid alternative track for students interested in tech and maintenance roles over direct cockpit careers.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AEA Educational Foundation ↗️", "https://aea.net/educationalfoundation/", use_container_width=True)
    st.write("")

    # --- TIER 10: VETTED SPECIALIZED VIDEO GROUND SCHOOLS (Ranks #91–100) ---
    st.markdown("#### 📺 Tier 10: Vetted Specialized Video Ground Schools (Ranks #91–100)")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #91</span><br>
        <div class="card-title">Free Pilot Training Online Ground Academy</div>
        <div class="card-subtitle">Category: Open Access Curriculum</div>
        <p style='font-size: 16px;'>Comprehensive, step-by-step video deep-dives going over the entire Private Pilot knowledge blueprint for zero cost.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Offers an excellent free alternative to premium video courses, making ground school accessible to all students.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Free Pilot Training Network ↗️", "https://www.youtube.com/@FreePilotTraining", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #92</span><br>
        <div class="card-title">FlightChops General Aviation Safety Matrices</div>
        <div class="card-subtitle">Category: Human Factors Analysis Vlogs</div>
        <p style='font-size: 16px;'>Highly produced real-world training vlogs exploring cockpit stress, checkride mistakes, instrument training, and safety errors.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Validates the learning curve by showing real pilot struggles, reinforcing realistic safety mindsets.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to FlightChops Safety Ecosystem ↗️", "https://flightchops.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #93</span><br>
        <div class="card-title">The Finer Points: Professional Pilot Flight Training</div>
        <div class="card-subtitle">Category: Practical Flight Deck Mechanics</div>
        <p style='font-size: 16px;'>Educational videos focusing on flight deck organization, refined piloting techniques, stick-and-rudder feel, and safety tips.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students master flight skills faster through sharp, actionable tips from senior flight instructors.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to The Finer Points Flight Resource ↗️", "https://www.learnthefinerpoints.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #94</span><br>
        <div class="card-title">MzeroA Flight Training Free Resource Playlists</div>
        <div class="card-subtitle">Category: Oral Checkride Evaluation Prep</div>
        <p style='font-size: 16px;'>Informative videos covering typical oral exam questions, checkride gotchas, and everyday safety procedures.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Excellent for last-minute oral checkride prep, helping turn complex regulations into clear talking points.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to MzeroA Online Platform ↗️", "https://mzeroa.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #95</span><br>
        <div class="card-title">Fly8MA Free Private Pilot Videos</div>
        <div class="card-subtitle">Category: Pre-Flight Competency Outlines</div>
        <p style='font-size: 16px;'>Short, focused tutorials on critical flight mechanics, crosswind landings, aircraft systems, and chart reading.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Great for quick reviews before flights, letting students easily refresh their memory on key concepts.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Fly8MA Aviation Academy ↗️", "https://fly8ma.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #96</span><br>
        <div class="card-title">Mentour Pilot Commercial Operational Airframe Deep-Dives</div>
        <div class="card-subtitle">Category: Commercial Line Crew Coordination</div>
        <p style='font-size: 16px;'>Detailed breakdowns by a senior airline captain detailing modern jet line problems, multi-crew communication failures, and automated system setups.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Bridges the gap to advanced airline career training by showing students real-world commercial flight safety situations.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Mentour Pilot Enterprise Channel ↗️", "https://mentourpilot.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #97</span><br>
        <div class="card-title">Aviation Training Network Technical Playlists</div>
        <div class="card-subtitle">Category: Mechanical Systems Visualizations</div>
        <p style='font-size: 16px;'>Illustrated animations explaining engine designs, variable-pitch props, and the mechanics of flight instruments.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps visual learners easily understand complex mechanical systems without needing a physical teardown.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Aviation Training Network ↗️", "https://skybrary.aero/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #98</span><br>
        <div class="card-title">AeroGuard Flight Training Academic Blueprints</div>
        <div class="card-subtitle">Category: Baseline Zero-To-Hero Frameworks</div>
        <p style='font-size: 16px;'>Structured learning guides mapping career paths from zero hours up to global airline first officer qualifications.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Helps students outline and budget their entire professional career timeline from day one.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to AeroGuard Flight Academy ↗️", "https://www.flyaeroguard.com/", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #99</span><br>
        <div class="card-title">Corporate Pilot Life: Operational Logistics Series</div>
        <div class="card-subtitle">Category: Part 135 Non-Scheduled Logistics</div>
        <p style='font-size: 16px;'>First-person operational logs detailing business jet flight planning, international handling, and corporate captain duties.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Pulls back the curtain on private charter careers, showing students a viable alternative to typical airline jobs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Corporate Pilot Life Portfolio ↗️", "https://www.youtube.com/@CorporatePilotLife", use_container_width=True)
    st.write("")

    st.markdown("""
    <div class="resource-card">
        <span class="tier-badge-medium">⚓ Rank #100</span><br>
        <div class="card-title">Flight Safety Foundation Accident Prevention Archives</div>
        <div class="card-subtitle">Category: Industry Systemic Incident Matrices</div>
        <p style='font-size: 16px;'>Data-heavy safety reports and case analyses highlighting systemic global airline risks and incident trends.</p>
        <div class="guidance-box">
            <strong>📋 Strategic Value:</strong> Teaches advanced students to appreciate systemic risk metrics and professional safety management architectures.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy to Flight Safety Foundation Resource Center ↗️", "https://flightsafety.org/", use_container_width=True)

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
