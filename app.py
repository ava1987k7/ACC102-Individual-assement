import streamlit as st
import pandas as pd
import joblib
import time
import os

# ==========================================
# 0. Page Basic Settings, Immersive Background & Effects
# ==========================================
# Use wide layout for a more impactful gym background
st.set_page_config(page_title="Fat-Burning Superpower Assessment", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    /* Inject immersive gym background image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=2000&auto=format&fit=crop");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    
    /* Make the content area a translucent frosted glass texture to ensure text is readable */
    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 3rem !important;
        margin-top: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
    }

    /* Animations and font size upgrades */
    .fade-in { animation: fadeIn 0.8s ease-in; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    
    .pop-in { animation: popIn 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    @keyframes popIn { 0% { transform: scale(0); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
    
    /* Jumbo Title */
    .breathing-title { 
        text-align: center; 
        color: #FF2A2A; 
        font-size: 70px !important; 
        font-weight: 900; 
        text-transform: uppercase;
        letter-spacing: 2px;
        animation: breathe 2s infinite alternate; 
    }
    @keyframes breathe { from { transform: scale(1); text-shadow: 0 0 10px #ffcccb; } to { transform: scale(1.03); text-shadow: 0 0 25px #ff2a2a; } }
    
    .npc-avatar { font-size: 70px; margin-right: 15px; line-height: 1; filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.2)); }
    .chat-bubble {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); 
        padding: 20px; border-radius: 20px; box-shadow: 0 8px 16px rgba(255,75,75,0.15);
        border: 2px solid #FF4B4B; position: relative; width: 100%;
        font-size: 18px; color: #333; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 1. State Machine
# ==========================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'prediction' not in st.session_state:
    st.session_state.prediction = 'Moderate'

def go_to_page(page_name):
    st.session_state.page = page_name

# ==========================================
# Page A: 🏠 Jumbo Cool Home Page with Dynamic Effects
# ==========================================
if st.session_state.page == 'home':
    # Inject custom JS/CSS for typewriter effect, live simulator, and 3D hover
    st.markdown("""
    <style>
        /* 3D tilt effect for cards */
        .tilt-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 15px;
            overflow: hidden;
        }
        .tilt-card:hover {
            transform: rotateX(2deg) rotateY(2deg) translateY(-5px);
            box-shadow: 0 20px 30px rgba(0,0,0,0.2);
        }
        /* Live feed container */
        .live-feed {
            background: rgba(0,0,0,0.7);
            backdrop-filter: blur(10px);
            border-radius: 40px;
            padding: 10px 20px;
            display: inline-block;
            font-family: monospace;
            font-size: 18px;
            color: #00ffcc;
            margin-bottom: 20px;
            border: 1px solid #00ffcc;
            box-shadow: 0 0 15px rgba(0,255,204,0.3);
        }
        @keyframes pulse-glow {
            0% { text-shadow: 0 0 2px #ff2a2a; }
            100% { text-shadow: 0 0 15px #ff2a2a; }
        }
        .breathing-title {
            animation: breathe 2s infinite alternate, pulse-glow 1.5s infinite;
        }
    </style>
    
    <script>
        // Simulate real-time heart rate / step data (frontend only)
        function updateLiveFeed() {
            let hr = Math.floor(60 + Math.random() * 30);
            let steps = Math.floor(3000 + Math.random() * 5000);
            document.getElementById('live-hr').innerText = hr;
            document.getElementById('live-steps').innerText = steps;
        }
        setInterval(updateLiveFeed, 2000);
        window.onload = updateLiveFeed;
    </script>
    
    <div id="live-feed-wrapper" style="text-align: center; margin-top: -20px;">
        <div class="live-feed">
            🔴 LIVE BIOMETRIC FEED &nbsp;|&nbsp;
            ❤️ <span id="live-hr">72</span> bpm &nbsp;|&nbsp;
            🚶 <span id="live-steps">4230</span> steps today
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Typewriter subtitle (using st.markdown + simple CSS animation)
    st.markdown("""
    <div style="text-align: center; font-size: 20px; font-weight: bold; color: #FF4B4B; margin-bottom: 30px;">
        <span id="typed-text"></span>
    </div>
    <script>
        const phrases = [
            "Your metabolism is unique. ⚡",
            "Stop guessing calories. 🧠",
            "AI knows your fat-burning zone. 🔥",
            "Based on 1000+ real fitness data. 📊"
        ];
        let i = 0;
        let j = 0;
        let currentPhrase = [];
        let isDeleting = false;
        function typeEffect() {
            let fullText = phrases[i];
            if (isDeleting) {
                currentPhrase.pop();
            } else {
                currentPhrase.push(fullText[j]);
                j++;
            }
            document.getElementById("typed-text").innerHTML = currentPhrase.join("");
            if (!isDeleting && j === fullText.length) {
                isDeleting = true;
                setTimeout(typeEffect, 2000);
                return;
            }
            if (isDeleting && currentPhrase.length === 0) {
                isDeleting = false;
                j = 0;
                i = (i + 1) % phrases.length;
            }
            let speed = isDeleting ? 50 : 100;
            setTimeout(typeEffect, speed);
        }
        typeEffect();
    </script>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        
        # Top Title
        st.markdown('<p class="breathing-title">⚡ Metabolic Power Assessment ⚡</p>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 22px; color: #444; font-weight: bold;'>AI Engine built on 1000+ real-world fitness data points</p><br><br>", unsafe_allow_html=True)
        
        # Three-column layout with tilt effect
        col1, col2, col3 = st.columns([1, 1.5, 1])
        
        with col1:
            st.markdown('<div class="tilt-card"><img src="https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=500&auto=format&fit=crop" style="width:100%; border-radius:15px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);"></div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="pop-in" style="text-align:center; font-size:140px; margin-top: -20px;">🔥</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("👉 Start Hardcore Assessment 👈", use_container_width=True, key="start_quiz_btn"):
                go_to_page('quiz')
                st.rerun()
                
        with col3:
            st.markdown('<div class="tilt-card"><img src="https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?q=80&w=500&auto=format&fit=crop" style="width:100%; border-radius:15px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);"></div>', unsafe_allow_html=True)

        # Social proof marquee
        st.markdown("""
        <div style="margin-top: 40px; text-align: center; font-size: 14px; color: #888; border-top: 1px solid #ddd; padding-top: 20px;">
            🔥 2,384 people assessed today · ⚡ 89% improved after 4 weeks · 🏆 Join the metabolic revolution
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
# ==========================================
# Page B: 💬 In-Depth Data Collection Page (Hardcore Pro Version)
# ==========================================
elif st.session_state.page == 'quiz':
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display: flex; align-items: flex-start; margin-bottom: 30px;">
        <div class="npc-avatar">👩‍🔬</div>
        <div class="chat-bubble">
            No need to guess calories blindly, and don't rely on feelings for heart rate!<br>
            Take out your smartwatch, complete the <b>3-Step Data Calibration</b> below, and the AI engine will calculate everything for you. 👇
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Completely discard tabs, use strong guided vertical layout (waterfall) ---
    
    # 🔴 Step 1
    st.markdown('<h3 style="color:#FF4B4B; border-bottom: 2px solid #FF4B4B; padding-bottom: 5px;">📊 STEP 1: Basic Metrics</h3>', unsafe_allow_html=True)
    st.info("The backend will accurately calculate your BMR (Basal Metabolic Rate) using the Mifflin-St Jeor equation.")
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        gender = st.radio("🚻 Gender", ["Male", "Female"], horizontal=True)
        age = st.number_input("🎂 Age", 10, 100, 25)
        height = st.number_input("📏 Height (cm)", 100.0, 250.0, 175.0, step=1.0)
        weight = st.number_input("⚖️ Weight (kg)", 30.0, 200.0, 65.0, step=1.0)
    with col1_2:
        body_fat_desc = st.selectbox("🥓 Which range roughly describes your current body fat?", 
                                    ["Visible clear abs/V-line (approx. 10-15%)", 
                                     "Flat and firm, no obvious fat (approx. 16-20%)", 
                                     "Slightly small belly (approx. 21-25%)", 
                                     "Obvious waist and belly fat, somewhat plump (approx. 26-30%)",
                                     "Overall round (30% and above)"], index=1)
        muscle_shape = st.selectbox("💪 Muscle definition visual assessment", 
                                    ["Weak, relatively soft body", "Normal and proportionate", "Signs of training, firm lines", "Professional bodybuilding level, very thick"],
                                    index=1)
                                    
    st.markdown("<br>", unsafe_allow_html=True)

    # 🔴 Step 2
    st.markdown('<h3 style="color:#FF8C00; border-bottom: 2px solid #FF8C00; padding-bottom: 5px;">🏃 STEP 2: Workout Load</h3>', unsafe_allow_html=True)
    st.info("Where did the calories go? (The AI will automatically convert total calories burned based on these two core metrics)")
    col2_1, col2_2 = st.columns(2)
    with col2_1:
        steps = st.number_input("👣 Daily average steps (Check your phone)", 0, 50000, 8000, step=500)
        active_mins = st.slider("⏱️ Truly intense workout duration per day (minutes)", 0, 300, 45)
    with col2_2:
        workouts = st.slider("🏋️ Formal workout sessions per week", 0, 14, 3)
        continuous_days = st.slider("📅 How many consecutive days have you worked out so far?", 0, 365, 2)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # 🔴 Step 3
    st.markdown('<h3 style="color:#28A745; border-bottom: 2px solid #28A745; padding-bottom: 5px;">🫀 STEP 3: Core Function</h3>', unsafe_allow_html=True)
    st.info("Cardiopulmonary & recovery capacity (Please refer to your smart wearable devices)")
    col3_1, col3_2 = st.columns(2)
    with col3_1:
        hr_resting = st.number_input("🫀 Resting Heart Rate bpm (Use smartwatch data, do not guess!)", 40, 120, 65)
        hr_avg = st.number_input("💓 Avg Workout Heart Rate bpm (Use smartwatch data, do not guess!)", 80, 200, 120)
    with col3_2:
        sleep = st.slider("💤 Average daily sleep (hours)", 3.0, 12.0, 7.5, step=0.5)
        water_cups = st.slider("💧 Roughly how many cups of water per day? (Based on 500ml large cup)", 1, 10, 4)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # 🔴 Submit button area
    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        # Modify button style, larger and more eye-catching
        st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #FF2A2A; color: white; height: 3.5em; font-size: 22px; font-weight: bold; border-radius: 12px;
            box-shadow: 0 5px 15px rgba(255, 42, 42, 0.4); transition: all 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            transform: translateY(-2px); box-shadow: 0 8px 20px rgba(255, 42, 42, 0.6);
        }
        </style>""", unsafe_allow_html=True)
        
        if st.button("✨ Data Locked, Start AI Engine! ✨", use_container_width=True):
            if not os.path.exists("rf_model.pkl"):
                st.error("🚨 Cannot find your core model file rf_model.pkl! Make sure it's in the same folder as the code.")
            else:
                try:
                    model = joblib.load("rf_model.pkl")
                    
                    # 1. Basic logic operations (unchanged)
                    calc_bmi = weight / ((height / 100) ** 2)
                    calc_hydration = water_cups * 0.5 
                    bf_dict = {"Visible clear abs/V-line (approx. 10-15%)": 12.5, "Flat and firm, no obvious fat (approx. 16-20%)": 18.0, "Slightly small belly (approx. 21-25%)": 23.0, "Obvious waist and belly fat, somewhat plump (approx. 26-30%)": 28.0, "Overall round (30% and above)": 35.0}
                    calc_body_fat = bf_dict[body_fat_desc]
                    muscle_dict = {"Weak, relatively soft body": 0.25, "Normal and proportionate": 0.40, "Signs of training, firm lines": 0.55, "Professional bodybuilding level, very thick": 0.75}
                    calc_muscle = muscle_dict[muscle_shape]
                    
                    if gender == "Male":
                        bmr = 10 * weight + 6.25 * height - 5 * age + 5
                    else:
                        bmr = 10 * weight + 6.25 * height - 5 * age - 161
                    
                    calc_calories = bmr * 1.2 + (active_mins * 8) + (steps * 0.04)
                    calc_intensity = active_mins / (steps + 1)
                    calc_fitness = calc_muscle / (calc_body_fat + 1e-5)
                    calc_recovery = sleep * calc_hydration
                    calc_cardio = hr_resting / (hr_avg + 1)
                    
                    # 2. Package raw data dictionary
                    raw_data = {
                        'age': age,
                        'steps_per_day': steps,
                        'active_minutes': active_mins,
                        'calories_burned': calc_calories,     
                        'sleep_hours': sleep,
                        'hydration_liters': calc_hydration,   
                        'bmi': calc_bmi,                      
                        'workouts_per_week': workouts,
                        'muscle_mass_ratio': calc_muscle,     
                        'body_fat_percentage': calc_body_fat, 
                        'heart_rate_resting': hr_resting,
                        'heart_rate_avg': hr_avg,
                        'continuous_exercise_days': continuous_days,
                        'activity_intensity': calc_intensity,
                        'fitness_ratio': calc_fitness,
                        'recovery_score': calc_recovery,
                        'cardio_efficiency': calc_cardio
                    }
                    
                    input_df = pd.DataFrame([raw_data])
                    
                    # 3. Core fix: industrial-grade feature alignment
                    # Automatically read the feature order and spelling of the backend model, strictly align. If any feature is missing, automatically fill with 0 to prevent crashes.
                    expected_features = model.feature_names_in_
                    aligned_df = input_df.reindex(columns=expected_features, fill_value=0)
                    
                    # Store data for Page C
                    st.session_state.raw_matrix = aligned_df
                    
                    # 4. Perform prediction
                    st.session_state.prediction = model.predict(aligned_df)[0]
                    st.session_state.page = 'result'
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Engine Architecture Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)
    
# =====================================================================
# PAGE C: 🧬 METABOLIC SPECTRUM & BIOMETRIC PAYLOAD (Data-Driven Engine)
# =====================================================================
elif st.session_state.page == 'result':
    
    # -----------------------------------------------------------------
    # [CORE ARCHITECTURE] DOM Minification & Injection Engine
    # -----------------------------------------------------------------
    class UI_Architect:
        @staticmethod
        def render(payload: str):
            import re
            compressed = re.sub(r'\s+', ' ', payload.replace('\n', ' ')).strip()
            st.markdown(compressed, unsafe_allow_html=True)

    class MetabolicSpectrumRenderer:
        @staticmethod
        def build_spectrum(percentile: int, rank_text: str, theme_color: str):
            spectrum_css = f"""
            <style>
                .spectrum-wrapper {{ margin: 30px 0; padding: 30px; background: #fff; border-radius: 16px; border: 1px solid #eaeaea; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
                .spectrum-header {{ display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 35px; }}
                .spectrum-title {{ font-size: 15px; font-weight: 800; color: #888; text-transform: uppercase; letter-spacing: 1px; margin: 0; }}
                .spectrum-highlight {{ font-size: 32px; font-weight: 900; color: {theme_color}; margin: 0; line-height: 1; }}
                .spectrum-track {{ position: relative; height: 24px; background: linear-gradient(to right, #E63946 0%, #E63946 55.5%, #F4A261 55.5%, #F4A261 77.7%, #2A9D8F 77.7%, #2A9D8F 100%); border-radius: 12px; box-shadow: inset 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 10px; }}
                .spectrum-zone-label {{ position: absolute; top: -25px; font-size: 11px; font-weight: bold; text-transform: uppercase; }}
                .zone-l3 {{ left: 15%; color: #E63946; }}
                .zone-l2 {{ left: 58%; color: #F4A261; }}
                .zone-l1 {{ left: 82%; color: #2A9D8F; }}
                .spectrum-marker {{ position: absolute; top: -12px; left: {percentile}%; width: 4px; height: 48px; background: #111; border-radius: 2px; transform: translateX(-50%); box-shadow: 0 0 10px rgba(0,0,0,0.3); z-index: 10; }}
                .spectrum-tooltip {{ position: absolute; top: 48px; left: {percentile}%; transform: translateX(-50%); background: #111; color: #fff; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: bold; white-space: nowrap; z-index: 10; animation: pulse-tip 2s infinite; }}
                .spectrum-tooltip::before {{ content: ''; position: absolute; top: -5px; left: 50%; transform: translateX(-50%); border-width: 0 6px 6px 6px; border-style: solid; border-color: transparent transparent #111 transparent; }}
                @keyframes pulse-tip {{ 0% {{ transform: translateX(-50%) scale(0.95); }} 50% {{ transform: translateX(-50%) scale(1.05); }} 100% {{ transform: translateX(-50%) scale(0.95); }} }}
                .tier-card {{ padding: 25px; border-radius: 12px; border: 2px solid #eee; background: #fff; opacity: 0.4; transition: all 0.3s; text-align: center; height: 100%; filter: grayscale(100%); }}
                .tier-card.active {{ opacity: 1; transform: scale(1.05); box-shadow: 0 15px 35px rgba(0,0,0,0.1); border-width: 4px; filter: grayscale(0%); }}
                .tier-icon {{ font-size: 45px; margin-bottom: 10px; }}
                .tier-title {{ font-size: 20px; font-weight: 900; margin: 0; text-transform: uppercase; }}
                .tier-desc {{ font-size: 13px; color: #666; margin-top: 10px; line-height: 1.5; }}
                .upgrade-hint {{ font-size: 11px; color: #888; margin-top: 12px; padding-top: 8px; border-top: 1px dashed #ddd; }}
            </style>
            """
            spectrum_html = f"""
            <div class="spectrum-wrapper">
                <div class="spectrum-header">
                    <p class="spectrum-title">Global Metabolic Distribution Spectrum</p>
                    <p class="spectrum-highlight">{rank_text}</p>
                </div>
                <div class="spectrum-track">
                    <div class="spectrum-zone-label zone-l3">Level 3 (Bottom 55.5%)</div>
                    <div class="spectrum-zone-label zone-l2">Level 2 (Middle 22.2%)</div>
                    <div class="spectrum-zone-label zone-l1">Level 1 (Top 22.2%)</div>
                    <div class="spectrum-marker"></div>
                    <div class="spectrum-tooltip">YOU ARE HERE</div>
                </div>
            </div>
            """
            return spectrum_css + spectrum_html

    # -----------------------------------------------------------------
    # [DATA LAYER] State Machine & Real User Data Extraction
    # -----------------------------------------------------------------
    res = st.session_state.prediction
    
    config = {
        "Low Efficiency": {"c": "#E63946", "pct": 27, "rank_text": "Bottom 27%", "vfx": 4},
        "Moderate": {"c": "#F4A261", "pct": 66, "rank_text": "Top 34%", "vfx": 0},
        "High Efficiency": {"c": "#2A9D8F", "pct": 89, "rank_text": "Top 11%", "vfx": -3}
    }.get(res, {"c": "#333", "pct": 50, "rank_text": "Average", "vfx": 0})

    if config["vfx"] > 0:
        for _ in range(config["vfx"]): st.snow()
    elif config["vfx"] < 0:
        for _ in range(abs(config["vfx"])): st.balloons()

    # Safely extract user data filled in Page B (fixed body fat display)
    try:
        rm = st.session_state.raw_matrix.iloc[0]
        age_val = int(rm['age'])
        steps_val = int(rm['steps_per_day'])
        active_val = int(rm['active_minutes'])
        workouts_val = int(rm['workouts_per_week'])
        rhr_val = int(rm['heart_rate_resting'])
        ahr_val = int(rm['heart_rate_avg'])
        sleep_val = float(rm['sleep_hours'])
        water_val = float(rm['hydration_liters'])
        bmi_val = float(rm['bmi'])
        bf_val = float(rm['body_fat_percentage'])   # Already a percentage value, no need to multiply by 100
        muscle_val = float(rm['muscle_mass_ratio'])
    except:
        age_val=steps_val=active_val=workouts_val=rhr_val=ahr_val=sleep_val=water_val=bmi_val=bf_val=muscle_val=0

    # -----------------------------------------------------------------
    # [VIEW LAYER] UI Assembly
    # -----------------------------------------------------------------
    UI_Architect.render(f"""
        <h1 style='text-align:center; color:{config['c']}; font-weight:900; font-size:45px; text-transform:uppercase; margin-bottom: 0;'>
            {res} DETECTED
        </h1>
        <p style='text-align:center; color:#666; font-size:18px;'>AI Assessment Complete | Peer Comparison Locked</p>
    """)

    # 1. Render global spectrum progress bar
    UI_Architect.render(MetabolicSpectrumRenderer.build_spectrum(config["pct"], config["rank_text"], config["c"]))

    # =========================================================================
    # Replace the long text and capsule tags: use a concise comparison table + key gap snapshot
    # =========================================================================
    
    # ----- International benchmark values (WHO / ACSM recommendations) -----
    benchmarks = {
        "steps": {"name": "Daily Steps", "unit": "steps", "benchmark": 10000, "higher_better": True},
        "active_mins": {"name": "Active Minutes", "unit": "min/day", "benchmark": 45, "higher_better": True},
        "bmi": {"name": "BMI", "unit": "", "benchmark": 22.0, "higher_better": False},
        "body_fat": {"name": "Body Fat", "unit": "%", "benchmark": 15.0 if st.session_state.get("user_gender", "Male") == "Male" else 22.0, "higher_better": False},
        "sleep": {"name": "Sleep", "unit": "h", "benchmark": 8.0, "higher_better": True},
        "hydration": {"name": "Hydration", "unit": "L", "benchmark": 2.5, "higher_better": True}
    }
    
    # User value mapping
    user_vals = {
        "steps": steps_val,
        "active_mins": active_val,
        "bmi": bmi_val,
        "body_fat": bf_val,
        "sleep": sleep_val,
        "hydration": water_val
    }
    
    # Calculate achievement ratio and status for each metric
    def get_ratio_and_status(key):
        meta = benchmarks[key]
        user = user_vals[key]
        bench = meta["benchmark"]
        if meta["higher_better"]:
            ratio = user / bench if bench > 0 else 0
        else:
            ratio = bench / user if user > 0 else 0
        ratio = min(1.0, max(0, ratio))
        if ratio >= 0.95:
            status = "Excellent"
            color = "#2A9D8F"
        elif ratio >= 0.75:
            status = "Good"
            color = "#F4A261"
        else:
            status = "Needs Work"
            color = "#E63946"
        return ratio, status, color
    
    # ----- Key gap snapshot (find the two metrics with largest gaps) -----
    gaps = []
    for key in benchmarks:
        ratio, _, _ = get_ratio_and_status(key)
        gaps.append((key, ratio))
    gaps.sort(key=lambda x: x[1])  # ascending, worst first
    worst_key = gaps[0][0]
    second_key = gaps[1][0] if len(gaps) > 1 else None
    
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🔍 Key Gap Snapshot</h3>", unsafe_allow_html=True)
    
    # Show the two worst metrics
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        meta_w = benchmarks[worst_key]
        user_w = user_vals[worst_key]
        bench_w = meta_w["benchmark"]
        ratio_w, status_w, color_w = get_ratio_and_status(worst_key)
        if meta_w["higher_better"]:
            diff_text = f"{user_w - bench_w:.0f} below" if user_w < bench_w else f"{user_w - bench_w:.0f} above"
        else:
            diff_text = f"{user_w - bench_w:.1f} above" if user_w > bench_w else f"{user_w - bench_w:.1f} below"
        st.markdown(f"""
        <div style="background:#f8f9fa; border-radius:12px; padding:15px; border-left:4px solid {color_w};">
            <span style="font-size:14px; font-weight:bold;">⚠️ {meta_w['name']}</span><br>
            <span style="font-size:24px; font-weight:800;">{user_w:.1f}</span> <span style="font-size:14px;">{meta_w['unit']}</span><br>
            <span style="font-size:13px; color:#666;">vs Elite benchmark {bench_w}{meta_w['unit']} → {diff_text}</span>
            <div style="background:#e9ecef; border-radius:10px; height:8px; margin:10px 0;">
                <div style="background:{color_w}; width:{ratio_w*100}%; height:8px; border-radius:10px;"></div>
            </div>
            <span style="font-size:13px;">Achievement: {ratio_w*100:.0f}% • {status_w}</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col_g2:
        if second_key:
            meta_s = benchmarks[second_key]
            user_s = user_vals[second_key]
            bench_s = meta_s["benchmark"]
            ratio_s, status_s, color_s = get_ratio_and_status(second_key)
            if meta_s["higher_better"]:
                diff_text_s = f"{user_s - bench_s:.0f} below" if user_s < bench_s else f"{user_s - bench_s:.0f} above"
            else:
                diff_text_s = f"{user_s - bench_s:.1f} above" if user_s > bench_s else f"{user_s - bench_s:.1f} below"
            st.markdown(f"""
            <div style="background:#f8f9fa; border-radius:12px; padding:15px; border-left:4px solid {color_s};">
                <span style="font-size:14px; font-weight:bold;">📉 {meta_s['name']}</span><br>
                <span style="font-size:24px; font-weight:800;">{user_s:.1f}</span> <span style="font-size:14px;">{meta_s['unit']}</span><br>
                <span style="font-size:13px; color:#666;">vs Elite benchmark {bench_s}{meta_s['unit']} → {diff_text_s}</span>
                <div style="background:#e9ecef; border-radius:10px; height:8px; margin:10px 0;">
                    <div style="background:{color_s}; width:{ratio_s*100}%; height:8px; border-radius:10px;"></div>
                </div>
                <span style="font-size:13px;">Achievement: {ratio_s*100:.0f}% • {status_s}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='background:#f8f9fa; border-radius:12px; padding:15px; text-align:center;'>✨ You're crushing it! Keep going.</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
        # ----- Full comparison table (all metrics) -----
    st.markdown("<h3 style='text-align: center;'>📊 Your Biometrics vs. Elite Benchmark</h3>", unsafe_allow_html=True)
    
    # Build DataFrame
    import pandas as pd
    table_data = []
    for key in benchmarks:
        meta = benchmarks[key]
        user = user_vals[key]
        bench = meta["benchmark"]
        ratio, status, color = get_ratio_and_status(key)
        # Generate text progress bar (10 bars)
        filled = int(ratio * 10)
        bar = "█" * filled + "░" * (10 - filled)
        table_data.append({
            "Metric": meta['name'],
            "You": f"{user:.1f}{' '+meta['unit'] if meta['unit'] else ''}",
            "Elite Benchmark": f"{bench}{' '+meta['unit'] if meta['unit'] else ''}",
            "Achievement": f"{bar} {ratio*100:.0f}%",
            "Status": status
        })
    df = pd.DataFrame(table_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Gentle overall advice
    st.info(f"💡 **Gentle Insight**: Your biggest lever is **{benchmarks[worst_key]['name']}**. A small improvement here would significantly boost your metabolic efficiency. Most users who improved this metric moved up one level within 8 weeks.")
    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Render three-tier horizontal comparison (with upgrade conditions)
    act1 = "active" if res == "High Efficiency" else ""
    act2 = "active" if res == "Moderate" else ""
    act3 = "active" if res == "Low Efficiency" else ""
    
    # Hardcoded upgrade conditions (based on international benchmarks)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        upgrade_hint = ""
        if res != "High Efficiency":
            upgrade_hint = "<div class='upgrade-hint'>🔓 To reach LEVEL 1: Achieve ≥10,000 steps/day, ≥45 active mins, and body fat ≤15% (M) / ≤22% (F).</div>"
        UI_Architect.render(f"<div class='tier-card {act1}' style='border-color: #28A745;'><div class='tier-icon'>⚡</div><div class='tier-title' style='color:#28A745;'>LEVEL 1: ELITE</div><div class='tier-desc'>Top 22% metabolic engine. Muscle hypertrophy state. Standard routines are obsolete.</div>{upgrade_hint}</div>")
    
    with col2:
        upgrade_hint = ""
        if res == "Low Efficiency":
            upgrade_hint = "<div class='upgrade-hint'>🔓 To reach LEVEL 2: Increase daily steps to 8,000+ OR active minutes to 30+.</div>"
        elif res == "High Efficiency":
            upgrade_hint = "<div class='upgrade-hint'>🏆 You are above this level. Keep pushing to Elite!</div>"
        UI_Architect.render(f"<div class='tier-card {act2}' style='border-color: #F4A261;'><div class='tier-icon'>⚙️</div><div class='tier-title' style='color:#F4A261;'>LEVEL 2: STEADY</div><div class='tier-desc'>Metabolic plateau. Requires precise heart-rate overload to break through.</div>{upgrade_hint}</div>")
    
    with col3:
        upgrade_hint = ""
        if res != "Low Efficiency":
            upgrade_hint = "<div class='upgrade-hint'>✅ You have surpassed this level. Great work!</div>"
        UI_Architect.render(f"<div class='tier-card {act3}' style='border-color: #E63946;'><div class='tier-icon'>⚠️</div><div class='tier-title' style='color:#E63946;'>LEVEL 3: SAVER</div><div class='tier-desc'>Majority bracket. High risk of metabolic adaptation. Immediate reset recommended.</div>{upgrade_hint}</div>")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =========================================================================
    # The radar chart and detailed metric cards remain unchanged (you already confirmed they are good)
    # =========================================================================
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>⚡ Gap Analysis vs. High-Efficiency Group</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Based on real training data from the top metabolic performers</p>", unsafe_allow_html=True)
    
    # ----- Define benchmark data (high-efficiency group averages, based on previous feature importance) -----
    gender_ref = st.session_state.get("user_gender", "Male")
    if gender_ref == "Male":
        benchmark_body_fat_high = 14.0
    else:
        benchmark_body_fat_high = 21.0

    benchmarks_high = {
        "steps_per_day": {"name": "Daily Steps", "unit": "steps", "benchmark": 11500, "higher_better": True, "importance": 0.32},
        "active_minutes": {"name": "Active Minutes", "unit": "min/day", "benchmark": 55, "higher_better": True, "importance": 0.11},
        "bmi": {"name": "BMI", "unit": "", "benchmark": 22.5, "higher_better": False, "importance": 0.08},
        "workouts_per_week": {"name": "Workouts/Week", "unit": "x", "benchmark": 4.5, "higher_better": True, "importance": 0.06},
        "body_fat_percentage": {"name": "Body Fat", "unit": "%", "benchmark": benchmark_body_fat_high, "higher_better": False, "importance": 0.02},
        "muscle_mass_ratio": {"name": "Muscle Ratio", "unit": "", "benchmark": 0.62, "higher_better": True, "importance": 0.03}
    }
    
    # Get user actual values
    user_values = {}
    for key in benchmarks_high.keys():
        try:
            if key == "body_fat_percentage":
                user_values[key] = bf_val
            elif key == "muscle_mass_ratio":
                user_values[key] = muscle_val
            elif key == "workouts_per_week":
                user_values[key] = workouts_val
            elif key == "steps_per_day":
                user_values[key] = steps_val
            elif key == "active_minutes":
                user_values[key] = active_val
            elif key == "bmi":
                user_values[key] = bmi_val
            else:
                user_values[key] = st.session_state.raw_matrix[key].values[0]
        except:
            user_values[key] = 0
    
    # ----- Radar chart drawing (using plotly) -----
    try:
        import plotly.graph_objects as go
        
        radar_categories = [benchmarks_high[k]["name"] for k in benchmarks_high.keys()]
        user_radar = []
        for k in benchmarks_high.keys():
            bench_val = benchmarks_high[k]["benchmark"]
            user_val = user_values[k]
            if benchmarks_high[k]["higher_better"]:
                ratio = user_val / bench_val if bench_val > 0 else 0
            else:
                ratio = bench_val / user_val if user_val > 0 else 0
            ratio = min(2.0, max(0, ratio))
            user_radar.append(ratio)
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=user_radar,
            theta=radar_categories,
            fill='toself',
            name='Your Result',
            line_color='#FF4B4B',
            fillcolor='rgba(255,75,75,0.3)',
            hoverinfo='text',
            text=[f"{benchmarks_high[k]['name']}: {user_values[k]:.1f}{benchmarks_high[k]['unit']}<br>Elite benchmark: {benchmarks_high[k]['benchmark']}{benchmarks_high[k]['unit']}<br>Achievement: {user_radar[i]*100:.0f}%" for i,k in enumerate(benchmarks_high.keys())]
        ))
        fig.add_trace(go.Scatterpolar(
            r=[1.0]*len(radar_categories),
            theta=radar_categories,
            fill='toself',
            name='High-Efficiency Avg',
            line_color='#2A9D8F',
            fillcolor='rgba(42,157,143,0.2)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1.8],
                    tickvals=[0.5, 1.0, 1.5],
                    ticktext=['50%', 'Baseline', '150%']
                ),
                angularaxis=dict(tickfont=dict(size=12, weight='bold'))
            ),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
            title=dict(text="<b>Multi-Dimensional Metabolic Radar</b>", x=0.5, font=dict(size=18)),
            margin=dict(l=80, r=80, t=80, b=40),
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            transition={'duration': 500}
        )
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.warning(f"Radar chart failed to load (plotly may not be installed): {e}")
    
    # ----- Detailed metric comparison cards (sorted by importance) -----
    st.markdown("<br><h3 style='text-align: center;'>📊 Detailed Metric Breakdown</h3>", unsafe_allow_html=True)
    
    sorted_keys = sorted(benchmarks_high.keys(), key=lambda x: benchmarks_high[x]["importance"], reverse=True)[:5]
    
    for key in sorted_keys:
        meta = benchmarks_high[key]
        user_val = user_values[key]
        bench_val = meta["benchmark"]
        higher_better = meta["higher_better"]
        
        if higher_better:
            ratio = user_val / bench_val if bench_val > 0 else 0
        else:
            ratio = bench_val / user_val if user_val > 0 else 0
        ratio = min(1.0, max(0, ratio))
        percent = int(ratio * 100)
        
        if percent >= 90:
            color = "#2A9D8F"
            status = "Excellent"
        elif percent >= 70:
            color = "#F4A261"
            status = "Good"
        else:
            color = "#E63946"
            status = "Needs Work"
        
        # Gentle advice
        if percent < 70:
            if key == "steps_per_day":
                advice = "💡 Gentle advice: +2,000 steps/day could boost your metabolism noticeably within a month."
            elif key == "active_minutes":
                advice = "💡 Gentle advice: Extend your intense interval by 5 minutes each session — small change, big impact."
            elif key == "bmi":
                advice = "💡 Gentle advice: Focus on body recomposition rather than weight loss. Strength training helps."
            elif key == "workouts_per_week":
                advice = "💡 Gentle advice: Adding one more strength session per week can accelerate fat loss."
            elif key == "body_fat_percentage":
                advice = "💡 Gentle advice: Slight reduction in refined carbs + HIIT twice a week will lower body fat effectively."
            else:
                advice = "💡 Gentle advice: Small consistent improvements in this area will bring you closer to the elite group."
        else:
            advice = "🎉 Congratulations! You're already matching the high-efficiency group on this metric. Keep it up!"
        
        col1, col2, col3 = st.columns([2, 3, 3])
        with col1:
            st.markdown(f"**{meta['name']}**<br><span style='font-size:12px; color:#aaa;'>Importance weight {meta['importance']*100:.0f}%</span>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<span style='font-size:28px; font-weight:800;'>{user_val:.1f}</span> <span style='font-size:14px;'>{meta['unit']}</span><br><span style='font-size:14px; color:#888;'>vs Elite avg {bench_val}{meta['unit']}</span>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div style="background-color:#e9ecef; border-radius:20px; height:12px; width:100%; margin-top:15px;">
                <div style="background-color:{color}; width:{percent}%; height:12px; border-radius:20px; transition: width 0.8s ease;"></div>
            </div>
            <div style="display:flex; justify-content:space-between; margin-top:5px;">
                <span style="font-size:13px;">Achievement <b>{percent}%</b></span>
                <span style="font-size:13px; color:{color};">{status}</span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:13px; margin-top: -10px; margin-bottom: 20px;'>{advice}</p>", unsafe_allow_html=True)
        st.markdown("<hr style='margin: 5px 0 20px 0; opacity:0.2;'>", unsafe_allow_html=True)
    
    # Summarize the metric with the largest gap
    worst_key_high = None
    worst_ratio = 1.0
    for key in benchmarks_high.keys():
        meta = benchmarks_high[key]
        user_val = user_values[key]
        bench_val = meta["benchmark"]
        if meta["higher_better"]:
            ratio = user_val / bench_val if bench_val > 0 else 1
        else:
            ratio = bench_val / user_val if user_val > 0 else 1
        if ratio < worst_ratio:
            worst_ratio = ratio
            worst_key_high = key
    
    if worst_key_high and worst_ratio < 0.85:
        worst_name = benchmarks_high[worst_key_high]["name"]
        st.info(f"🔍 **Your biggest gap**: {worst_name}. Many high-efficiency users started by improving this metric. We've designed a specific plan to help you close this gap.")
    else:
        st.success("🌟 **Fantastic!** You're already close to the high-efficiency profile. A few more weeks of consistency will push you into the top tier.")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # 4. Commercial funnel button
    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        if st.button("🔓 REVEAL COMMERCIAL INTERVENTION (Phase 2)", use_container_width=True, type="primary"):
            st.session_state.page = 'plan'
            st.rerun()
# ==========================================
# Page D: 💰 Personalized Commercial Prescription (Data-Driven)
# ==========================================
elif st.session_state.page == 'plan':
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # Get user's weakest metric from session_state (already calculated in Page C)
    # If not stored in Page C, recalculate for compatibility
    try:
        rm = st.session_state.raw_matrix.iloc[0]
        steps_val = int(rm['steps_per_day'])
        active_val = int(rm['active_minutes'])
        bf_val = float(rm['body_fat_percentage'])
        # Recalculate worst metric (consistent with Page C logic)
        benchmarks_local = {
            "steps": steps_val,
            "active_mins": active_val,
            "body_fat": bf_val
        }
        bench_steps = 10000
        bench_active = 45
        bench_bf = 15.0 if st.session_state.get("user_gender", "Male") == "Male" else 22.0
        ratios = {
            "steps": min(1.0, steps_val / bench_steps),
            "active_mins": min(1.0, active_val / bench_active),
            "body_fat": min(1.0, bench_bf / bf_val) if bf_val > 0 else 0
        }
        worst_key = min(ratios, key=ratios.get)
        worst_ratio = ratios[worst_key]
    except:
        worst_key = "steps"
        worst_ratio = 0.5
    
    res = st.session_state.prediction
    
    # Dynamic title
    st.markdown(f"<h1 style='text-align:center; color:#FF2A2A;'>Your Personalized Prescription</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 18px; color:#555;'>Based on your <b>{res}</b> profile and your biggest gap: <b>{worst_key.replace('_',' ').title()}</b></p><hr>", unsafe_allow_html=True)
    
    # Generate personalized action suggestions based on level and gap (do not change course package type)
    if res == "Low Efficiency":
        st.markdown("### 🐢 Your Metabolic Reality")
        st.markdown(f"Your largest gap is **{worst_key.replace('_',' ').title()}**. Our data shows that users at Level 3 typically struggle with daily movement volume and consistent nutrition.")
        
        # Custom tips based on specific gap
        if worst_key == "steps":
            st.info("📌 **Personalized Tip**: Increase your daily steps by 2,000. Try a 15-min walk after lunch and park farther away. This alone can boost your metabolism by 12% in 4 weeks.")
        elif worst_key == "active_mins":
            st.info("📌 **Personalized Tip**: Your active minutes are below target. Replace 30 min of steady cardio with 20 min of HIIT (1 min sprint, 2 min rest). You'll burn more fat in less time.")
        elif worst_key == "body_fat":
            st.info("📌 **Personalized Tip**: Slight reduction in refined carbs + adding protein to each meal will accelerate fat loss. Aim for 1g protein per lb of body weight.")
        else:
            st.info("📌 **Personalized Tip**: Focus on consistency. Small daily improvements in your weakest metric will yield the fastest results.")
        
        st.markdown("""
        ### 💡 Recommended Program: Foundation Builder
        You don't need a punishing personal trainer right now. You need habit engineering, accountability, and low-impact volume.
        """)
        
        st.markdown("""
        <div style="background: #f8f9fa; padding: 25px; border-radius: 15px; border-left: 8px solid #FF4B4B; margin: 20px 0;">
            <h2 style="color: #FF4B4B; margin-top:0;">📦 "21-Day Metabolic Wake-Up Camp"</h2>
            <p style="font-size: 16px; color:#444;">Group classes + basic personal training focused on your #1 gap: <b>{}</b>.</p>
            <h4 style="color:#333;">What You Get:</h4>
            <ul style="font-size: 16px;">
                <li><b>🚲 12 Immersive Group Cycling Classes:</b> Low-impact, high fun, builds step foundation.</li>
                <li><b>⌚ Smart Wearable Integration:</b> TAs monitor your daily steps to hit 10,000 baseline.</li>
                <li><b>📸 Daily Nutritional Check-ins:</b> Snap meal photos – no strict dieting, just awareness.</li>
                <li><b>🤝 Tribe Accountability:</b> Squad of 10 with same metabolic profile.</li>
            </ul>
            <h3 style="color: #FF2A2A; text-align:right;">Starter Offer: $99 / Month</h3>
        </div>
        """.format(worst_key.replace('_',' ').title()), unsafe_allow_html=True)
        btn_text = "🛒 Secure Your Spot in Wake-Up Camp"

    elif res == "Moderate":
        st.markdown("### 🚶‍♂️ Your Metabolic Reality")
        st.markdown(f"Your biggest gap is **{worst_key.replace('_',' ').title()}**. You have discipline but lack efficiency. Your active minutes are likely compromised by 'junk volume'.")
        
        if worst_key == "steps":
            st.info("📌 **Personalized Tip**: Your steps are decent, but increasing to 12,000/day will push you into the next tier. Try a 30-min morning walk.")
        elif worst_key == "active_mins":
            st.info("📌 **Personalized Tip**: Extend your intense interval by 5 minutes each session. Use a heart rate monitor to stay in zone 4-5 for at least 15 minutes.")
        elif worst_key == "body_fat":
            st.info("📌 **Personalized Tip**: Add two full-body resistance sessions per week. Muscle is your metabolic engine – more muscle, higher resting burn.")
        else:
            st.info("📌 **Personalized Tip**: Precision overload is key. Focus on heart-rate targeting and structured intensity.")
        
        st.markdown("""
        ### 💡 Recommended Program: Metabolic Breakthrough
        You need a professional coach to disrupt your plateau and maximize your active minutes.
        """)
        
        st.markdown("""
        <div style="background: #f8f9fa; padding: 25px; border-radius: 15px; border-left: 8px solid #FF8C00; margin: 20px 0;">
            <h2 style="color: #FF8C00; margin-top:0;">📦 "1V1 Metabolic Breakthrough Program"</h2>
            <p style="font-size: 16px; color:#444;">Elite personal training focused entirely on your #1 gap: <b>{}</b>.</p>
            <h4 style="color:#333;">What You Get:</h4>
            <ul style="font-size: 16px;">
                <li><b>🏋️ 8 x 1-on-1 HIIT Sessions:</b> 45 min pure metabolic conditioning.</li>
                <li><b>🫀 Live Heart-Rate Tracking:</b> Chest strap ensures you stay in fat-burning zone.</li>
                <li><b>🥗 Macro-Nutrient Realignment:</b> Exact protein/carb needs to fuel intensity.</li>
                <li><b>📊 Weekly Data Review:</b> Coach reviews smartwatch data and tweaks variables.</li>
            </ul>
            <h3 style="color: #FF8C00; text-align:right;">Best Value: $249 / Month</h3>
        </div>
        """.format(worst_key.replace('_',' ').title()), unsafe_allow_html=True)
        btn_text = "🛒 Book Your 1V1 Transformation"

    else: # High Efficiency
        st.markdown("### ⚡ Your Metabolic Reality")
        st.markdown(f"Your biggest gap is **{worst_key.replace('_',' ').title()}**. You've mastered steps and duration. Your body needs body recomposition, not weight loss.")
        
        if worst_key == "steps":
            st.info("📌 **Personalized Tip**: Maintain your step count but shift focus to strength training. Add progressive overload to build lean mass.")
        elif worst_key == "active_mins":
            st.info("📌 **Personalized Tip**: Your active minutes are elite. Now incorporate periodized training – undulating intensity to force adaptation.")
        elif worst_key == "body_fat":
            st.info("📌 **Personalized Tip**: Slight calorie deficit + high protein + carb cycling will reveal the muscle underneath. Consider DEXA scan for precision.")
        else:
            st.info("📌 **Personalized Tip**: Biomechanics and recovery are your next frontier. Ice baths, sauna, and mobility work will unlock the final 5%.")
        
        st.markdown("""
        ### 💡 Recommended Program: Elite Physique Sculpting
        You need a top-tier coach who understands biomechanics, periodization, and elite recovery.
        """)
        
        st.markdown("""
        <div style="background: #f8f9fa; padding: 25px; border-radius: 15px; border-left: 8px solid #28A745; margin: 20px 0;">
            <h2 style="color: #28A745; margin-top:0;">📦 "Elite Masterclass: Physique Sculpting"</h2>
            <p style="font-size: 16px; color:#444;">Reserved for high-efficiency individuals. Paired with national-level competitors and biomechanics experts.</p>
            <h4 style="color:#333;">What You Get:</h4>
            <ul style="font-size: 16px;">
                <li><b>🦾 Advanced Hypertrophy Programming:</b> Complex periodization, drop sets, eccentric overloading.</li>
                <li><b>🔬 DEXA Scan Analysis:</b> Monthly clinical body composition testing.</li>
                <li><b>🧊 Elite Recovery Access:</b> Unlimited contrast therapy (ice baths + infrared saunas).</li>
                <li><b>🍽️ Peak Week Nutrition:</b> Carb-cycling protocols used by fitness models.</li>
            </ul>
            <h3 style="color: #28A745; text-align:right;">VIP Experience: $450 / Month</h3>
        </div>
        """, unsafe_allow_html=True)
        btn_text = "🛒 Apply for Elite Masterclass"

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- Show projected improvement timeline (based on gap ratio) ---
    weeks_needed = max(4, min(12, int((1 - worst_ratio) * 20)))
    st.info(f"⏱️ **Your projected timeline**: With consistent adherence, you can reach the next metabolic level in approximately **{weeks_needed} weeks**. Many users with a similar gap achieved this within {weeks_needed-2}-{weeks_needed} weeks.")
    
    # --- Action Buttons ---
    col_buy, col_back = st.columns([2, 1])
    with col_buy:
        if st.button(btn_text, use_container_width=True, type="primary"):
            st.balloons()
            st.success("🎉 Registration Confirmed! A dedicated account manager will call you within 2 hours to finalize your schedule.")
            
    with col_back:
        if st.button("🔄 Test Another Client", use_container_width=True):
            st.session_state.page = 'home'
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    import os
import joblib


base_path = os.path.dirname(__file__)

model_path = os.path.join(base_path, 'rf_model.pkl')

model = joblib.load(model_path)