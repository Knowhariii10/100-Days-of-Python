import streamlit as st

st.set_page_config(page_title="Silent Auction 🏷️", layout="centered")

# ---------------- HEADER ----------------
st.title("🏷️ Silent Auction")
st.caption("Submit your bid privately. Highest bid wins.")
st.divider()

# ---------------- SESSION STATE INIT ----------------
if "bids" not in st.session_state:
    st.session_state.bids = {}

if "auction_closed" not in st.session_state:
    st.session_state.auction_closed = False

if "bid_amount" not in st.session_state:
    st.session_state.bid_amount = 0.0

if "name" not in st.session_state:
    st.session_state.name = ""

# ---------------- CALLBACK FUNCTION ----------------
def submit_bid():
    if st.session_state.name.strip() == "":
        st.warning("Name cannot be empty.")
        return

    st.session_state.bids[st.session_state.name] = st.session_state.bid_amount
    st.success("✅ Bid submitted successfully.")
    st.info("🔒 Your bid is hidden until the auction ends.")

    # ✅ SAFE RESET (THIS IS THE KEY FIX)
    st.session_state.bid_amount = 0.0
    st.session_state.name = ""

# ---------------- BID SUBMISSION ----------------
if not st.session_state.auction_closed:
    st.text_input("👤 Your Name", key="name")

    st.number_input(
        "💰 Your Bid Amount ($)",
        min_value=0.0,
        step=10.0,
        key="bid_amount"
    )

    st.button("📥 Submit Bid", on_click=submit_bid)

    st.divider()
    st.warning("🚫 No bids are visible during the auction.")

    if st.button("🏁 Close Auction"):
        if len(st.session_state.bids) == 0:
            st.warning("No bids placed yet.")
        else:
            st.session_state.auction_closed = True

# ---------------- RESULT REVEAL ----------------
if st.session_state.auction_closed:
    st.subheader("📢 Auction Closed")

    highest_bid = 0
    winner = ""

    for bidder, amount in st.session_state.bids.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder

    st.success(f"🏆 Winner: **{winner}**")
    st.info(f"💵 Winning Bid: **${highest_bid}**")

    st.divider()

    if st.button("🔁 Start New Auction"):
        st.session_state.bids = {}
        st.session_state.auction_closed = False
        st.session_state.bid_amount = 0.0
        st.session_state.name = ""

st.caption("Built with Python & Streamlit | Day 10 of #100DaysOfCode")
