import streamlit as st
import re
import time
from streamlit_lottie import st_lottie
import requests
import json
import random

# Set page configuration
st.set_page_config(
    page_title="Cosmic Password Strength",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&display=swap');
        
        .main {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: white;
        }
        
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif;
            color: #00ffff;
            text-shadow: 0 0 10px rgba(0, 255, 255, 0.7);
        }
        
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border: 2px solid #00ffff;
            border-radius: 10px;
            padding: 15px;
            font-size: 18px;
        }
        
        .stTextInput > div > div > input:focus {
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.7);
        }
        
        .password-card {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
        }
        
        .criteria-met {
            color: #00ff00;
            font-weight: bold;
        }
        
        .criteria-not-met {
            color: #ff3366;
            font-weight: bold;
        }
        
        .strength-meter {
            height: 20px;
            border-radius: 10px;
            margin: 20px 0;
            position: relative;
            overflow: hidden;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .strength-meter-fill {
            height: 100%;
            border-radius: 10px;
            transition: width 0.5s ease-in-out;
        }
        
        .weak-fill {
            background: linear-gradient(90deg, #ff3366, #ff0066);
            box-shadow: 0 0 10px rgba(255, 51, 102, 0.7);
        }
        
        .moderate-fill {
            background: linear-gradient(90deg, #ffcc33, #ff9900);
            box-shadow: 0 0 10px rgba(255, 204, 51, 0.7);
        }
        
        .strong-fill {
            background: linear-gradient(90deg, #33ff99, #00cc66);
            box-shadow: 0 0 10px rgba(51, 255, 153, 0.7);
        }
        
        .cosmic-button {
            background: linear-gradient(90deg, #00ffff, #00ccff);
            color: #000033;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 20px;
            text-align: center;
        }
        
        .cosmic-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.8);
        }
        
        .stExpander {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: rgba(255, 255, 255, 0.6);
        }
        
        .star {
            position: fixed;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
        }
        
        @keyframes rocket-animation {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }
        
        .rocket {
            animation: rocket-animation 2s infinite ease-in-out;
            display: inline-block;
            font-size: 30px;
            margin-right: 10px;
        }
        
        .planet {
            display: inline-block;
            margin: 0 5px;
            font-size: 24px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Add stars to the background
    stars_script = """
    <script>
    function createStars() {
        const mainElement = document.querySelector('.main');
        for (let i = 0; i < 100; i++) {
            const star = document.createElement('div');
            star.classList.add('star');
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.opacity = Math.random();
            star.style.width = `${Math.random() * 3}px`;
            star.style.height = star.style.width;
            mainElement.appendChild(star);
        }
    }
    
    // Run after the page loads
    window.addEventListener('load', createStars);
    </script>
    """
    st.markdown(stars_script, unsafe_allow_html=True)

# Load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Apply custom CSS
local_css()

# Create columns for layout
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # App title with space theme
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <span class="rocket">🚀</span>
        <h1>COSMIC PASSWORD STRENGTH</h1>
        <div>
            <span class="planet">🪐</span>
            <span class="planet">🌎</span>
            <span class="planet">🌕</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="password-card">
        <p style="text-align: center; font-size: 18px;">
            Enter your password below to test its cosmic strength. 
            The stronger your password, the further your security will travel into the universe!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Load space-themed animations
    lottie_space = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_XiFKBm.json")
    lottie_rocket = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qdcw41qh.json")
    lottie_security = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_q77jpyct.json")
    
    # Display a space animation
    if lottie_space:
        with st.container():
            st_lottie(lottie_space, height=200, key="space")
    
    # Password input with custom styling
    st.markdown('<div class="password-card">', unsafe_allow_html=True)
    password = st.text_input("🔑 Enter your password", type="password")
    st.markdown('</div>', unsafe_allow_html=True)

    # Function to check password strength
    def check_password_strength(password):
        score = 0
        feedback = []
        
        # Check length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Your password needs to be at least 8 characters to begin its cosmic journey")
        
        # Check for uppercase letters
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Add uppercase letters to fuel your password's rocket")
        
        # Check for lowercase letters
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Include lowercase letters to stabilize your password's orbit")
        
        # Check for digits
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Numbers will help your password navigate through the digital cosmos")
        
        # Check for special characters
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|]', password):
            score += 1
        else:
            feedback.append("Special characters act as shields against cosmic hackers")
        
        return score, feedback

    # Check button with animation
    if password:
        score, feedback = check_password_strength(password)
        
        # Display score with cosmic theme
        st.markdown('<div class="password-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>COSMIC SECURITY LEVEL</h2>", unsafe_allow_html=True)
        
        # Create a custom strength meter
        if score <= 2:
            strength_category = "VULNERABLE"
            color_class = "weak-fill"
            emoji = "☄️"  # Meteor (danger)
            description = "Your password is vulnerable to alien attacks!"
        elif score <= 4:
            strength_category = "ORBITAL"
            color_class = "moderate-fill"
            emoji = "🛰️"  # Satellite (moderate)
            description = "Your password is in orbit, but not yet reaching the stars."
        else:
            strength_category = "INTERSTELLAR"
            color_class = "strong-fill"
            emoji = "✨"  # Stars (strong)
            description = "Your password has achieved interstellar strength!"
        
        # Display the custom strength meter
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <h3>{emoji} {strength_category} {emoji}</h3>
            <p>{description}</p>
        </div>
        <div class="strength-meter">
            <div class="strength-meter-fill {color_class}" style="width: {score * 20}%;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: -15px;">
            <span>Vulnerable</span>
            <span>Orbital</span>
            <span>Interstellar</span>
        </div>
        <div style="text-align: center; margin-top: 10px;">
            <span style="font-size: 24px; font-weight: bold;">{score}/5</span> cosmic criteria met
        </div>
        """, unsafe_allow_html=True)
        
        # Display rocket animation for strong passwords
        if score == 5 and lottie_rocket:
            st_lottie(lottie_rocket, height=150, key="rocket")
        
        # Display security animation for weak passwords
        if score <= 2 and lottie_security:
            st_lottie(lottie_security, height=150, key="security")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display criteria checklist with space theme
        st.markdown('<div class="password-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>COSMIC CRITERIA</h2>", unsafe_allow_html=True)
        
        criteria = {
            "🔢 Minimum 8 characters": len(password) >= 8,
            "🔠 Uppercase letters": bool(re.search(r'[A-Z]', password)),
            "🔡 Lowercase letters": bool(re.search(r'[a-z]', password)),
            "🔢 Numeric digits": bool(re.search(r'\d', password)),
            "⚡ Special characters": bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|]', password))
        }
        
        for criterion, is_met in criteria.items():
            if is_met:
                st.markdown(f"<div class='criteria-met'>✅ {criterion} - SECURED</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='criteria-not-met'>❌ {criterion} - VULNERABLE</div>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display feedback with cosmic theme
        if feedback:
            st.markdown('<div class="password-card">', unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>MISSION CONTROL FEEDBACK</h2>", unsafe_allow_html=True)
            
            for suggestion in feedback:
                st.markdown(f"<div style='margin: 10px 0; padding: 10px; background: rgba(255, 51, 102, 0.2); border-radius: 10px; border-left: 4px solid #ff3366;'>🛸 {suggestion}</div>", unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Display success message for strong passwords
        if score == 5:
            st.markdown('<div class="password-card" style="background: rgba(51, 255, 153, 0.2);">', unsafe_allow_html=True)
            st.markdown("""
            <div style='text-align: center;'>
                <h2 style='color: #33ff99;'>MISSION ACCOMPLISHED! 🚀</h2>
                <p style='font-size: 18px;'>Your password has achieved interstellar strength and is ready to protect your digital universe!</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Add information about password security with space theme
    with st.expander("🌌 WHY COSMIC PASSWORDS MATTER"):
        st.markdown("""
        <div style='padding: 10px;'>
            <h3>The Universe of Digital Security</h3>
            <p>In the vast digital cosmos, your password is the shield protecting your personal galaxy from invaders.</p>
            
            <h4>Cosmic Threats Your Strong Password Defends Against:</h4>
            <ul>
                <li>🕳️ <b>Black Hole Attacks</b> (Brute Force) - Hackers trying every possible combination</li>
                <li>📚 <b>Nebula Attacks</b> (Dictionary Attacks) - Using common words to crack your password</li>
                <li>👽 <b>Alien Infiltration</b> (Credential Stuffing) - Using leaked passwords from other sites</li>
            </ul>
            
            <h4>Password Galaxy Best Practices:</h4>
            <ul>
                <li>🌠 Use a unique password for each account</li>
                <li>🛸 Consider using a password manager</li>
                <li>🔄 Change your passwords periodically</li>
                <li>🌌 The longer and more complex, the better</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Generate a random password button
    st.markdown('<div class="password-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>NEED A COSMIC PASSWORD?</h3>", unsafe_allow_html=True)
    
    if st.button("Generate Interstellar Password", key="generate"):
        # Generate a strong random password
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
        length = random.randint(12, 16)
        random_password = ''.join(random.choice(chars) for _ in range(length))
        
        st.markdown(f"""
        <div style='background: rgba(0, 255, 255, 0.1); padding: 15px; border-radius: 10px; margin-top: 10px; text-align: center;'>
            <p style='font-family: monospace; font-size: 18px; word-break: break-all;'>{random_password}</p>
            <p style='font-size: 14px;'>Copy this password and keep it safe in your cosmic vault!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>🚀 COSMIC PASSWORD STRENGTH CHECKER v1.0 🚀</p>
        <p>Protecting your digital universe, one password at a time.</p>
    </div>
    """, unsafe_allow_html=True)

# Add a fun easter egg
if password == "ilovespace":
    st.balloons()