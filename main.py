import streamlit as st
import re
import random
import string

# Page configuration
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
    .stButton > button {
        background-color: #ff6600;
        color: white;
        padding: 0.5em 1em;
        font-size: 16px;
        border: none;
    }
    .password-meter {
        height: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .footer {
        margin-top: 3em;
        padding: 1em;
        text-align: center;
        font-size: 0.9em;
        color: #6c757d;
        border-top: 1px solid #ddd;
    }
    .footer a {
        color: #ff6600;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# --- Functions ---
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# --- App UI ---
st.title("🔐 Password Strength Meter")
st.markdown("Check how secure your password is and get suggestions to improve it.")

# Password input
password = st.text_input("Enter your password", type="password")

if password:
    blacklist = ["password", "123456", "qwerty", "admin", "password123"]
    if password.lower() in blacklist:
        st.error("❌ This is a commonly used password. Choose something more unique.")
    else:
        score, feedback = check_password_strength(password)

        # Strength level bar
        strength_colors = ["#dc3545", "#fd7e14", "#ffc107", "#28a745"]
        strength_labels = ["Weak", "Moderate", "Good", "Strong"]
        st.markdown(f"""
            <div class="password-meter" style="background-color: {strength_colors[score-1]}; width: {(score/4)*100}%;"></div>
            <p><b>Strength:</b> {strength_labels[score-1]}</p>
        """, unsafe_allow_html=True)

        # Feedback
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider improving it.")
            for f in feedback:
                st.write(f)
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
            for f in feedback:
                st.write(f)

    st.markdown("---")
    st.write("Need help? Click below to generate a strong password:")

    if st.button("🔄 Generate Strong Password"):
        strong_password = generate_strong_password()
        st.code(strong_password, language="text")

# --- Footer ---
st.markdown("""
<div class="footer">
    🔐 Built by <b>Mehwish Naz</b> ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a> |
    <a href="https://github.com/mehwishnaz1603/" target="_blank">GitHub Repo</a><br>
    © 2025 Password Strength Meter
</div>
""", unsafe_allow_html=True)
