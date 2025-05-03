import streamlit as st
from datetime import datetime
import time

# Custom CSS with modern banking UI
st.markdown(f"""
<style>
    /* Main container with clean banking UI */
    .stApp {{
        background-color: #f5f7fa;
        font-family: 'Inter', sans-serif;
    }}
    
    /* Card styling */
    .bank-card {{
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}
    
    /* Balance display */
    .balance-display {{
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        margin: 0.5rem 0;
    }}
    
    /* Transaction items */
    .transaction-item {{
        padding: 12px 16px;
        margin: 8px 0;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.9);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    
    /* Colors for transaction types */
    .deposit {{ color: #38a169; }}
    .withdrawal {{ color: #e53e3e; }}
    
    /* Button styling */
    .stButton>button {{
        border-radius: 12px;
        padding: 12px 24px;
        background: #4f46e5;
        color: white;
        border: none;
        font-weight: 600;
    }}
    
    /* Input fields */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input {{
        border-radius: 12px !important;
    }}
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
        st.markdown('<div class="bank-card">', unsafe_allow_html=True)
        st.subheader("Create New Account")
        holder = st.text_input("Account Holder Name")
        number = st.number_input("Account Number", min_value=1000, step=1)
        initial = st.number_input("Initial Deposit", min_value=0.0, value=100.0)
        
        if st.button("Create Account"):
            if number not in st.session_state.accounts:
                st.session_state.accounts[number] = BankAccount(holder, number, initial)
                st.success(f"Account created for {holder}!")
            else:
                st.error("Account number already exists!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Account Selection
    if st.session_state.accounts:
        acc_number = st.sidebar.selectbox(
            "Select Account", 
            list(st.session_state.accounts.keys())
        )
        st.session_state.current_account = st.session_state.accounts[acc_number]
        
        # Deposit
        if operation == "Deposit":
            st.markdown('<div class="bank-card">', unsafe_allow_html=True)
            st.subheader("Make Deposit")
            amount = st.number_input("Amount to deposit", min_value=0.01)
            if st.button("Deposit"):
                if st.session_state.current_account.deposit(amount):
                    st.success(f"Deposited ${amount:.2f} successfully!")
                    time.sleep(0.5)
                    st.experimental_rerun()
                else:
                    st.error("Invalid deposit amount")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Withdraw
        elif operation == "Withdraw":
            st.markdown('<div class="bank-card">', unsafe_allow_html=True)
            st.subheader("Make Withdrawal")
            amount = st.number_input("Amount to withdraw", min_value=0.01)
            if st.button("Withdraw"):
                if st.session_state.current_account.withdraw(amount):
                    st.success(f"Withdrew ${amount:.2f} successfully!")
                    time.sleep(0.5)
                    st.experimental_rerun()
                else:
                    st.error("Invalid withdrawal amount or insufficient funds")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # View Account
        elif operation == "View Account":
            st.markdown('<div class="bank-card">', unsafe_allow_html=True)
            st.subheader("Account Details")
            st.markdown(f'<div class="balance-display">${st.session_state.current_account.balance:.2f}</div>', unsafe_allow_html=True)
            st.write(f"Account Holder: {st.session_state.current_account.account_holder}")
            st.write(f"Account Number: {st.session_state.current_account.account_number}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="bank-card">', unsafe_allow_html=True)
            st.subheader("Transaction History")
            if st.session_state.current_account.transactions:
                for date, desc, amt in st.session_state.current_account.transactions:
                    transaction_class = "deposit" if desc == "Deposit" else "withdrawal"
                    st.markdown(f"""
                    <div class="transaction-item">
                        <div>{date.strftime('%Y-%m-%d %H:%M')}</div>
                        <div class="{transaction_class}">{desc}: ${amt:.2f}</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("No transactions yet")
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
