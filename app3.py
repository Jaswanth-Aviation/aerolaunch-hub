import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. PAGE CONFIGURATION & METADATA INJECTION
# ==========================================
st.set_page_config(
    page_title="AeroLaunch Hub",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injected verification headers for search engine optimization
st.markdown(
    """
    <head>
        <meta name="google-site-verification" content="SratphLQH9l1bcw65FrdBhyFi_d0i4wGVhuOCR027ks" />
    </head>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 2. DICTIONARY REGISTRY: 200 AVIATION RESOURCES
# ==========================================
PILOT_HUB_DATA = {
    "🥇 Tier 1: Foundational Academics & Checkride Essentials (Ranks #1–10)": [
        {"rank": "#1", "name": "FAA Pilot’s Handbook of Aeronautical Knowledge (PHAK)", "brief": "The foundational textbook covering aerodynamic physics, structural forces, and legal airspace grids.", "link": "https://open.umn.edu/opentextbooks/textbooks/pilot-s-handbook-of-aeronautical-knowledge"},
        {"rank": "#2", "name": "FAA Airplane Flying Handbook (AFH)", "brief": "Step-by-step physical flight mechanics detailing takeoffs, landings, climbs, and stalls.", "link": "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/airplane_flying_handbook"},
        {"rank": "#3", "name": "Pilot Institute Free Private Pilot Ground School Primer", "brief": "Highly interactive visual modules breaking down initial aviation regulations.", "link": "https://pilotinstitute.com/"},
        {"rank": "#4", "name": "Sporty’s Study Buddy Exam Prep Engine", "brief": "Authentic database testing module replicating true Private Pilot written examinations.", "link": "https://www.sportys.com/"},
        {"rank": "#5", "name": "SkyVector Aeronautical Charts", "brief": "Real-time global digital sectional charts used to map visual routing parameters.", "link": "https://skyvector.com/"},
        {"rank": "#6", "name": "EASA Private Pilot Syllabus Framework", "brief": "The core learning blueprint detailing cross-border rules for European flight cadets.", "link": "https://www.easa.europa.eu/"},
        {"rank": "#7", "name": "King Schools Interactive Flight Exam Modules", "brief": "Targeted conceptual video assets covering crosswind limits and aviation math.", "link": "https://kingschools.com/"},
        {"rank": "#8", "name": "Boldmethod Flight Training Quizzes", "brief": "Visual scenario quizzes training quick aeronautical decision-making.", "link": "https://www.boldmethod.com/"},
        {"rank": "#9", "name": "MIT OpenCourseWare: Introduction to Aerospace Engineering", "brief": "Advanced academic breakdowns of lift profiles and aerodynamic load forces.", "link": "https://ocw.mit.edu/"},
        {"rank": "#10", "name": "FAA Airman Certification Standards (ACS)", "brief": "The exact checkride grading sheet outlining acceptable performance parameters.", "link": "https://www.faa.gov/training_testing/testing/acs"}
    ],
    "🎮 Tier 2: Flight Simulation & Cockpit Flow Drills (Ranks #11–20)": [
        {"rank": "#11", "name": "FlightSim.Com Freeware Aircraft Archive", "brief": "Community database hosting virtual avionics modifications and modular airframe dynamics.", "link": "https://www.flightsim.com/"},
        {"rank": "#12", "name": "X-Plane Scenery Gateway", "brief": "Global repository map tracking airport rendering configurations mapped out by simulation engineers.", "link": "https://gateway.x-plane.com/"},
        {"rank": "#13", "name": "FSLTL Live Real-Time Traffic Injection", "brief": "Bridges simulator sessions with true flight radar tracking vectors to populate virtual environments.", "link": "https://fslongtrail.com/"},
        {"rank": "#14", "name": "SmartCopilot Configurations", "brief": "Open-source configuration alternatives enabling shared multicrew cockpit flows in real-time.", "link": "https://skyrun.eu/smartcopilot"},
        {"rank": "#15", "name": "FreeChecklists.net Directory", "brief": "Massive community archive containing standard operating checklist indices across 500 airframes.", "link": "http://www.freechecklists.net/"},
        {"rank": "#16", "name": "SimBrief Enterprise Dispatch Engine", "brief": "Professional flight route planner computing fuel, alternative tracks, and weather profiles.", "link": "https://www.simbrief.com/"},
        {"rank": "#17", "name": "SimToolkitPro Flight Ecosystem", "brief": "Electronic flight bag log tracing navigation charts, speed cards, and landings metrics.", "link": "https://simtoolkitpro.co.uk/"},
        {"rank": "#18", "name": "Little Navmap Open-Source Navigation", "brief": "Open-source flight planning tracker displaying terrain alerts and airspace borders.", "link": "https://albar965.github.io/littlenavmap.html"},
        {"rank": "#19", "name": "VOR Navigation Web App Simulator", "brief": "Interactive instrumentation simulator mapping target radial tracking and CDI alignment.", "link": "http://www.luizmonteiro.com/"},
        {"rank": "#20", "name": "Garmin G1000 Glass Cockpit Interface Guide", "brief": "Official software processing handbooks tracking primary and multi-function flight displays.", "link": "https://www.garmin.com/"}
    ],
    "🌤️ Tier 3: Aviation Meteorology & Weather Tracking (Ranks #21–30)": [
        {"rank": "#21", "name": "NOAA Aviation Weather Center (AWC)", "brief": "Primary meteorology feed tracking active convective layers, turbulence graphs, and icing loops.", "link": "https://aviationweather.gov/"},
        {"rank": "#22", "name": "FAA Aviation Weather Handbook (FAA-H-8083-28)", "brief": "Regulatory framework explaining weather mechanisms from structural ice to fronts.", "link": "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation"},
        {"rank": "#23", "name": "Bad Elf METAR/TAF Decoding Tool", "brief": "Simplifies cryptic meteorological reports into readable wind shear vectors and temperature variables.", "link": "https://bad-elf.com/"},
        {"rank": "#24", "name": "Windy.com Advanced Weather Interface", "brief": "Interactive high-fidelity weather layers scanning isobar contours and altitude winds.", "link": "https://www.windy.com/"},
        {"rank": "#25", "name": "National Weather Service JetStream Online Academy", "brief": "Comprehensive digital curriculum explaining the mechanics behind localized pressure cells.", "link": "https://www.weather.gov/jetstream/"},
        {"rank": "#26", "name": "Skew-T Log-P Atmospheric Diagram Guide", "brief": "Advanced thermodynamic sounding indexes predicting microburst risk and cloud boundary profiles.", "link": "https://www.meted.ucar.edu/"},
        {"rank": "#27", "name": "University of Wyoming Weather Data Archives", "brief": "Direct sounding data portal providing historical tropospheric atmospheric profile details.", "link": "http://weather.uwyo.edu/"},
        {"rank": "#28", "name": "Coordinated Icing & Turbulence Forecast Models", "brief": "Graphical forecasting maps measuring relative humidity grids to flag icing vectors.", "link": "https://aviationweather.gov/forecast/icing"},
        {"rank": "#29", "name": "Climate & Micro-Meteorology Aviation Guides", "brief": "SKYbrary manual tracking global jetstream bands and wind deviations.", "link": "https://skybrary.aero/"},
        {"rank": "#30", "name": "NASA/Ames Aviation Safety Reporting System (ASRS)", "brief": "Confidential submission ledger indexing human factor feedback and weather encounters.", "link": "https://asrs.arc.nasa.gov/"}
    ],
    "🎙️ Tier 4: Radio Telephony & Communication Frameworks (Ranks #31–40)": [
        {"rank": "#31", "name": "LiveATC.net Global Audio Network", "brief": "Live streaming feeds catching true tower transmissions and center separation vectors worldwide.", "link": "https://www.liveatc.net/"},
        {"rank": "#32", "name": "PlaneEnglish: ARSim Free Training Tier", "brief": "Interactive sandbox evaluating standard aviation phraseology patterns.", "link": "https://planeenglishsim.com/"},
        {"rank": "#33", "name": "PilotEdge Public Training Workshops", "brief": "Video guide assets covering real-world communication flows across Class Bravo sectors.", "link": "https://www.pilotedge.net/"},
        {"rank": "#34", "name": "VATSIM Pilot Academy Phrasing Guide", "brief": "Core reference sheet demonstrating standard text and voice communications protocols.", "link": "https://my.vatsim.net/"},
        {"rank": "#35", "name": "FAA AIM Chapter 4: Air Traffic Control Procedures", "brief": "Regulatory framework defining standard traffic patterns and transponder settings.", "link": "https://www.faa.gov/air_traffic/publications/atpubs/aim_html/"},
        {"rank": "#36", "name": "CAA CAP 413 Radiotelephony Manual (UK/Europe)", "brief": "Comprehensive documentation detailing unique ICAO radio codes and wording standards.", "link": "https://www.caa.co.uk/"},
        {"rank": "#37", "name": "SayIntentions.AI Free Trial Module", "brief": "AI voice engine testing pilot transmission clarity within reactive virtual towers.", "link": "https://sayintentions.ai/"},
        {"rank": "#38", "name": "LiveATC Audio Archive Transcription Worksheets", "brief": "Query portal matching timestamped radio voice recordings with textual radar targets.", "link": "https://www.liveatc.net/archive.php"},
        {"rank": "#39", "name": "AOPA Phonetic Alphabet & Numeric Pronunciation Decks", "brief": "Flashcard decks reviewing correct spelling and numbers delivery conventions over radio.", "link": "https://www.aopa.org/"},
        {"rank": "#40", "name": "Lost Communications Procedures Manual", "brief": "Emergency guide outlining routing choices during AVE-F/AME signal loss events.", "link": "https://skybrary.aero/articles/lost-communications"}
    ],
    "📐 Tier 5: Navigation, Flight Planning & Dead Reckoning (Ranks #41–50)": [
        {"rank": "#41", "name": "Open-Source Digital E6B Flight Computer", "brief": "Digital slider tool converting pressure limits, density adjustments, and fuel consumption.", "link": "https://www.onlinee6b.com/"},
        {"rank": "#42", "name": "SkyVector Flight Plan Matrix Developer", "brief": "Waypoint mapping utility generating navigational log paths automatically.", "link": "https://skyvector.com/"},
        {"rank": "#43", "name": "FAA Navigation Handbook (FAA-H-8083-16A)", "brief": "Aviation reference parsing GPS paths, VOR radials, and dead reckoning steps.", "link": "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation"},
        {"rank": "#44", "name": "Great Circle Mapper Navigation Tool", "brief": "Mathematical layout tracking geodesic distance paths across global horizons.", "link": "http://www.gcmap.com/"},
        {"rank": "#45", "name": "Time-Distance-Speed Calculation Sheets", "brief": "Standardized templates organizing ground speed calculations and fuel tracking logs.", "link": "https://www.cfinotebook.net/"},
        {"rank": "#46", "name": "Pilotage Landmark Identification Guides", "brief": "FAA pictorial indices detailing ground reference markers on visual flight rules maps.", "link": "https://www.faa.gov/air_traffic/publications/atpubs/aip/"},
        {"rank": "#47", "name": "IFR Low Altitude Enroute Navigation Manuals", "brief": "Instructional breakdown showing victor routes and minimum enroute altitudes.", "link": "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/"},
        {"rank": "#48", "name": "Magnetic Compass Error Simulation Web Tool", "brief": "Interactive visualizer tracing errors like variation and dip during turns.", "link": "https://www.aerotoolbox.com/"},
        {"rank": "#49", "name": "Airspace Boundary Distance & Safe Vertical Buffers", "brief": "Core reference index tracking horizontal and vertical dimensions of terminal airspace.", "link": "https://www.faa.gov/"},
        {"rank": "#50", "name": "Alternate Airport Selection Rubrics", "brief": "Regulatory reference outlining weather requirements for choosing backup fields under 1-2-3 flight profiles.", "link": "https://www.ecfr.gov/"}
    ],
    "📐 Tier 6: Aerodynamics & Principles of Flight (Ranks #51–60)": [
        {"rank": "#51", "name": "NASA Glenn Research Center: Aerodynamics Portal", "brief": "Explains fluid flow dynamics, lift coefficients, and boundary layers.", "link": "https://www.nasa.gov/glenn"},
        {"rank": "#52", "name": "The Science of Stalls & Angle of Attack (AoA)", "brief": "FAA guide on managing critical angles of attack to prevent spins.", "link": "https://www.faa.gov/news/safety_briefing"},
        {"rank": "#53", "name": "Lift-to-Drag Ratio Calculation Guides", "brief": "Explains the aerodynamics of maximize glide range profiles ($L/D\\text{ Max}$).", "link": "https://skybrary.aero/"},
        {"rank": "#54", "name": "Left-Turning Tendencies Training Systems", "brief": "Explains p-factor, spiraling slipstreams, torque, and gyroscopic precession forces.", "link": "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation"},
        {"rank": "#55", "name": "Boundary Layer Control & Wing Design Textbooks", "brief": "NASA research archives tracking vortex generator setups and laminar boundary profiles.", "link": "https://ntrs.nasa.gov/"},
        {"rank": "#56", "name": "Maneuvering Speed ($V_A$) & Structural Load Limits", "brief": "AOPA analytics tracking structural load limit stresses across varied airframe loads.", "link": "https://www.aopa.org/"},
        {"rank": "#57", "name": "Ground Effect Aerodynamic Matrix Models", "brief": "Explains reduced induced drag profiles experienced close to runway paths.", "link": "https://skybrary.aero/"},
        {"rank": "#58", "name": "Longitudinal, Lateral, and Directional Stability Files", "brief": "Explains the restoration dynamics of stability configurations relative to center of gravity placements.", "link": "https://www.faa.gov/"},
        {"rank": "#59", "name": "Supersonic Mach Wave & Shockwave Aero Manuals", "brief": "Advanced NASA structural guides charting boundary air compression spikes during high-speed flows.", "link": "https://www.nasa.gov/"},
        {"rank": "#60", "name": "Induced vs. Parasite Drag Interception Profiles", "brief": "Explains the intersection point of drag vectors relative to performance curves.", "link": "https://www.cfinotebook.net/"}
    ],
    "⚙️ Tier 7: Aircraft Systems, Propulsion & Turbine Theory (Ranks #61–70)": [
        {"rank": "#61", "name": "Lycoming Reciprocating Aircraft Engine Overviews", "brief": "Schematic files exploring internal component oil routing, pushrods, and ignition profiles.", "link": "https://www.lycoming.com/"},
        {"rank": "#62", "name": "Aircraft Carburetor Ice & Fuel Injection Frameworks", "brief": "FAA safety guide on tracking venturi temperature drops and venturi structural configurations.", "link": "https://www.faa.gov/"},
        {"rank": "#63", "name": "Constant-Speed Propeller Governor Operational Manuals", "brief": "Explains oil pressure alterations used to manage blade pitches via internal flyweights.", "link": "https://mccauley.txtav.com/"},
        {"rank": "#64", "name": "Dual-Bus Alternator Electrical Grid Schematics", "brief": "Cessna POH diagrams detailing voltage regulators, diode protections, and master bus lines.", "link": "https://textronaviation.com/"},
        {"rank": "#65", "name": "Hydraulic Landing Gear & Braking System Checklists", "brief": "Explains closed-loop fluid lines, actuator configurations, and emergency fluid release lines.", "link": "https://skybrary.aero/"},
        {"rank": "#66", "name": "Basic Jet Engine Turbine Theory", "brief": "Explains internal air velocity paths across compressor blades and combustor chambers.", "link": "https://www.rolls-royce.com/"},
        {"rank": "#67", "name": "Pitot-Static Instrument System Plumbing Frameworks", "brief": "Diagrams tracking alternative air sources, static lines, and system drain seals.", "link": "https://www.faa.gov/"},
        {"rank": "#68", "name": "Environmental Cabin Pressurization System Layouts", "brief": "Explains structural configurations managing cabin outflow valves to maintain cabin altitude limits.", "link": "https://skybrary.aero/"},
        {"rank": "#69", "name": "Fuel System Siphoning & Cross-Feed Valve Protocols", "brief": "Explains lateral tank balancing methods and line routing to prevent vapor lock.", "link": "https://www.faa.gov/"},
        {"rank": "#70", "name": "Aircraft Anti-Deicing Boot & Heated Leading Edge Outlines", "brief": "NASA design data highlighting thermal heat lines and pneumatic boot cycles.", "link": "https://www.nasa.gov/"}
    ],
    "🏥 Tier 8: Aeromedical Factors & Fitness Preparation (Ranks #71–80)": [
        {"rank": "#71", "name": "FAA Pilot Safety: Aeromedical Factors Handbook", "brief": "Official manuals tracking atmospheric weight factors, hypoxic thresholds, and flight tolerances.", "link": "https://www.faa.gov/pilots/safety/"},
        {"rank": "#72", "name": "Spatial Disorientation Night Flight Illusion Manuals", "brief": "Aviation guides explaining false horizons and autokinesis risks during low-visibility flights.", "link": "https://www.faa.gov/"},
        {"rank": "#73", "name": "FAA Third-Class Medical Examination Checklist Standards", "brief": "Aviation medical guidelines defining baseline vision parameters and neurologic standards.", "link": "https://www.faa.gov/ame_guide/"},
        {"rank": "#74", "name": "Hypoxia Time of Useful Consciousness (TUC) Matrix Tables", "brief": "Reference index matching pressure altitudes to cognitive capability windows.", "link": "https://skybrary.aero/"},
        {"rank": "#75", "name": "Vestibular Inner-Ear Motion Illusion Simulators", "brief": "Explains fluid movement patterns inside semicircular canals that cause spatial disorientation.", "link": "https://www.faa.gov/"},
        {"rank": "#76", "name": "IM SAFE Personal Pre-Flight Fitness Rubric", "brief": "Diagnostic check template tracking illness, medication, stress, alcohol, fatigue, and emotion status.", "link": "https://www.aopa.org/"},
        {"rank": "#77", "name": "High-Altitude Vision Accommodation & Scanning Tactics", "brief": "Explains visual scanning techniques to combat peripheral blind spots at night.", "link": "https://www.faa.gov/"},
        {"rank": "#78", "name": "Decompression Sickness & Nitrogen Bubble Prohibitions", "brief": "Dive safety reference detailing required surface wait intervals before ascending above altitude limits.", "link": "https://dan.org/"},
        {"rank": "#79", "name": "Aviation Noise Induced Hearing Loss & Protection Science", "brief": "CDC research studying cockpit ambient decibel trends and protective headset seals.", "link": "https://www.cdc.gov/niosh/"},
        {"rank": "#80", "name": "OTC Medication Interaction Safety Guidelines", "brief": "FAA restrictive master ledger listing approved and prohibited over-the-counter medications.", "link": "https://www.faa.gov/"}
    ],
    "💰 Tier 9: High School Cadet Funding & Scholarship Matrices (Ranks #81–90)": [
        {"rank": "#81", "name": "AOPA High School Flight Training Scholarship Portal", "brief": "Annual award platform providing flight funding opportunities to secondary education candidates.", "link": "https://www.aopa.org/training-and-safety/students/scholarships"},
        {"rank": "#82", "name": "EAA Ray Aviation Scholarship Foundation Database", "brief": "Localized scholarship tracker funding full private ground training programs.", "link": "https://www.eaa.org/eaa/youth/ray-aviation-scholarships"},
        {"rank": "#83", "name": "Women in Aviation International (WAI) Grant Matrix", "brief": "WAI registry listing global airframe, turbine rating, and ground training financial support programs.", "link": "https://www.wai.org/scholarships"},
        {"rank": "#84", "name": "Organization of Black Aerospace Professionals (OBAP) Scholarships", "brief": "Direct grant frameworks helping minority candidates secure entry-level flight training.", "link": "https://obap.org/scholarships/"},
        {"rank": "#85", "name": "National Gay Pilots Association (NGPA) Education Funds", "brief": "Financial framework offering flight training grants to advanced ratings applicants.", "link": "https://www.ngpa.org/scholarships"},
        {"rank": "#86", "name": "Air Force JROTC Flight Academy Portal", "brief": "Presents zero-cost summer private license residential flight programs.", "link": "https://www.airforce.com/"},
        {"rank": "#87", "name": "Captain Barney Conrath Aviation Scholarship Funds", "brief": "Dedicated foundation grants focused on assisting student instrument rating candidates.", "link": "https://www.scholarships.com/"},
        {"rank": "#88", "name": "The Ninety-Nines International Women Pilots Funding Systems", "brief": "The Amelia Earhart memorial grant directory offering flight training assistance.", "link": "https://www.ninety-nines.org/scholarships.htm"},
        {"rank": "#89", "name": "Regional Airline Association (RAA) Academic Scholarship Boards", "brief": "Corporate airline scholarship platforms offering funding options to commercial aviation students.", "link": "https://www.raa.org/"},
        {"rank": "#90", "name": "Aircraft Electronics Association (AEA) Technology Grants", "brief": "Financial support tools supporting avionics repair, structural alignment, and system maintenance studies.", "link": "https://aea.net/educationalfoundation/"}
    ],
    "📺 Tier 10: Vetted Specialized Video Ground Schools (Ranks #91–100)": [
        {"rank": "#91", "name": "Free Pilot Training Online Ground Academy", "brief": "Complete YouTube instruction playlists analyzing weather indices and system structures.", "link": "https://www.youtube.com/@FreePilotTraining"},
        {"rank": "#92", "name": "FlightChops General Aviation Safety Matrices", "brief": "Real-world flight scenario videos focusing on risk management and recurrent checkride reviews.", "link": "https://www.youtube.com/@FlightChops"},
        {"rank": "#93", "name": "The Finer Points: Professional Pilot Flight Training", "brief": "Aviation channel analyzing stick-and-rudder mechanics and mountain flight safety.", "link": "https://www.youtube.com/@TheFinerPoints"},
        {"rank": "#94", "name": "MzeroA Flight Training Free Resource Playlists", "brief": "Video resources demonstrating checkride responses and checkride preparation frameworks.", "link": "https://www.youtube.com/@MzeroA"},
        {"rank": "#95", "name": "Fly8MA Free Private Pilot Videos", "brief": "High-yield video modules breaking down weight variations, balance sheets, and traffic rules.", "link": "https://www.youtube.com/@FLY8MA"},
        {"rank": "#96", "name": "Mentour Pilot Commercial Operational Airframe Deep-Dives", "brief": "Commercial captain analyzing heavy-jet incidents, engine flameouts, and cockpit CRM.", "link": "https://www.youtube.com/@MentourPilot"},
        {"rank": "#97", "name": "Aviation Training Network Technical Playlists", "brief": "Video series focusing on IFR chart reading and terminal approach navigation charts.", "link": "https://www.youtube.com/"},
        {"rank": "#98", "name": "AeroGuard Flight Training Academic Blueprints", "brief": "Visual ground tracks detailing aircraft performance optimization tips.", "link": "https://www.aeroguardft.com/"},
        {"rank": "#99", "name": "Corporate Pilot Life: Operational Logistics Series", "brief": "Video logs outlining the real-world demands of corporate operations and business aviation.", "link": "https://www.youtube.com/"},
        {"rank": "#100", "name": "Flight Safety Foundation Accident Prevention Archives", "brief": "Global safety logs analyzing human factor limitations and international flight incident reviews.", "link": "https://flightsafety.org/"}
    ]
}

ATC_HUB_DATA = {
    "🥇 Tier 1: Virtual ATC Frameworks & Master Rules (Ranks #1–10)": [
        {"rank": "#1", "name": "VATSIM S1 Controller Training Syllabus", "brief": "Initial standard operating blueprint managing delivery, clearance, and taxi logic.", "link": "https://vatsim.net/"},
        {"rank": "#2", "name": "FAA Order JO 7110.65 (Air Traffic Control Manual)", "brief": "The legal dictionary containing precise phraseology and vector distance rules.", "link": "https://www.faa.gov/air_traffic/publications/atpubs/atc_html/"},
        {"rank": "#3", "name": "IVAO ATC Online Academy Manuals", "brief": "Specialized instruction manual tracking international ICAO terminal routing setups.", "link": "https://ivao.aero/"},
        {"rank": "#4", "name": "Eurocontrol Training Zone Portal", "brief": "Dynamic network flow exercises covering international sector capacity.", "link": "https://trainingzone.eurocontrol.int/"},
        {"rank": "#5", "name": "VATSIM UK Controller Academy Handbook", "brief": "Pristine guide formatting the core phraseology steps for European sectors.", "link": "https://vatsim.uk/"},
        {"rank": "#6", "name": "ClearAndConcur Ground Control Logic Trainer", "brief": "Open browser puzzles tracking aircraft crossings over busy runway grids.", "link": "https://github.com/"},
        {"rank": "#7", "name": "SkyVector High/Low IFR Enroute Chart Networks", "brief": "High-altitude mapping tracking jet vector intersection points globally.", "link": "https://skyvector.com/"},
        {"rank": "#8", "name": "FAA AIM Chapter 4: Airspace & Tower Layouts", "brief": "Visual layouts demonstrating tower positions and airspace layers.", "link": "https://www.faa.gov/"},
        {"rank": "#9", "name": "EuroScope Radar Client Software Project", "brief": "Professional software package tracking virtual transponder operations.", "link": "https://www.euroscope.hu/"},
        {"rank": "#10", "name": "OpenRadar Open-Source Tower Tracking Software", "brief": "Standalone cross-platform desktop setup tracking terminal radar fields.", "link": "https://sourceforge.net/projects/openradar/"}
    ],
    "🛰️ Tier 2: Radar Vectoring Mechanics & Separation Rules (Ranks #11–20)": [
        {"rank": "#11", "name": "ATC-Sim Browser Radar Vectoring Game", "brief": "Web simulation tool tracking terminal sector radar feeds to manage approach flows.", "link": "http://www.atc-sim.com/"},
        {"rank": "#12", "name": "London Heathrow Tower Operations Guide", "brief": "NATS structural layouts showing sequencing methods at high-intensity fields.", "link": "https://www.nats.aero/"},
        {"rank": "#13", "name": "FAA Runway Incursion Prevention Training Simulator", "brief": "Visual training modules to identify and prevent unauthorized runway access errors.", "link": "https://www.faa.gov/airports/runway_safety/"},
        {"rank": "#14", "name": "ICAO Document 4444 (Air Traffic Management Standards)", "brief": "Global rules for airspace flow coordination and international terminology standards.", "link": "https://store.icao.int/"},
        {"rank": "#15", "name": "Terminal Radar Approach Control (TRACON) Vector Guides", "brief": "Operational strategies for sequencing arrivals into highly congested terminal airspace.", "link": "https://skybrary.aero/"},
        {"rank": "#16", "name": "Standard Lateral and Vertical Separation Minimums Matrix", "brief": "Safety matrices detailing required radar separation distances under instrument conditions.", "link": "https://skybrary.aero/"},
        {"rank": "#17", "name": "Wake Turbulence Category Separation Requirements", "brief": "FAA spacing charts based on weight classes (Super, Heavy, B757, Large, Small).", "link": "https://www.faa.gov/"},
        {"rank": "#18", "name": "Intercept Angle Mathematics for Instrument Approaches", "brief": "FAA guidelines for localizer interception angles under varied wind conditions.", "link": "https://www.faa.gov/"},
        {"rank": "#19", "name": "Speed Adjustment and Clean Sequencing Matrices", "brief": "Methods for adjusting target airspeeds to maintain consistent terminal approach intervals.", "link": "https://skybrary.aero/"},
        {"rank": "#20", "name": "Minimum Vectoring Altitude (MVA) Sector Sectionals", "brief": "FAA safety charts showing minimum safe radar assignment altitudes to prevent terrain collisions.", "link": "https://www.faa.gov/"}
    ],
    "🎙️ Tier 3: ATC Phraseology, Strip Marking & Communications (Ranks #21–30)": [
        {"rank": "#21", "name": "Standard FAA Flight Progress Strip Shorthand Manuals", "brief": "Decodes written clearance symbols, altitude tracking notes, and coordination markings on paper strips.", "link": "https://www.faa.gov/"},
        {"rank": "#22", "name": "Controller-Pilot Readback Error Verification Checklists", "brief": "Safety reference analyzing common miscommunications and target callsign confusion.", "link": "https://skybrary.aero/"},
        {"rank": "#23", "name": "ICAO Standard ATC Phraseology Quick Reference", "brief": "Reference sheet contrasting international terminology with local FAA phraseology conventions.", "link": "https://store.icao.int/"},
        {"rank": "#24", "name": "LiveATC Audio Logs Tower Transcription Exercises", "brief": "Training worksheets to match recorded radio audio with actual radar tracks.", "link": "https://www.liveatc.net/"},
        {"rank": "#25", "name": "Position Relief Briefing Checklists (FAA Form 7230-10)", "brief": "Standard operating procedures ensuring safe traffic hands-offs between controllers.", "link": "https://www.faa.gov/"},
        {"rank": "#26", "name": "Clearances: CRAFT Verification Matrix", "brief": "Clearance delivery tool organizing items: Clearance Limit, Route, Altitude, Frequency, Transponder.", "link": "https://www.cfinotebook.net/"},
        {"rank": "#27", "name": "Ground Control Intersecting Runway Operations Blueprints", "brief": "FAA tool tracking safety buffers for aircraft crossing active runways.", "link": "https://www.faa.gov/"},
        {"rank": "#28", "name": "Conditional Clearance Restrictions and Prohibitions", "brief": "Safety notices warning against non-standard timing instructions like 'behind landing aircraft'.", "link": "https://skybrary.aero/"},
        {"rank": "#29", "name": "Pilot Request Denials & Airspace Saturation Phrasing", "brief": "Standard phrases used to manage high traffic volumes, such as 'unable due to traffic'.", "link": "https://www.faa.gov/"},
        {"rank": "#30", "name": "Visual Flight Rules (VFR) Radar Flight Following Codes", "brief": "AOPA guide to assigning unique squawk codes for advisory services in enroute sectors.", "link": "https://www.aopa.org/"}
    ],
    "🛬 Tier 4: Aerodrome & Tower Operations Architecture (Ranks #31–40)": [
        {"rank": "#31", "name": "FAA Airport Sign and Marking Guide", "brief": "Visual manual explaining runway hold bars, taxiway signs, and critical area markers.", "link": "https://www.faa.gov/"},
        {"rank": "#32", "name": "Runway Configuration Capacity Vector Models", "brief": "Explains how layout choices, prevailing winds, and intersection use affect operations.", "link": "https://skybrary.aero/"},
        {"rank": "#33", "name": "Airport Surface Detection Equipment (ASDE-X) Manuals", "brief": "Technical parameters for radar tracking systems designed to spot ground incursions.", "link": "https://www.faa.gov/"},
        {"rank": "#34", "name": "Airfield Lighting Visual Systems", "brief": "Design guides for precision path indicators, approach light arrays, and flashing identifiers.", "link": "https://www.faa.gov/"},
        {"rank": "#35", "name": "Land and Hold Short Operations (LAHSO) Safety Limits", "brief": "FAA guidelines on aircraft distance minimums and braking performance required for intersection operations.", "link": "https://www.faa.gov/"},
        {"rank": "#36", "name": "Visual Tower Blind Spot Mitigating Procedures", "brief": "Methods for managing areas blocked by hangars or structures using electronic tracking tools.", "link": "https://skybrary.aero/"},
        {"rank": "#37", "name": "Noise Abatement Flight Track Constraints", "brief": "FAA procedures for routing departures away from populated neighborhoods.", "link": "https://www.faa.gov/"},
        {"rank": "#38", "name": "Visual Flight Rules (VFR) Reporting Point Sectionals", "brief": "Charts showing standard reporting markers used to map visual approaches into busy airports.", "link": "https://www.faa.gov/"},
        {"rank": "#39", "name": "Ground Vehicle Movement Transponder Standards", "brief": "Rules for tracking airport maintenance vehicles using active transponders.", "link": "https://www.faa.gov/"},
        {"rank": "#40", "name": "High-Density Gate Pushback Sequencing Schematics", "brief": "ICAO taxiway design systems configured to prevent bottlenecks at busy terminals.", "link": "https://store.icao.int/"}
    ],
    "🗺️ Tier 5: En-Route, Approach & Airspace Stratification (Ranks #41–50)": [
        {"rank": "#41", "name": "Airspace Classifications Dimensional Metric Matrix", "brief": "FAA maps outlining dimensions and pilot entry requirements for Classes Alpha through Echo.", "link": "https://www.faa.gov/"},
        {"rank": "#42", "name": "Standard Terminal Arrival Route (STAR) Chart Profiles", "brief": "Charts mapping arrival tracks, speed restrictions, and vertical profiles.", "link": "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/"},
        {"rank": "#43", "name": "Standard Instrument Departure (SID) Flight Vectors", "brief": "Charts charting departure flight paths to transition aircraft out of busy terminal areas.", "link": "https://www.faa.gov/"},
        {"rank": "#44", "name": "North Atlantic Tracks (NAT) Oceanic Management Systems", "brief": "ICAO routing rules using flexible tracks to optimize transatlantic traffic flows.", "link": "https://www.icao.int/"},
        {"rank": "#45", "name": "Air Route Traffic Control Center (ARTCC) Boundary Maps", "brief": "High-altitude charts mapping geographic boundaries across regional control sectors.", "link": "https://www.faa.gov/"},
        {"rank": "#46", "name": "Pacific Organized Track System (PACOTS) Frameworks", "brief": "Oakland Center oceanic manuals tracking routing structures to optimize fuel burns.", "link": "https://www.faa.gov/"},
        {"rank": "#47", "name": "Holding Pattern Entry Geometric Calculation Worksheets", "brief": "Formulas to determine correct teardrop, parallel, or direct entries based on holding tracks.", "link": "https://www.cfinotebook.net/"},
        {"rank": "#48", "name": "Reduced Vertical Separation Minimum (RVSM) Flight Levels", "brief": "FAA rules reducing vertical separation to 1,000 feet above Flight Level 290.", "link": "https://www.faa.gov/"},
        {"rank": "#49", "name": "Approach Control Radar Hand-off Automation Formats", "brief": "Automated procedures for passing target transponder tags between center and terminal sectors.", "link": "https://www.faa.gov/"},
        {"rank": "#50", "name": "Flight Level Transition Layer Barometric Conversions", "brief": "Procedures for transitioning altimeters to 29.92 when climbing past localized pressure boundaries.", "link": "https://skybrary.aero/"}
    ],
    "🧠 Tier 6: ATSA Aptitude Testing & Selection Prep (Ranks #51–60)": [
        {"rank": "#51", "name": "ATSA Air Traffic Selection Assessment Prep Guide", "brief": "Official application portal outlining testing requirements and timelines for aspiring controllers.", "link": "https://www.faa.gov/be-atc"},
        {"rank": "#52", "name": "ATSA Interactive Radar Collision Avoidance Simulators", "brief": "Testing tools to evaluate quick vector adjustments under high traffic loads.", "link": "https://www.jobtestprep.com/"},
        {"rank": "#53", "name": "Multi-Tasking Memory Math Exercise Grids", "brief": "Cognitive tests checking a candidate's ability to solve math equations while managing visual targets.", "link": "https://humanbenchmark.com/"},
        {"rank": "#54", "name": "Spatial Awareness Relative Direction Tests", "brief": "Psychometric tests evaluating a candidate's speed in tracking relative paths of opposing aircraft.", "link": "https://www.psychometric-success.com/"},
        {"rank": "#55", "name": "ATSA Value Order Target Logical Reasoning Problems", "brief": "Analytical question banks assessing logical ordering speed under strict time pressure.", "link": "https://www.indiana.edu/"},
        {"rank": "#56", "name": "Short-Term Memory Digit Retention Drill Decks", "brief": "Memory exercises measuring accuracy in recalling critical callsigns and heading lists.", "link": "https://humanbenchmark.com/"},
        {"rank": "#57", "name": "Controller Stress Response Reflex Management Profiles", "brief": "Studies on maintaining performance and situational awareness during sudden high-density traffic surges.", "link": "https://www.faa.gov/"},
        {"rank": "#58", "name": "ATSA Personality & Situational Judgement Rubrics", "brief": "FAA evaluation models scoring safe decision-making and rule compliance under pressure.", "link": "https://www.faa.gov/"},
        {"rank": "#59", "name": "Fast-Paced Trajectory Intersect Prediction Modules", "brief": "Math tools measuring speed in predicting path intersections based on speed vectors.", "link": "https://github.com/"},
        {"rank": "#60", "name": "Selective Auditory Attention Distraction Drills", "brief": "Audio tests checking the ability to isolate specific controller voices against background noise.", "link": "https://www.faa.gov/"}
    ],
    "⚠️ Tier 7: Emergency Response Vectors & System Failures (Ranks #61–70)": [
        {"rank": "#61", "name": "ATC Emergency Management Guide (FAA JO 7110.65 Ch.10)", "brief": "Manual defining emergency handling, including fuel alerts, lost communications, and radar failures.", "link": "https://www.faa.gov/"},
        {"rank": "#62", "name": "Transponder Squawk Code Matrix (7500, 7600, 7700)", "brief": "Emergency transponder settings: 7500 for Hijack, 7600 for Radio Failure, 7700 for General Emergency.", "link": "https://www.aopa.org/"},
        {"rank": "#63", "name": "Forced Off-Field Landing Vector Support Protocols", "brief": "Procedures for providing immediate headings and terrain details to aircraft in distress.", "link": "https://skybrary.aero/"},
        {"rank": "#64", "name": "In-Flight Fire Rapid Descents Clearances", "brief": "Priority handling rules to clear lower altitudes quickly during smoke emergencies.", "link": "https://skybrary.aero/"},
        {"rank": "#65", "name": "Complete Radio Failure (NORDO) Intercept Procedures", "brief": "Chart displaying light gun signals used by towers to control aircraft without radios.", "link": "https://www.faa.gov/"},
        {"rank": "#66", "name": "Pilot Disorientation Instrument Failure Radar Support", "brief": "Guidelines for vectoring disoriented pilots out of clouds by avoiding steep turns.", "link": "https://www.faa.gov/"},
        {"rank": "#67", "name": "Fuel Emergency (Minimum Fuel vs. Mayday Fuel) Actions", "brief": "Differentiates between 'minimum fuel' warnings and 'mayday fuel' priority declarations.", "link": "https://skybrary.aero/"},
        {"rank": "#68", "name": "Airport Ground Emergency Equipment Pre-Staging Forms", "brief": "Procedures for coordinating emergency response vehicles along runway entry paths.", "link": "https://www.faa.gov/"},
        {"rank": "#69", "name": "Severe Airframe Icing Escape Vector Allocation", "brief": "Procedures for coordinating rapid altitude changes to help aircraft escape dangerous icing layers.", "link": "https://aviationweather.gov/"},
        {"rank": "#70", "name": "Compass Heading Gyro Failure No-Gyro Vector Rules", "brief": "Methods for guiding pilots with broken directional gyros using timed turn commands.", "link": "https://www.faa.gov/"}
    ],
    "🌤️ Tier 8: Meteorology Coordination for Air Traffic Control (Ranks #71–80)": [
        {"rank": "#71", "name": "Terminal Aerodrome Forecast (TAF) Airport Matrix Interpretation", "brief": "Decodes airport forecast matrices to plan adjustments for upcoming weather changes.", "link": "https://aviationweather.gov/"},
        {"rank": "#72", "name": "SIGMET & AIRMET Active Airspace Boundary Overlays", "brief": "Charts tracking severe hazards, such as severe icing, turbulence, and ash clouds.", "link": "https://aviationweather.gov/"},
        {"rank": "#73", "name": "Microburst & Wind Shear Detection System Alerts (LLWAS)", "brief": "Systems analyzing wind sensors to warn tower controllers of hazardous shear events.", "link": "https://www.faa.gov/"},
        {"rank": "#74", "name": "Convective Weather Avoidance Routing Strategy Manuals", "brief": "Procedures for rerouting traffic around severe thunderstorms to keep arrival gates clear.", "link": "https://skybrary.aero/"},
        {"rank": "#75", "name": "Ground RVR Runway Visual Range Transmissometer Logs", "brief": "Tracks equipment that measures exact runway visibility for low-visibility operations.", "link": "https://www.faa.gov/"},
        {"rank": "#76", "name": "Volcanic Ash Airspace Closure Diversion Routing", "brief": "Coordination maps used to divert traffic around damaging volcanic ash clouds.", "link": "https://www.noaa.gov/"},
        {"rank": "#77", "name": "Winter Operations Runway Friction Coefficient Reports", "brief": "Decodes runway conditions to confirm safe braking performance metrics for landing traffic.", "link": "https://www.faa.gov/"},
        {"rank": "#78", "name": "Density Altitude Tower Capacity Adjustments", "brief": "Explains how hot weather reduces climb rates, requiring wider aircraft spacing.", "link": "https://www.weather.gov/"},
        {"rank": "#79", "name": "Pilot Weather Report (PIREP) Active Solicitation Guidelines", "brief": "Procedures for collecting and sharing weather observations reported directly by pilots.", "link": "https://www.faa.gov/"},
        {"rank": "#80", "name": "Marine Layer Advection Fog Stratus Cleaving Timelines", "brief": "Forecasting guides to anticipate sudden drops in visibility caused by coastal fog.", "link": "https://www.weather.gov/"}
    ],
    "🌐 Tier 9: Cross-Border Logistics & International Routing (Ranks #81–90)": [
        {"rank": "#81", "name": "ICAO Document 9426 (Air Traffic Services Planning Manual)", "brief": "Framework for planning airspace structures and dividing sector responsibilities internationally.", "link": "https://www.icao.int/"},
        {"rank": "#82", "name": "Eurocontrol Central Flow Management Unit Operations", "brief": "Systems managing departure times to prevent traffic overloads across European sectors.", "link": "https://www.eurocontrol.int/"},
        {"rank": "#83", "name": "International Radar Boundary Transition Protocols", "brief": "Procedures for safely handing off transponder data across international borders.", "link": "https://www.faa.gov/"},
        {"rank": "#84", "name": "Altimeter Setting Transition Layers (QNH vs. QNE vs. QFE)", "brief": "Explains international pressure settings used to maintain vertical separation.", "link": "https://skybrary.aero/"},
        {"rank": "#85", "name": "Oceanic Position Reporting Boundary Checkpoints", "brief": "Methods for tracking aircraft over oceans without radar using standard waypoint reports.", "link": "https://skybrary.aero/"},
        {"rank": "#86", "name": "Inter-Center Coordination Automation (ICAD) Systems", "brief": "Systems designed to share flight data smoothly between international control centers.", "link": "https://www.icao.int/"},
        {"rank": "#87", "name": "Flexible Use of Airspace (FUA) Military Transition Zones", "brief": "Procedures for opening military airspace to civilian traffic during low-use periods.", "link": "https://www.eurocontrol.int/"},
        {"rank": "#88", "name": "Pacific Flight Path Multi-Jurisdictional Frameworks", "brief": "ICAO guidelines for coordinating traffic over international waters in the Pacific.", "link": "https://www.icao.int/"},
        {"rank": "#89", "name": "Language Proficiency Standards: ICAO Level 4 Benchmarks", "brief": "Defines international English proficiency standards required for all international operators.", "link": "https://www.icao.int/"},
        {"rank": "#90", "name": "Cross-Border Search and Rescue (SAR) Notification Channels", "brief": "Emergency alert procedures for coordinating international rescue responses.", "link": "https://www.copsas-sarsat.int/"}
    ],
    "📺 Tier 10: System Failure Case Studies & Operational History (Ranks #91–100)": [
        {"rank": "#91", "name": "Tenerife Airport Disaster Systemic Breakdown Analysis", "brief": "Case study on how runway confusion and phraseology errors led to a major runway collision.", "link": "https://skybrary.aero/"},
        {"rank": "#92", "name": "Uberlingen Mid-Air Collision TCAS Priority Study", "brief": "Safety analysis highlighting why pilots should prioritize automated TCAS alerts over conflicting controller instructions.", "link": "https://skybrary.aero/"},
        {"rank": "#93", "name": "1981 PATCO Strike Air Traffic Restructuring History", "brief": "Historical overview of how the 1981 strike changed modern airspace organization.", "link": "https://www.faa.gov/"},
        {"rank": "#94", "name": "Avianca Flight 52 Fuel Management Communication Failure", "brief": "Case study on how non-standard phrases failed to communicate an urgent low-fuel situation.", "link": "https://www.ntsb.gov/"},
        {"rank": "#95", "name": "Milan Linate Runway Incursion Ground Logic Overhaul", "brief": "Analysis of how poor ground markings and thick fog caused a serious runway accident.", "link": "https://skybrary.aero/"},
        {"rank": "#96", "name": "San Diego Mid-Air Collision VFR/IFR Mixing Failure Case", "brief": "Case study that led to stricter radar tracking rules for visual flight rules traffic near busy terminals.", "link": "https://www.ntsb.gov/"},
        {"rank": "#97", "name": "LAX 1991 Runway Intersect Blind Spot System Failure", "brief": "Review of a runway collision caused by local radar blind spots and high controller workload.", "link": "https://www.ntsb.gov/"},
        {"rank": "#98", "name": "Swissair Flight 111 Cockpit Fire Dump Vector Logistics", "brief": "Case study highlighting the balance between dumping fuel and managing an immediate emergency descent.", "link": "https://www.tsb.gc.ca/"},
        {"rank": "#99", "name": "1956 Grand Canyon Mid-Air Collision History", "brief": "Historical review of the collision over the Grand Canyon that led to the creation of the modern FAA.", "link": "https://www.faa.gov/"},
        {"rank": "#100", "name": "Flight Safety Foundation: Continuous ATC Integrity Reports", "brief": "Safety reviews analyzing human factor challenges and system improvements globally.", "link": "https://flightsafety.org/"}
    ]
}

# ==========================================
# 3. CORE UTILITIES & DASHBOARD GENERATION
# ==========================================
@st.cache_data
def load_flight_matrix_data():
    """Generates simulated live aviation data matrices for testing."""
    np.random.seed(42)
    rows = 50
    data = {
        "Flight ID": [f"AL{100 + i}" for i in range(rows)],
        "Aircraft Type": np.random.choice(["Boeing 737-800", "Airbus A320neo", "Boeing 787-9", "Embraer 195"], rows),
        "Departure Vector": np.random.choice(["KJFK", "KLAX", "EGLL", "RJTT", "OMDB"], rows),
        "Arrival Vector": np.random.choice(["ORD", "DFW", "CDG", "SIN", "SYD"], rows),
        "Altitude (ft)": np.random.randint(28000, 41000, size=rows),
        "Airspeed (kts)": np.random.randint(420, 510, size=rows),
        "Status": np.random.choice(["On Schedule", "En Route", "Delayed", "Approaching"], rows, p=[0.4, 0.4, 0.1, 0.1])
    }
    return pd.DataFrame(data)

df_flights = load_flight_matrix_data()

# ==========================================
# 4. SIDEBAR NAVIGATION & FILTERS
# ==========================================
st.sidebar.title("✈️ AeroLaunch Control")
st.sidebar.markdown("---")

nav_selection = st.sidebar.radio(
    "Select Workspace Hub:",
    [
        "📊 Flight Operations Dashboard", 
        "✈️ Section 1: The Pilot Hub", 
        "🎛️ Section 2: The Air Traffic Control Hub",
        "📐 Vector Calculations", 
        "⚙️ System Configuration Settings"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Global Filter Parameters")
selected_status = st.sidebar.multiselect(
    "Filter Dashboard Status:",
    options=df_flights["Status"].unique(),
    default=df_flights["Status"].unique()
)
filtered_df = df_flights[df_flights["Status"].isin(selected_status)]

# ==========================================
# 5. WORKSPACE RENDER LOOP
# ==========================================

# VIEW A: DASHBOARD METRICS
if nav_selection == "📊 Flight Operations Dashboard":
    st.title("📊 AeroLaunch Flight Operations Dashboard")
    st.markdown("Real-time airspace monitoring, vector alignments, and performance telemetry matrices.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Active System Vectors", value=len(filtered_df))
    with col2:
        delayed_count = len(filtered_df[filtered_df["Status"] == "Delayed"])
        st.metric(label="Reported Delays", value=delayed_count, delta="-2 since last sync" if delayed_count > 0 else "0", delta_color="inverse")
    with col3:
        st.metric(label="Mean Airspeed Fleetwide", value=f"{int(filtered_df['Airspeed (kts)'].mean())} kts")
    with col4:
        st.metric(label="Optimal Route Index", value="98.4%")

    st.markdown("---")
    st.subheader("📋 Real-Time Flight Vector Tracking Grid")
    st.dataframe(filtered_df, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📈 Flight Altitude Profile Distributing Matrix")
    st.bar_chart(data=filtered_df, x="Flight ID", y="Altitude (ft)", color="#1F77B4")


# VIEW B: THE PILOT HUB INDEX (1-100)
elif nav_selection == "✈️ Section 1: The Pilot Hub":
    st.title("✈️ Section 1: The Pilot Hub (Ranked #1 to #100)")
    st.markdown("The primary curriculum directory mapped out into ten critical operational flight layers.")
    st.markdown("---")
    
    # Render tiers out dynamically inside expander modules
    for tier_title, resources in PILOT_HUB_DATA.items():
        with st.expander(tier_title, expanded=False):
            for res in resources:
                st.markdown(f"**{res['rank']}: {res['name']}**")
                st.markdown(f"*{res['brief']}*")
                st.markdown(f"[🔗 Open Resource Destination Link]({res['link']})")
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)


# VIEW C: THE ATC HUB INDEX (1-100)
elif nav_selection == "🎛️ Section 2: The Air Traffic Control Hub":
    st.title("🎛️ Section 2: The Air Traffic Control Hub (Ranked #1 to #100)")
    st.markdown("The primary air traffic services directory cataloging operational manuals and tactical simulators.")
    st.markdown("---")
    
    # Render tiers out dynamically inside expander modules
    for tier_title, resources in ATC_HUB_DATA.items():
        with st.expander(tier_title, expanded=False):
            for res in resources:
                st.markdown(f"**{res['rank']}: {res['name']}**")
                st.markdown(f"*{res['brief']}*")
                st.markdown(f"[🔗 Open Resource Destination Link]({res['link']})")
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)


# VIEW D: VECTOR SOLVERS
elif nav_selection == "📐 Vector Calculations":
    st.title("📐 Aviation Vector Calculations Hub")
    st.markdown("Compute airspeed conversions, geometric crosswind vectors, and glide slopes.")
    
    calc_type = st.selectbox("Choose Calculation Matrix Type:", ["Crosswind Component Solver", "True Airspeed (TAS) Calculator"])
    st.markdown("---")
    
    if calc_type == "Crosswind Component Solver":
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            runway_hdg = st.number_input("Runway Heading (Degrees):", min_value=0, max_value=360, value=90)
            wind_direction = st.number_input("Wind Direction Source (Degrees):", min_value=0, max_value=360, value=120)
        with c_col2:
            wind_speed = st.number_input("Reported Wind Velocity (Knots):", min_value=0, value=20)
            
        angle_rad = np.radians(abs(runway_hdg - wind_direction))
        crosswind = np.sin(angle_rad) * wind_speed
        headwind = np.cos(angle_rad) * wind_speed
        
        st.info(f"📐 **Resulting Matrix Output:** Crosswind Component is **{crosswind:.1f} kts** | Headwind Component is **{headwind:.1f} kts**")

    elif calc_type == "True Airspeed (TAS) Calculator":
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            ias = st.number_input("Indicated Airspeed (IAS) in Knots:", min_value=0, value=250)
        with t_col2:
            altitude = st.number_input("Current Flight Pressure Altitude (Feet):", min_value=0, value=10000)
            
        tas_est = ias + (ias * (0.02 * (altitude / 1000)))
        st.success(f"🚀 **Estimated True Airspeed (TAS):** Roughly **{int(tas_est)} kts** under ISA standard environmental profiles.")


# VIEW E: SYSTEM SETTINGS
elif nav_selection == "⚙️ System Configuration Settings":
    st.title("⚙️ System Configuration Settings")
    st.markdown("Manage application structural setups, parameters, and metadata validations.")
    st.markdown("---")
    
    st.subheader("System Information Metadata Verification")
    st.text_input(
        label="Google Verification Reference Key Identifier:", 
        value="SratphLQH9l1bcw65FrdBhyFi_d0i4wGVhuOCR027ks", 
        disabled=True
    )
    
    st.markdown("---")
    st.subheader("Data Synchronization Controls")
    if st.button("Force Global Re-Sync & Clear Cache Engine"):
        st.cache_data.clear()
        st.success("App configuration caches cleared! All matrices have refreshed successfully.")

# ==========================================
# 6. FOOTER FRAMEWORK
# ==========================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.8em;'>"
    "AeroLaunch Hub Portal v4.0.0 • Verified via Production Vercel Core Layer Gateway Pipelines"
    "</div>",
    unsafe_allow_html=True
)
