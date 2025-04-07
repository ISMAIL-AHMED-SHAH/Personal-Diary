import streamlit as st
from datetime import datetime
import os

# --- Page Config ---
st.set_page_config(page_title="📓 My Diary", layout="centered")

st.image("diary4-bg.png", use_container_width=True)
# --- CSS Styling ---
st.markdown("""
    <style>
        .stApp {

            color: white;
        }
        .entry-box {
            border: 1px solid #555;
            border-radius: 10px;
            padding: 15px;
            background-color: #2E2E2E;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("📓 My Personal Diary")
st.markdown("Write your thoughts. Reflect. Grow. ✨")

# --- User Input ---
diary_entry = st.text_area("📝 Enter today’s diary entry")

# --- Save Entry Button ---
if st.button("💾 Save Entry"):
    if diary_entry.strip() != "":
        now = datetime.now()

        # ✅ Create directory if it doesn't exist
        if not os.path.exists("diary_entries"):
            os.makedirs("diary_entries")

        # ✅ Save entry in the folder
        filename = f"diary_entries/{now.date()}.txt"
        timestamp = now.strftime("[%Y-%m-%d %H:%M]")

        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{timestamp}\n{diary_entry}\n{'-'*40}\n")

        st.success("✅ Your thoughts have been saved successfully!")
    else:
        st.warning("Please write something before saving.")


# --- Read Previous Entries ---
if st.checkbox("📚 Show Previous Entries"):
    now = datetime.now()
    filename = f"diary_entries/{now.date()}.txt"

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        entries = [lines[i:i+3] for i in range(0, len(lines), 3)]
        last_entries = entries[-10:]

        st.subheader("📖 Last Entries")
        for e in last_entries:
            st.markdown("<div class='entry-box'>" + "".join(e).replace("\n", "<br>") + "</div><br>", unsafe_allow_html=True)
    else:
        st.info("No previous entries found for today.")



st.sidebar.image("diary3.png")
st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Search Diary by Date")
search_date = st.sidebar.date_input("Select a date")
search_btn = st.sidebar.button("📖 Show Entry")

if search_btn:
    filename = f"diary_entries/{search_date}.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        st.sidebar.success(f"Entry for {search_date}:")
        st.sidebar.text_area("🗒️ Entry Preview", content, height=250)
    else:
        st.sidebar.warning("No entry found for this date.")



st.sidebar.markdown("---")
# --- Sidebar ---
st.sidebar.markdown("## 💡 Diary Tip")
st.sidebar.write("Journaling helps organize thoughts, reduce stress, and boost mindfulness. Try it daily! 🧘‍♂️")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")

st.sidebar.markdown("---")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png", width=90, use_container_width=True)
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Built with ❤️ by Ismail Ahmed Shah</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
