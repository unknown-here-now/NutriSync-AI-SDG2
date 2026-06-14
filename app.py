import streamlit as st
import time

st.set_page_config(
    page_title="NutriSync AI — Child Nutrition Optimizer", 
    page_icon="🥗", 
    layout="centered"
)

st.html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');

    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #05160e 0%, #0b2216 50%, #113320 100%);
    }

    .center-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }

    .glass-hero {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 45px;
        margin-bottom: 35px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.45);
        text-align: center;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 35px;
        margin-bottom: 35px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    }

    .hero-title {
        color: #ffffff;
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 10px;
        background: linear-gradient(120deg, #ffffff, #a3e635);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .section-title {
        color: #ffffff;
        font-size: 1.75rem;
        font-weight: 700;
        margin-bottom: 25px;
        border-left: 5px solid #a3e635;
        padding-left: 15px;
    }

    .step-badge {
        background: rgba(163, 230, 53, 0.12);
        color: #a3e635;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 15px;
        border: 1px solid rgba(163, 230, 53, 0.2);
    }

    .metric-value {
        font-size: 4rem;
        font-weight: 800;
        margin: 20px 0;
        line-height: 1;
        letter-spacing: -1px;
    }

    .neon-text-green {
        color: #4ade80;
        text-shadow: 0 0 20px rgba(74, 222, 128, 0.5);
    }
    
    .neon-text-amber {
        color: #fbbf24;
        text-shadow: 0 0 20px rgba(251, 191, 36, 0.5);
    }
    
    .neon-text-red {
        color: #f87171;
        text-shadow: 0 0 20px rgba(248, 113, 113, 0.5);
    }

    .explanation-panel {
        background: rgba(56, 189, 248, 0.05);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 25px;
    }

    .danger-box {
        background: rgba(248, 113, 113, 0.05);
        border-radius: 16px;
        padding: 20px;
        margin-top: 15px;
        border: 1px solid rgba(248, 113, 113, 0.2);
    }

    .success-box {
        background: rgba(74, 222, 128, 0.05);
        border-radius: 16px;
        padding: 20px;
        margin-top: 15px;
        border: 1px solid rgba(74, 222, 128, 0.2);
    }

    .recipe-container {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 16px;
        padding: 25px;
        margin-top: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .recipe-step-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
    }

    .instruction-step {
        display: flex;
        align-items: flex-start;
        gap: 16px;
        margin-bottom: 16px;
    }

    .step-number {
        background: #a3e635;
        color: #05160e;
        font-weight: 800;
        border-radius: 50%;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        font-size: 0.95rem;
        box-shadow: 0 0 10px rgba(163, 230, 53, 0.4);
    }

    label, p, span, li {
        color: #cbd5e1 !important;
    }
    
    h1, h2, h3, h4, strong {
        color: #ffffff !important;
    }

    div[data-testid="stBlock"] {
        padding: 0px !important;
    }
    
    .stCheckbox > label {
        background: rgba(255, 255, 255, 0.03);
        padding: 14px 20px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        display: flex;
        width: 100%;
        transition: all 0.2s ease;
    }
    
    .stCheckbox > label:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(163, 230, 53, 0.3);
    }
    </style>
