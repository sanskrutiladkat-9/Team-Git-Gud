import streamlit as st
import random

st.set_page_config(page_title="MindNest", page_icon="🌿", layout = "wide")
st.markdown("""
<style>

/* Full Page Background Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #dbeafe, #f0fdf4);
}

/* Remove default dark background */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
/* Banner Styling */
.hero {
    background: linear-gradient(135deg, #4e73df, #1cc88a);
    padding: 80px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    animation: fadeIn 1.5s ease-in;
}

/* Smooth Fade In */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Card Styling */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
    animation: fadeIn 1s ease-in;
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
    st.title("🌿 MindNest")
    st.markdown("### Anonymous Support System")
    st.write("Step-Based Mental Health Assistance")

    language = st.selectbox("🌍 Select Language", ["English", "Hindi"])

    st.markdown("---")
    st.caption("Emergency Helpline")
    st.write("📞 1800-599-0019")

if "alias" not in st.session_state:
    st.session_state.alias = "User-" + str(random.randint(1000, 9999))

st.markdown("---")

st.subheader("How are you feeling today?")

col1, col2 = st.columns(2)

with col1:
    mood = st.radio(
        "Select your current state:",
        ["Mild Stress", "Moderate Distress"]
    )

with col2:
    mood2 = st.radio(
        " ",
        ["Severe Distress", "Acute Crisis"]
    )

mood = mood if mood else mood2
st.markdown("---")

user_input = st.text_area("Share what's on your mind...")

if user_input:
    risky_words = ["suicide", "kill myself", "end my life", "hopeless", "worthless"]

    if any(word in user_input.lower() for word in risky_words):
        st.error("⚠ High-Risk Indicators Detected")
        st.write("You may be experiencing severe emotional distress.")
        st.write("Would you like immediate anonymous connection to a crisis counselor?")
        st.write("📞 KIRAN: 1800-599-0019")
    else:
        st.success("Thank you for sharing. Your feelings are valid and important 🌿")
