import streamlit as st
import requests
# App Title
st.title("🎉 JUPITER Airdrop Checker 🎉")
st.markdown("Enter your wallet address to check if you're eligible for an airdrop.")

# User Input for Wallet Address
wallet_address = st.text_input("Enter Your SOLANA Wallet Address")

def get_allocation(address):
    url = f"https://jupuary-api.jup.ag/claim-proof-2025/{address}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
 
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # Check if the response is successful
        if response.status_code == 200:
                data = response.json()
                amount = data.get('amount', None)
                amount = int(amount)/1000000
                return amount
        else:
            return None
            
    except Exception as e:
            return None

# Button to check eligibility
if st.button("Check Eligibility"):
    
    if len(wallet_address) == 44:
        # Check if the address is eligible for the airdroP
        with st.spinner("🔍 Checking eligibility..."):
            allocation = get_allocation(wallet_address)
            if allocation is not None:
                # Display the result
                st.success(f"🎉 Congratulations! You're eligible for {allocation} JUP tokens!")
                st.balloons()
            elif allocation is None:
                st.warning("❌ Sorry, you are not eligible for the airdrop.")
            else:
                st.warning("❌ Sorry, you are not eligible for the airdrop.")
    else:
        st.error("❌ Please enter a valid SOLANA wallet address.")