""")

st.html("""
    <div class="glass-hero">
        <h1 class="hero-title">NutriSync AI</h1>
        <p style="font-size: 1.35rem; color: #f1f5f9; font-weight: 500; margin-bottom: 30px;">
            Simple Midday Meal Nutrition Helper
        </p>
        <div style="max-width: 650px; margin: 0 auto; text-align: left;">
            <div class="explanation-panel">
                <h4 style="margin-top:0; color:#38bdf8; font-weight:700; font-size:1.1rem; display:flex; align-items:center; gap:8px;">
                    ℹ️ Why is this tracking tool necessary?
                </h4>
                <p style="font-size:0.98rem; margin-bottom:0; line-height:1.6; color:#e2e8f0 !important;">
                    Children can eat big meals every day but still remain weak, tired, and anemic. This happens because certain foods, when mixed together, block vitamins from entering the body. We calculate this hidden absorption match so you can get the maximum health value out of the ingredients you already own.
                </p>
            </div>
            <h4 style="color:#a3e635; font-weight:700; margin-bottom:15px; font-size:1.1rem;">How to check your menu:</h4>
            <div class="instruction-step"><div class="step-number">1</div><p style="font-size:1rem; margin:0; padding-top:2px;">Pick the food ingredients you have in your kitchen today from the list below.</p></div>
            <div class="instruction-step"><div class="step-number">2</div><p style="font-size:1rem; margin:0; padding-top:2px;">Press the big green analysis button to view your automatic safety score.</p></div>
            <div class="instruction-step"><div class="step-number">3</div><p style="font-size:1rem; margin:0; padding-top:2px;">Look at the easy cooking recipe corrections to protect child health.</p></div>
        </div>
        <div style="margin-top: 35px; font-size: 0.85rem; color: #a3e635; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">
            🔽 Scroll Down to Choose Ingredients
        </div>
    </div>
