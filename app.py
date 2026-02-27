import streamlit as st
import random

# FIXED: Added missing braces and commas
translations = {
    "English": {
        "welcome": "Anonymous, Multilingual Mental Health Support",
        "mood_question": "How are you feeling today?",
        "share": "Share what's on your mind...",
        "mild": "Mild Stress",
        "moderate": "Moderate Distress",
        "severe": "Severe Distress",
        "acute": "Acute Crisis"
    }, # Added comma
    "Hindi": {
        "welcome": "गोपनीय बहुभाषी मानसिक स्वास्थ्य सहायता",
        "mood_question": "आप आज कैसा महसूस कर रहे हैं?",
        "share": "अपने मन की बात यहाँ लिखें...",
        "mild": "हल्का तनाव",
        "moderate": "मध्यम परेशानी",
        "severe": "गभीर तनाव",
        "acute": "आपात स्थिति"
    }, # Added comma
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

st.set_page_config(page_title="MindNest", page_icon="🌿", layout="wide")

# ... (Your CSS remains the same) ...
st.markdown("<style>...</style>", unsafe_allow_html=True) 

# Sidebar setup first so we can define 't'
with st.sidebar:
    # Note: Ensure "assets/logo image.png" exists in your folder!
    # st.image("assets/logo image.png", width=700) 
    st.title("🌿 MindNest")
    language = st.selectbox("🌍 Select Language", ["English", "Hindi", "Marathi"])
    t = translations[language] # Define 't' here

# Hero Section
st.markdown(f"""
<div class="hero">
    <h1 style="font-size:50px; margin-bottom:10px;">🌿 MindNest</h1>
    <h3 style="margin-bottom:15px;">{t['welcome']}</h3>
    <p style="font-size:18px;">
        AI-Augmented Early Intervention • Zero-Trace Privacy • Stepped-Care Escalation
    </p>
</div>
""", unsafe_allow_html=True)

st.subheader(t["mood_question"])

# FIXED: Simplified mood selection to avoid the "two radio button" conflict
mood_options = [t["mild"], t["moderate"], t["severe"], t["acute"]]
selected_mood = st.select_slider("Select the intensity of your distress:", options=mood_options)

st.markdown("---")
user_input = st.text_area(t["share"])

if user_input:
    risky_words = ["suicide", "kill myself", "end my life", "hopeless", "worthless"]
    if any(word in user_input.lower() for word in risky_words):
        st.error("⚠ High-Risk Indicators Detected")
        st.write("📞 KIRAN: 1800-599-0019")
    else:
        st.success("Thank you for sharing. Your feelings are valid and important 🌿")
