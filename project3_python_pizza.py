import streamlit as st

st.set_page_config(page_title="Python Pizza Deliveries")

st.title("🍕 Welcome to Python Pizza Deliveries!")

size = st.selectbox(
    "What size pizza do you want?",
    ["S", "M", "L", "XL"]
)

pepperoni = st.selectbox(
    "Do you want pepperoni?",
    ["Y", "N"]
)

cheese = st.selectbox(
    "Do you want extra cheese?",
    ["Y", "N"]
)

if st.button("🧾 Calculate Bill"):
    bill = 0

    # Base price
    if size == "S":
        bill = 15
        if pepperoni == "Y":
            bill += 2
    elif size == "M":
        bill = 20
        if pepperoni == "Y":
            bill += 2
    elif size == "L":
        bill = 25
        if pepperoni == "Y":
            bill += 3
    elif size == "XL":
        bill = 30
        if pepperoni == "Y":
            bill += 3

    # Extra cheese (same for all sizes)
    if cheese == "Y":
        bill += 1

    st.success(f"🍕 Your Final Bill is **${bill}**")
