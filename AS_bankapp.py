import streamlit as st
from datetime import datetime
import time

# Custom CSS with animations and glassmorphism design
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Card styling - Glassmorphism effect */
    .card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5);
    }
    
    /* Button styling */
    .stButton>button {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: scale(1.05);
    }
    
    /* Input fields */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border-radius: 12px !important;
    }
    
    /* Radio buttons */
    .stRadio>div {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 10px;
    }
    
    /* Pulse animation for balance */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .balance-display {
        animation: pulse 2s infinite;
        font-size: 2.5rem !important;
        font-weight: bold;
        color: white;
        text-align: center;
        margin: 20px 0;
    }
    
    /* Transaction animation */
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .transaction {
        animation: slideIn 0.5s ease forwards;
        opacity: 0;
    }
</style>
""", unsafe_allow_html=True)

class BankAccount:
    def __init__(self, holder: str, number: int, initial_balance: float):
        self.account_holder = holder
        self.account_number = number
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.now(), "Deposit", amount))
            return True
        return False
    
    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.now(), "Withdrawal", amount))
            return True
        return False
    
    def display(self):
        return f"""
        Account Holder: {self.account_holder}
        Account Number: {self.account_number}
        Current Balance: ${self.balance:.2f}
        """

def main():
    st.title("🏦 Akash's Banking App")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Initialize session state
    if 'accounts' not in st.session_state:
        st.session_state.accounts = {}
        st.session_state.current_account = None
    
    # Sidebar operations
    st.sidebar.header("Account Management")
    operation = st.sidebar.radio("Choose operation:", 
                               ["Create Account", "Deposit", "Withdraw", "View Account"])
    
    # Create Account
    if operation == "Create Account":
        st.subheader("Create New Account")
        holder = st.text_input("Account Holder Name")
        number = st.number_input("Account Number", min_value=1000, step=1)
        initial = st.number_input("Initial Deposit", min_value=0.0, value=100.0)
        
        if st.button("Create Account"):
            if number not in st.session_state.accounts:
                st.session_state.accounts[number] = BankAccount(holder, number, initial)
                st.success(f"Account created for {holder}!")
                st.balloons()
            else:
                st.error("Account number already exists!")
    
    # Account Selection
    if st.session_state.accounts:
        acc_number = st.sidebar.selectbox(
            "Select Account", 
            list(st.session_state.accounts.keys())
        )
        st.session_state.current_account = st.session_state.accounts[acc_number]
        
        # Deposit
        if operation == "Deposit":
            st.subheader("Make Deposit")
            amount = st.number_input("Amount to deposit", min_value=0.01)
            if st.button("Deposit"):
                if st.session_state.current_account.deposit(amount):
                    st.success(f"Deposited ${amount:.2f} successfully!")
                    time.sleep(0.5)
                    st.experimental_rerun()
                else:
                    st.error("Invalid deposit amount")
        
        # Withdraw
        elif operation == "Withdraw":
            st.subheader("Make Withdrawal")
            amount = st.number_input("Amount to withdraw", min_value=0.01)
            if st.button("Withdraw"):
                if st.session_state.current_account.withdraw(amount):
                    st.success(f"Withdrew ${amount:.2f} successfully!")
                    time.sleep(0.5)
                    st.experimental_rerun()
                else:
                    st.error("Invalid withdrawal amount or insufficient funds")
        
        # View Account
        elif operation == "View Account":
            st.subheader("Account Details")
            st.markdown(f'<div class="card"><h3>{st.session_state.current_account.account_holder}</h3>'
                       f'<p>Account #: {st.session_state.current_account.account_number}</p>'
                       f'<div class="balance-display">${st.session_state.current_account.balance:.2f}</div></div>', 
                       unsafe_allow_html=True)
            
            st.subheader("Transaction History")
            if st.session_state.current_account.transactions:
                for i, (date, desc, amt) in enumerate(st.session_state.current_account.transactions):
                    st.markdown(f"""
                    <div class="card transaction" style="animation-delay: {i*0.1}s">
                        <div style="display: flex; justify-content: space-between;">
                            <span>{date.strftime('%Y-%m-%d %H:%M')}</span>
                            <span style="font-weight: bold; color: {'#4CAF50' if desc == 'Deposit' else '#F44336'}">
                                {desc}: ${amt:.2f}
                            </span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown('<div class="card">No transactions yet</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
