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

    # --- IMAGE ABOVE BIO LAYOUT ---
    st.markdown("### 🧑‍✈️ About the Founder")
    
    # Check directory for image file
    import os
    founder_image = None
    for file in os.listdir("."):
        name_upper = file.upper()
        if ("IMG_" in name_upper) and (file.lower().endswith(".jpg") or file.lower().endswith(".jpeg")):
            founder_image = file
            break
            
    # Render layout: Image is explicitly displayed FIRST (above), then the bio card follows below it
    if founder_image:
        st.image(founder_image, width=300)
    else:
        st.info("💡 Place your founder image file (e.g., IMG_5662.jpg) into your active project directory folder to display it right here above your bio!")

    st.markdown("""
    <div class="resource-card" style="margin-top: 15px;">
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

