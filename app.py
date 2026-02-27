import streamlit as st
import random

translations = {
    "English": 
        "welcome": "Anonymous, Multilingual Mental Health Support",
        "mood_question": "How are you feeling today?",
        "share": "Share what's on your mind...",
        "mild": "Mild Stress",
        "moderate": "Moderate Distress",
        "severe": "Severe Distress",
        "acute": "Acute Crisis"
    }
    "Hindi": {
        "welcome": "गोपनीय बहुभाषी मानसिक स्वास्थ्य सहायता",
        "mood_question": "आप आज कैसा महसूस कर रहे हैं?",
        "share": "अपने मन की बात यहाँ लिखें...",
        "mild": "हल्का तनाव",
        "moderate": "मध्यम परेशानी",
        "severe": "गंभीर तनाव",
        "acute": "आपात स्थिति"
    }
    "Marathi": {
    "welcome": "गोपनीय बहुभाषिक मानसिक आरोग्य सहाय्य",
    "mood_question": "आज तुम्हाला कसे वाटत आहे?",
        "share": "तुमच्या मनातील विचार येथे लिहा...",
        "mild": "हलका ताण",
        "moderate": "मध्यम त्रास",
        "severe": "तीव्र ताण",
        "acute": "तातडीची परिस्थिती",
        "select_state": "तुमची सध्याची स्थिती निवडा:"
}
}

st.set_page_config(page_title="MindNest", page_icon="🌿", layout = "wide")
st.markdown("""
<style>

/* ================================
   GLOBAL APP STYLING
================================ */

/* Full page background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #dbeafe, #f0fdf4);
}

/* Force all text dark */
[data-testid="stAppViewContainer"] * {
    color: #1f2937 !important;
}

/* Remove default header background */
[data-testid="stHeader"] {
    background: transparent;
}


/* ================================
   SIDEBAR STYLING
================================ */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f8fafc, #e0f2fe) !important;
}

section[data-testid="stSidebar"] * {
    color: #1f2937 !important;
}

/* ================================
   SELECTBOX FIX (Force Light Theme)
================================ */

/* Main selectbox container */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #1f2937 !important;
    border-radius: 10px !important;
    border: 1px solid #d1d5db !important;
}

/* Selected value text */
div[data-baseweb="select"] span {
    color: #1f2937 !important;
}

/* Dropdown menu background */
div[role="listbox"] {
    background-color: #ffffff !important;
}

/* Dropdown options */
div[role="option"] {
    background-color: #ffffff !important;
    color: #1f2937 !important;
}

/* Hover effect */
div[role="option"]:hover {
    background-color: #e0f2fe !important;
}
/* ================================
   INPUT COMPONENTS
================================ */

/* Selectbox */
div[data-testid="stSelectbox"] > div {
    background-color: #ffffff !important;
    border-radius: 10px !important;
    border: 1px solid #d1d5db !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
}

div[data-testid="stSelectbox"] div[role="button"] {
    color: #1f2937 !important;
}

ul[role="listbox"] {
    background-color: white !important;
    color: #1f2937 !important;
}

ul[role="listbox"] li:hover {
    background-color: #e0f2fe !important;
}


/* Text Area */
div[data-testid="stTextArea"] textarea {
    color: #1f2937 !important;
    background-color: white !important;
    border-radius: 10px !important;
    border: 1px solid #d1d5db !important;
}


/* ================================
   CUSTOM UI COMPONENTS
================================ */

/* Banner */
.hero {
    background: linear-gradient(135deg, #4e73df, #1cc88a);
    padding: 80px;
    border-radius: 20px;
    text-align: center;
    color: white !important;
    margin-bottom: 40px;
    animation: fadeIn 1.5s ease-in;
}

/* Card */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
    animation: fadeIn 1s ease-in;
}


/* ================================
   ANIMATIONS
================================ */

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1 style="font-size:50px; margin-bottom:10px;">🌿 MindNest</h1>
    <h3 style="margin-bottom:15px;">Anonymous, Multilingual Mental Health Support</h3>
    <p style="font-size:18px;">
        AI-Augmented Early Intervention • Zero-Trace Privacy • Stepped-Care Escalation
    </p>
</div>
""", unsafe_allow_html=True)
        
st.markdown("---")
with st.sidebar:
    st.image("assets/logo image.png", width=700)
    st.title("🌿 MindNest")
    st.markdown("### Anonymous Support System")
    st.write("Step-Based Mental Health Assistance")

    language = st.selectbox("🌍 Select Language", ["English", "Hindi","Marathi"])
    t = translations[language]

    st.markdown("---")
    st.caption("Emergency Helpline")
    st.write("📞 1800-599-0019")

if "alias" not in st.session_state:
    st.session_state.alias = "User-" + str(random.randint(1000, 9999))

st.markdown("---")

st.subheader(t["mood_question"])
col1, col2 = st.columns(2)

with col1:
    mood = st.radio(
        "Select your current state:",
        [t["mild"], t["moderate"]]
    )

with col2:
    mood2 = st.radio(
        " ",
        [t["severe"], t["acute"]]
         )

mood = mood if mood else mood2
st.markdown("---")

user_input = st.text_area(t["share"])

if user_input:
    risky_words = ["suicide", "kill myself", "end my life", "hopeless", "worthless"]

    if any(word in user_input.lower() for word in risky_words):
        st.error("⚠ High-Risk Indicators Detected")
        st.write("You may be experiencing severe emotional distress.")
        st.write("Would you like immediate anonymous connection to a crisis counselor?")
        st.write("📞 KIRAN: 1800-599-0019")
    else:
        st.success("Thank you for sharing. Your feelings are valid and important 🌿")
