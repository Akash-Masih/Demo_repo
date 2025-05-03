import streamlit as st
from datetime import datetime

# Mock database
accounts = {
    "user1": {"password": "pass1", "balance": 1000, "transactions": []},
    "user2": {"password": "pass2", "balance": 2500, "transactions": []}
}

def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        if username in accounts and accounts[username]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

def bank_operations():
    st.title(f"🏦 Welcome, {st.session_state['username']}")
    account = accounts[st.session_state["username"]]
    
    # Balance display
    st.subheader(f"Current Balance: ${account['balance']}")
    
    # Operations
    operation = st.radio("Choose operation:", ["Deposit", "Withdraw"])
    amount = st.number_input("Amount", min_value=0.01, format="%.2f")
    
    if st.button("Submit"):
        if operation == "Deposit":
            account["balance"] += amount
            account["transactions"].append((datetime.now(), "Deposit", amount))
            st.success(f"Deposited ${amount:.2f}")
        else:
            if amount > account["balance"]:
                st.error("Insufficient funds!")
            else:
                account["balance"] -= amount
                account["transactions"].append((datetime.now(), "Withdrawal", amount))
                st.success(f"Withdrew ${amount:.2f}")
    
    # Transaction history
    st.subheader("Transaction History")
    for date, desc, amt in account["transactions"]:
        st.write(f"{date.strftime('%Y-%m-%d %H:%M')} | {desc} | ${amt:.2f}")

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    if not st.session_state["logged_in"]:
        login()
    else:
        bank_operations()
        
        if st.sidebar.button("Logout"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