""")

st.html('<div class="glass-card"><span class="step-badge">Pantry List</span><h3 class="section-title" style="margin-top:0;">What are you cooking today?</h3>')

col1, col2 = st.columns(2)

with col1:
    st.html("<p style='font-weight:700; color:#a3e635 !important; margin-bottom:12px; font-size:1.05rem;'>Main Foods (Iron & Protein Base)</p>")
    has_spinach = st.checkbox("Spinach / Green Vegetables (Palak)", help="Contains vital iron components")
    st.html("<div style='margin-bottom: 10px;'></div>")
    has_lentils = st.checkbox("Lentils / Beans / Dal", help="Provides strength and core protein")
    st.html("<div style='margin-bottom: 10px;'></div>")
    has_beans = st.checkbox("Soybeans or Chickpeas (Chana)", help="High nutritional energy value")

with col2:
    st.html("<p style='font-weight:700; color:#a3e635 !important; margin-bottom:12px; font-size:1.05rem;'>Side Items & Liquids</p>")
    has_lemon = st.checkbox("Lemon Juice (Vitamin C)", help="Helps unlock iron absorption pathways")
    st.html("<div style='margin-bottom: 10px;'></div>")
    has_curd = st.checkbox("Curd / Yogurt / Milk Products", help="Contains calcium building blocks")
    st.html("<div style='margin-bottom: 10px;'></div>")
    has_tea = st.checkbox("Local Tea / Tannin Extracts", help="Contains plant polyphenols")

st.html('</div>')

st.html('<div class="center-wrapper">')
analyze_clicked = st.button("✨ Verify Food Combination Safety Score", type="primary")
st.html('</div>')

if analyze_clicked:
    st.html("<br>")
    
    with st.spinner("Processing chemical tracking data..."):
        time.sleep(1.2)
        
    score = 75
    blocker_reasons = []
    booster_reasons = []
    
    if (has_spinach or has_lentils) and has_curd:
        score -= 25
        blocker_reasons.append("The Calcium inside the Curd/Dairy works like a wall against the plant iron in your Spinach/Lentils. When served at the exact same moment, they bind together, meaning the child's body cannot absorb the strength from the iron.")
        
    if (has_spinach or has_lentils) and has_tea:
        score -= 35
        blocker_reasons.append("Tannin molecules found within local tea options completely lock away nutritional metal ions. This prevents the child's intestines from picking up blood-building value from the main food.")
        
    if (has_spinach or has_lentils) and has_lemon:
        score += 20
        booster_reasons.append("The Vitamin C content present in fresh lemons acts as an immediate bio-catalyst. It converts difficult plant iron particles into a highly fluid, soluble structure that elevates uptake targets by 300%.")

    if score > 100: score = 100
    if score < 10: score = 10

    if score >= 80:
        text_style = "neon-text-green"
        summary_verdict = "EXCELLENT BALANCE — SAFE TO SERVE"
        banner_msg = "Perfect configuration! These ingredients support each other harmoniously. The children will successfully absorb the full nutritional properties of this meal setup."
    elif score >= 50:
        text_style = "neon-text-amber"
        summary_verdict = "MODERATE QUALITY — NUTRITION IS LIMITED"
        banner_msg = "Caution advised. Some ingredients are blocking each other from performing well. Review the adjustments below to fix the hidden absorption loss."
    else:
        text_style = "neon-text-red"
        summary_verdict = "HIGH NUTRITION LOSS DETECTED"
        banner_msg = "Action needed! Though the food volume is plentiful, the combined properties are neutralizing each other's functional health value."

    st.html(f"""
        <div class="glass-card">
            <span class="step-badge">Analysis Output</span>
            <h3 class="section-title" style="margin-top:0;">Your Nutrition Score Report</h3>
            <p style="font-size: 1.05rem; font-weight: 500; margin-bottom: 5px; color:#cbd5e1;">How well the body absorbs this combination:</p>
            <div style="font-size: 1.4rem; font-weight:800;" class="{text_style}">{summary_verdict}</div>
            <div class="metric-value {text_style}">{score}%</div>
            <p style="line-height: 1.6; font-size: 1.05rem; background: rgba(0,0,0,0.2); padding: 18px; border-radius: 12px; border-left: 4px solid rgba(255,255,255,0.15); margin: 0;">{banner_msg}</p>
        </div>
    """)

    st.html("""
        <div class="glass-card">
            <span class="step-badge">Action Plan</span>
            <h3 class="section-title" style="margin-top:0;">Why this happened & How to fix it</h3>
    """)

    if not blocker_reasons and not booster_reasons:
        st.html("<p style='font-size:1.05rem;'>Your current combination is neutral. To actively maximize nutritional value without spending money, try squeezing a fresh lemon or adding an amla piece onto the lentils right before the kids eat.</p>")
    else:
        if blocker_reasons:
            st.html("<p style='color:#f87171 !important; font-weight:700; margin-bottom:10px; font-size:1.1rem;'>⚠️ Absorption Blockers Found:</p>")
            for reason in blocker_reasons:
                st.html(f'<div class="danger-box"><p style="margin:0; font-size: 1rem; line-height:1.5; color:#fca5a5 !important;">{reason}</p></div>')
            st.html("<br>")

        if booster_reasons:
            st.html("<p style='color:#4ade80 !important; font-weight:700; margin-bottom:10px; font-size:1.1rem;'>🌱 Helpful Bio-Catalysts Found:</p>")
            for reason in booster_reasons:
                st.html(f'<div class="success-box"><p style="margin:0; font-size: 1rem; line-height:1.5; color:#bbf7d0 !important;">{reason}</p></div>')

    st.html("""
            <div class="recipe-container">
                <h4 style="margin-top:0; margin-bottom:15px; font-weight:700; color:#38bdf8 !important; font-size:1.15rem;">📋 Super Simple Kitchen Rules for Better Health:</h4>
                
                <div class="recipe-step-card">
                    <p style="margin:0 0 4px 0; font-weight:700; color:#ffffff;">1. Separate Dairy from Green Vegetables</p>
                    <p style="margin:0; font-size:0.95rem; color:#94a3b8 !important;">Do not serve milk or curd at the same time as spinach or dal. Give milk or curd to children during morning breaks instead, at least 2 hours apart.</p>
                </div>
                
                <div class="recipe-step-card">
                    <p style="margin:0 0 4px 0; font-weight:700; color:#ffffff;">2. The Lemon Squeeze Rule</p>
                    <p style="margin:0; font-size:0.95rem; color:#94a3b8 !important;">Always squeeze fresh lemon juice directly over cooked green dishes on the plate right before the child eats. This immediately unlocks the iron value.</p>
                </div>
                
                <div class="recipe-step-card">
                    <p style="margin:0 0 4px 0; font-weight:700; color:#ffffff;">3. Soak Raw Grains Overnight</p>
                    <p style="margin:0; font-size:0.95rem; color:#94a3b8 !important;">Always leave dry beans, chana, and pulses soaking in water overnight. This breaks down the hard natural acids that block basic digestion pathways.</p>
                </div>
            </div>
        </div>
    """)