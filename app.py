import streamlit as st
import random

st.set_page_config(page_title="Aalamban", page_icon="🌿")

if "alias" not in st.session_state:
    st.session_state.alias = "User-" + str(random.randint(1000, 9999))

st.title("🌿 Aalamban")
st.write(f"Anonymous ID: {st.session_state.alias}")
st.caption("Your identity is protected. No personal data is stored.")

st.markdown("---")

st.subheader("How are you feeling today?")

mood = st.radio(
    "Select your current state:",
    ["Mild Stress", "Moderate Distress", "Severe Distress", "Acute Crisis"]
)

if mood == "Mild Stress":
    st.success("Step 1 Activated: AI Self-Guided Support")

elif mood == "Moderate Distress":
    st.warning("Step 2 Activated: Peer Support (Barefoot Counselor)")

elif mood == "Severe Distress":
    st.error("Step 3 Activated: Clinical Counseling Recommended")

elif mood == "Acute Crisis":
    st.error("Step 4 Activated: Immediate Medical Intervention Required")
    st.write("📞 KIRAN Helpline: 1800-599-0019")

st.markdown("---")

user_input = st.text_area("Share what's on your mind...")

if user_input:
    risky_words = ["suicide", "kill myself", "hopeless", "worthless"]

    if any(word in user_input.lower() for word in risky_words):
        st.error("⚠ Red Flag Detected.")
        st.write("📞 Please contact KIRAN: 1800-599-0019")
    else:
        st.success("Thank you for sharing. You are heard 🌿")
