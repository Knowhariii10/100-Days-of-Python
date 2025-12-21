import streamlit as st
import random

st.set_page_config(page_title="Hangman Game 🎯", layout="centered")

# ---------------- WORDS + HINTS ----------------
word_hints = {
    "python": "A popular programming language 🐍",
    "apple": "A red or green fruit 🍎",
    "train": "Used for travelling on tracks 🚆",
    "music": "You listen to it 🎵",
    "phone": "Used for calling and messaging 📱"
}

# ---------------- SESSION STATE ----------------
if "word" not in st.session_state:
    st.session_state.word = random.choice(list(word_hints.keys()))
    st.session_state.hint = word_hints[st.session_state.word]
    st.session_state.guessed = []
    st.session_state.lives = 6
    st.session_state.game_over = False

# ---------------- HEADER ----------------
st.title("🎯 Hangman Game")
st.caption("Guess the word before you run out of lives")
st.divider()

# ---------------- HINT (REVEAL AFTER 2 WRONG GUESSES) ----------------
if st.session_state.lives <= 4 and not st.session_state.game_over:
    st.info(f"💡 Hint: {st.session_state.hint}")

# ---------------- WORD DISPLAY ----------------
display_word = " ".join(
    [letter if letter in st.session_state.guessed else "_" 
     for letter in st.session_state.word]
)

st.markdown(
    f"<h2 style='text-align:center; letter-spacing:6px;'>{display_word}</h2>",
    unsafe_allow_html=True
)

# ---------------- LIVES DISPLAY ----------------
st.markdown(
    f"<h3 style='text-align:center;'>Lives: {'❤️ ' * st.session_state.lives}</h3>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- LETTER BUTTONS ----------------
st.subheader("Choose a letter")

alphabet = "abcdefghijklmnopqrstuvwxyz"
cols = st.columns(7)

for index, letter in enumerate(alphabet):
    with cols[index % 7]:
        if st.button(
            letter.upper(),
            disabled=letter in st.session_state.guessed or st.session_state.game_over
        ):
            st.session_state.guessed.append(letter)

            if letter not in st.session_state.word:
                st.session_state.lives -= 1

            # WIN CONDITION
            if all(l in st.session_state.guessed for l in st.session_state.word):
                st.session_state.game_over = True
                st.success("🎉 YOU WON! Great job!")

            # LOSE CONDITION
            if st.session_state.lives == 0:
                st.session_state.game_over = True
                st.error(f"💀 GAME OVER! The word was **{st.session_state.word}**")

# ---------------- PLAY AGAIN ----------------
if st.session_state.game_over:
    st.divider()
    if st.button("🔁 Play Again"):
        st.session_state.word = random.choice(list(word_hints.keys()))
        st.session_state.hint = word_hints[st.session_state.word]
        st.session_state.guessed = []
        st.session_state.lives = 6
        st.session_state.game_over = False

st.caption("🎮 Built with Python & Streamlit | Day 8 of #100DaysOfCode")
