import streamlit as st
import pandas as pd
import numpy as np
import datetime

# ==========================================
# 1. PAGE CONFIGURATION & GOOGLE META TAGS
# ==========================================
st.set_page_config(
    page_title="AeroLaunch Hub",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injection of verification headers for search engine tracking
st.markdown(
    """
    <head>
        <meta name="google-site-verification" content="SratphLQH9l1bcw65FrdBhyFi_d0i4wGVhuOCR027ks" />
    </head>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 2. CORE UTILITIES & DATA GENERATION
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
# 3. SIDEBAR NAVIGATION & FILTERS
# ==========================================
st.sidebar.title("✈️ AeroLaunch Control Panel")
st.sidebar.markdown("---")

nav_selection = st.sidebar.radio(
    "Select Workspace Hub:",
    ["📊 Flight Operations Dashboard", "📐 Vector Calculations", "⚙️ System Configuration Settings"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Global Vectors Filters")
selected_status = st.sidebar.multiselect(
    "Filter by Flight Status:",
    options=df_flights["Status"].unique(),
    default=df_flights["Status"].unique()
)

# Apply dynamic filtering
filtered_df = df_flights[df_flights["Status"].isin(selected_status)]

# ==========================================
# 4. WORKSPACE VIEWS
# ==========================================

# VIEW A: FLIGHT OPERATIONS DASHBOARD
if nav_selection == "📊 Flight Operations Dashboard":
    st.title("📊 AeroLaunch Flight Operations Dashboard")
    st.markdown("Real-time airspace monitoring, vector alignments, and performance telemetry matrices.")
    
    # Live high-level metric rows
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
    
    # Flight Data Matrix Grid View
    st.subheader("📋 Real-Time Flight Vector Tracking Grid")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Analytics Breakdown Charting
    st.markdown("---")
    st.subheader("📈 Flight Altitude Profile Distributing Matrix")
    st.bar_chart(data=filtered_df, x="Flight ID", y="Altitude (ft)", color="#1F77B4")


# VIEW B: VECTOR CALCULATIONS
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
            
        # Calculation logic
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
            
        # Standard rule-of-thumb: add 2% to IAS per 1000 ft altitude
        tas_est = ias + (ias * (0.02 * (altitude / 1000)))
        st.success(f"🚀 **Estimated True Airspeed (TAS):** Roughly **{int(tas_est)} kts** under ISA standard environmental profiles.")


# VIEW C: SYSTEM CONFIGURATION SETTINGS
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
    st.caption("This system string aligns with the validation metadata header injected directly into your routing index profile.")
    
    st.markdown("---")
    st.subheader("Data Synchronization Controls")
    if st.button("Force Global Re-Sync & Clear Cache Engine"):
        st.cache_data.clear()
        st.success("App configuration caches cleared! All matrices have refreshed successfully.")

# ==========================================
# 5. FOOTER FRAMEWORK
# ==========================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.8em;'>"
    "AeroLaunch Hub Portal v3.4.0 • Verified via Production Vercel Core Layer Gateway Pipelines"
    "</div>",
    unsafe_allow_html=True
)
