import streamlit as st
import random

st.set_page_config(page_title="MindNest", page_icon="🌿")
st.markdown("## 🧠 Welcome to MindNest")
st.markdown("A Safe, Anonymous Space for Emotional Support")
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

st.title("🌿 MindNest")
st.write(f"Anonymous ID: {st.session_state.alias}")
st.caption("Your identity is protected. No personal data is stored.")

st.set_page_config(page_title="MindNest", page_icon="🌿")
st.markdown("---")

st.subheader("How are you feeling today?")
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
