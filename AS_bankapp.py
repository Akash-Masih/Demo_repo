import streamlit as st
from datetime import datetime
import time

# Custom CSS with modern banking UI
st.markdown(f"""
<style>
    /* Main container with AI background */
    .stApp {{
        background: linear-gradient(rgba(0, 5, 15, 0.85), 
                    url('https://images.unsplash.com/photo-1620712943543-bcc4688e7485?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}
    
    /* Modern card styling */
    .modern-card {{
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 24px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.36);
        margin-bottom: 24px;
        transition: all 0.3s ease;
    }}
    
    .modern-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5);
    }}
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Inter', sans-serif;
        font-weight: 600;
    }}
    
    /* Balance display */
    .balance-display {{
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00d4ff 0%, #6a11cb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 16px 0;
        animation: pulse 2.5s infinite;
    }}
    
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.03); }}
        100% {{ transform: scale(1); }}
    }}
    
    /* Transaction items */
    .transaction-item {{
        padding: 12px 16px;
        margin: 8px 0;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.08);
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.2s ease;
    }}
    
    .transaction-item:hover {{
        background: rgba(255, 255, 255, 0.15);
    }}
    
    /* Category colors */
    .food {{ color: #FF9A8B; }}
    .shopping {{ color: #FFD166; }}
    .income {{ color: #06D6A0; }}
    
    /* Navigation */
    .nav-item {{
        padding: 12px 16px;
        border-radius: 12px;
        margin: 4px 0;
        cursor: pointer;
        transition: all 0.2s ease;
    }}
    
    .nav-item:hover {{
        background: rgba(255, 255, 255, 0.1);
    }}
    
    /* Button styling */
    .stButton>button {{
        border-radius: 12px;
        padding: 12px 24px;
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(106, 17, 203, 0.3);
    }}
</style>
""", unsafe_allow_html=True)

# Main App
def main():
    # Header with AI-themed greeting
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    with col2:
        st.title("Hi, Olivia!")
        st.caption("Your AI Banking Assistant")
    
    # Balance Overview
    st.markdown("""
    <div class="modern-card">
        <h3>SATISFACTION BALANCE</h3>
        <div class="balance-display">$1,561.50</div>
        <div style="display: flex; justify-content: space-between;">
            <div>ACTIVITIES</div>
            <div>$961.50</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="nav-item">💳 My Cards</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="nav-item">📈 Investing</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="nav-item">⚙ Settings</div>', unsafe_allow_html=True)
    
    # Transactions Section
    st.markdown("""
    <div class="modern-card">
        <h3>Recent Activities</h3>
        <div class="transaction-item">
            <div><span class="food">Food & Beverage</span></div>
            <div>+$28.11</div>
        </div>
        <div class="transaction-item">
            <div><span class="shopping">Shopping</span></div>
            <div>+$157.40</div>
        </div>
        <div class="transaction-item">
            <div><span class="income">Salary Income</span></div>
            <div>+$3,800.60</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Investment Tips
    st.markdown("""
    <div class="modern-card">
        <h3>Investing Tips</h3>
        <div class="transaction-item">
            <div>What is an ETF?</div>
            <div>💡</div>
        </div>
        <div class="transaction-item">
            <div>My Portfolio</div>
            <div>📊</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Assistant Prompt
    st.markdown("""
    <div class="modern-card">
        <h4>AI Assistant Suggestion</h4>
        <p>You forgot to log about $12.50 for pizza last night. Add it now?</p>
        <button class="stButton">Add Transaction</button>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
