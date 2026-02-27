import streamlit as st
import random

st.markdown("""
### Omnichannel AI-Augmented Mental Health Ecosystem  
Providing anonymous, multilingual early intervention and stepped-care escalation.
""")

st.set_page_config(page_title="MindNest", page_icon="🌿")

if "alias" not in st.session_state:
    st.session_state.alias = "User-" + str(random.randint(1000, 9999))

st.title("🌿 MindNest")
st.write(f"Anonymous ID: {st.session_state.alias}")
st.caption("Your identity is protected. No personal data is stored.")

st.markdown("---")

st.subheader("How are you feeling today?")

mood = st.radio(
    "Select your current state:",
    ["Mild Stress", "Moderate Distress", "Severe Distress", "Acute Crisis"]
)

if mood == "Mild Stress":
    st.success("🟢 Step 1: AI Self-Guided Support Activated")
    st.write("• Guided breathing")
    st.write("• Grounding exercises")
    st.write("• Psychoeducation modules")

elif mood == "Moderate Distress":
    st.warning("🟡 Step 2: Peer Support (Barefoot Counselor)")
    st.write("You can be connected anonymously to a trained volunteer.")

elif mood == "Severe Distress":
    st.error("🟠 Step 3: Clinical Counseling Recommended")
    st.write("Escalation to licensed tele-psychologist.")

elif mood == "Acute Crisis":
    st.error("🔴 Step 4: Emergency Intervention Required")
    st.write("📞 KIRAN Helpline: 1800-599-0019")
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
