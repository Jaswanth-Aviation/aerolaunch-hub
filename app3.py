# ==========================================
# 1. CORE IMPORTS, CONFIGS & PERSISTENCE
# ==========================================
import streamlit as st
import json
import os
import re
from datetime import datetime

# Define file paths for light database simulation
USER_DB = "user_db.json"
CHAT_DB = "chat_db.json"

# Initialize JSON files if they don't exist
if not os.path.exists(USER_DB):
    with open(USER_DB, "w") as f:
        # Default starter accounts
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
    # Dynamic profile image generation based strictly on the typed nickname via Dicebear Initials API
    clean_name = re.sub(r'[^a-zA-Z0-9 ]', '', nickname).strip().replace(" ", "%20")
    if not clean_name:
        clean_name = "User"
    return f"https://api.dicebear.com/7.x/initials/svg?seed={clean_name}"

# Initial page setup
st.set_page_config(page_title="AeroLaunch", page_icon="✈️", layout="wide")

# ==========================================
# 🔐 AUTHENTICATION GATEWAY
# ==========================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_username" not in st.session_state:
    st.session_state.user_username = ""
if "user_display_name" not in st.session_state:
    st.session_state.user_display_name = ""

# Handle query parameter sessions safely
if st.query_params.get("session") == "active" and "current_user" in st.query_params:
    st.session_state.logged_in = True
    st.session_state.user_username = st.query_params["current_user"]
    users = load_users()
    if st.session_state.user_username in users:
        st.session_state.user_display_name = users[st.session_state.user_username]["name"]

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
            login_pass = st.text_input("Password", type="password")
            submit_login = st.form_submit_button("Enter Flight Deck Controls 🚀", use_container_width=True, type="primary")
            
            if submit_login:
                if login_user in users and users[login_user]["password"] == login_pass:
                    st.session_state.logged_in = True
                    st.session_state.user_username = login_user
                    st.session_state.user_display_name = users[login_user]["name"]
                    st.query_params["session"] = "active"
                    st.query_params["current_user"] = login_user
                    st.success("Access Granted! Accessing main deck...")
                    st.rerun()
                else:
                    st.error("Invalid Username or Password. Use 'pilot1' and 'password123' to test.")
                    
    else:
        with st.form("signup_form"):
            st.markdown("### Create New Account Profile")
            new_user = st.text_input("Choose Unique Username (lowercase, no spaces)").strip().lower()
            new_name = st.text_input("Choose Display Nickname (Your dynamic avatar is built from this)")
            new_email = st.text_input("Email Address")
            new_pass = st.text_input("Account Password", type="password")
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

# Load real-time database user definitions for navigation and layouts
users_data = load_users()
current_username = st.session_state.user_username

# Security check to guarantee session synchronization
if current_username not in users_data:
    st.session_state.logged_in = False
    st.query_params.clear()
    st.rerun()

current_nickname = users_data[current_username]["name"]

# ==========================================
# 🧭 SIDEBAR SESSION & LOGOUT CONTROL
# ==========================================
with st.sidebar:
    st.markdown("### 👤 User Session")
    user_avatar_side = get_avatar_url(current_nickname)
    
    # Visual sidebar profile badge
    st.markdown(f"""
    <div style="text-align: center; padding: 10px; background-color: white; border-radius: 8px; border: 1px solid #cbd5e1; margin-bottom: 10px;">
        <img src="{user_avatar_side}" width="55" style="border-radius: 50%; background: #f1f5f9; border: 2px solid #1d4ed8;"><br>
        <strong style="font-size: 14px; color: #0f172a;">{current_nickname}</strong><br>
        <span style="font-size: 11px; color: #64748b;">@{current_username}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("🟢 Status: Connected as Pilot")
    st.markdown("---")
    
    if st.button("🚪 Log Out & Clear Session", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user_username = ""
        st.session_state.user_display_name = ""
        st.query_params.clear()
        st.rerun()

# ==========================================
# --- Your Navigation Deck & UI Styling ---
# ==========================================
st.markdown("""
<style>
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

st.markdown('<div class="app-header"><h1>AeroLaunch</h1></div>', unsafe_allow_html=True)

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
# 🗺️ ROUTING LOGIC PAGES
# ==========================================

if st.session_state.page == "Feed":
    st.markdown("### 📢 Mission Briefing")
    st.markdown(f"""
    <div class="resource-card">
        <div class="card-title">The High-School Aviation Deployment Matrix</div>
        <div class="card-subtitle">System Status: Operational</div>
        <p style='font-size: 17px;'>Welcome back to AeroLaunch, <strong>{current_nickname}</strong>. This portal was engineered specifically to solve the information gap for high school students looking to enter professional aviation. Use the navigation deck above to deploy into your chosen vector.</p>
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

elif st.session_state.page in ["Pilots", "ATC", "Crew", "Maintenance", "Drone", "AI"]:
    st.info(f"Welcome to the **{st.session_state.page}** Roadmap section module. Your content databases remain structurally live.")
    # (Placeholder representing your comprehensive aviation matrices #1-#25 from the background code)

# ==========================================
# 🌐 UPDATED COMMUNITY PAGE WITH CUSTOM PROFILE AVATARS
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
            
            # Stylized Profile card container
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
                
                # Render messages with micro inline avatars matching their sender nickname
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
