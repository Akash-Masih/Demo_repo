import streamlit as st
from datetime import datetime

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

# Streamlit App
def main():
    st.title("🏦 Akash Banking App")
    
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
                else:
                    st.error("Invalid deposit amount")
        
        # Withdraw
        elif operation == "Withdraw":
            st.subheader("Make Withdrawal")
            amount = st.number_input("Amount to withdraw", min_value=0.01)
            if st.button("Withdraw"):
                if st.session_state.current_account.withdraw(amount):
                    st.success(f"Withdrew ${amount:.2f} successfully!")
                else:
                    st.error("Invalid withdrawal amount or insufficient funds")
        
        # View Account
        elif operation == "View Account":
            st.subheader("Account Details")
            st.text(st.session_state.current_account.display())
            
            st.subheader("Transaction History")
            if st.session_state.current_account.transactions:
                for date, desc, amt in st.session_state.current_account.transactions:
                    st.write(f"{date.strftime('%Y-%m-%d %H:%M')} | {desc} | ${amt:.2f}")
            else:
                st.write("No transactions yet")

if __name__ == "__main__":
    main()
