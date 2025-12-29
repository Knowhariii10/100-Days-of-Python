import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game 🎯", layout="centered")

# ---------------- SESSION STATE ----------------
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 0
    st.session_state.game_over = False

# ---------------- UI ----------------
st.title("🎯 Number Guessing Game")
st.caption("Guess the number between 1 and 100")
st.divider()

# ---------------- DIFFICULTY ----------------
difficulty = st.radio(
    "Choose Difficulty",
    ("Easy (10 attempts)", "Hard (5 attempts)")
)

if st.button("🎮 Start Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.max_attempts = 10 if "Easy" in difficulty else 5

# ---------------- GAME LOGIC ----------------
if st.session_state.max_attempts > 0 and not st.session_state.game_over:

    guess = st.number_input(
        "Make a guess",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("✅ Submit Guess"):
        st.session_state.attempts += 1

        if guess == st.session_state.number:
            st.success("🎉 Correct! You guessed the number!")
            st.session_state.game_over = True

        elif guess > st.session_state.number:
            st.warning("📉 Too high! Guess lower.")

        else:
            st.warning("📈 Too low! Guess higher.")

        remaining = st.session_state.max_attempts - st.session_state.attempts
        st.info(f"Attempts remaining: {remaining}")

        if remaining == 0 and not st.session_state.game_over:
            st.error(f"❌ Game Over! The number was {st.session_state.number}")
            st.session_state.game_over = True

# ---------------- RESET ----------------
if st.session_state.game_over:
    if st.button("🔁 Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.max_attempts = 0
        st.session_state.game_over = False

st.caption("Built with Python & Streamlit | Day 13 of #100DaysOfCode")
