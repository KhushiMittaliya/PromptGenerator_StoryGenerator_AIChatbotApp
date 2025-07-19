import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# Set page config
st.set_page_config(page_title="Prompt Generator App", layout="wide")

# Page title
st.title("💻 AI Prompt Generator & Chatbot")

# Sidebar menu
option = st.sidebar.radio(
    "Select a Generator:",
    ("💼 Business Idea Generator", "📚 Story Idea Generator", "🤖 ML Chatbot")
)

# ===================== A1: Business Idea Generator =====================
if option == "💼 Business Idea Generator":
    st.header("💼 Business Idea Generator")
    industry = st.text_input("Enter an industry (e.g. healthcare, finance, education):")
    audience = st.text_input("Target audience (e.g. students, elderly, remote workers):")
    trend = st.text_input("Mention a trend or tech (e.g. AI, sustainability, blockchain):")

    if st.button("Generate Business Idea"):
        if industry and audience and trend:
            st.success(f"A business idea for the {industry} industry targeting {audience}, using {trend}:")
            st.write(f"🧠 **AI-powered {industry} assistant for {audience}** that uses {trend} to offer personalized services and increase engagement.")
        else:
            st.warning("Please fill all the fields!")

    # 👉 Business Chart
    st.subheader("📊 Popular Industries Chosen")
    industries = ['Healthcare', 'Education', 'Finance', 'E-Commerce']
    counts = [10, 7, 4, 9]

    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_facecolor('#F5F5F5')
    ax.set_facecolor('#EAEAEA')
    bars = ax.barh(industries, counts, color="#4E79A7", edgecolor='black')
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.set_axisbelow(True)
    ax.set_xlabel("Number of Selections", fontsize=9)
    ax.set_ylabel("Industry", fontsize=9)
    ax.set_title("Top Selected Industries", fontsize=11, weight='bold')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)

# ===================== A2: Story Idea Generator =====================
elif option == "📚 Story Idea Generator":
    st.header("📚 Story Idea Generator")
    genre = st.selectbox("Choose a genre:", ["Sci-Fi", "Fantasy", "Mystery", "Romance"])
    character = st.text_input("Enter a main character type (e.g. hacker, orphan, detective):")
    plot = st.text_input("Enter a basic plot idea or theme:")

    if st.button("Generate Story Idea"):
        if genre and character and plot:
            st.success("Here’s your story idea:")
            st.write(f"A **{genre}** story featuring a **{character}** who navigates a world where {plot}.")
        else:
            st.warning("Please fill all the fields!")

    # 👉 Time-Series Prompt Generation Chart
    st.subheader("📈 Prompt Generation Trend")
    df = pd.DataFrame({
        "date": pd.date_range(start="2024-01-01", periods=10),
        "prompts_generated": [5, 10, 15, 13, 20, 18, 22, 24, 30, 28]
    })
    st.line_chart(df.set_index("date"))

# ===================== A3: ML Chatbot =====================
elif option == "🤖 ML Chatbot":
    st.header("🤖 Conversational ML Chatbot")
    st.write("Ask me anything about Machine Learning. You can ask up to 5 questions!")

    if 'count' not in st.session_state:
        st.session_state.count = 0

    user_input = st.text_input("👤 You:")

    def get_response(user_input):
        user_input = user_input.lower()
        if "what is machine learning" in user_input:
            return "Machine learning is a branch of AI where computers learn from data."
        elif "types of machine learning" in user_input:
            return "1. Supervised\n2. Unsupervised\n3. Reinforcement Learning"
        elif "example" in user_input and "supervised" in user_input:
            return "Example: Email spam detection with labeled data."
        elif "tools" in user_input:
            return "Python, Scikit-learn, TensorFlow, Pandas, NumPy, etc."
        elif "mistake" in user_input:
            return "Yes, ML models can make mistakes due to bad data or overfitting."
        else:
            return "I’m still learning. Try asking about types, tools, or fun facts!"

    if user_input and st.session_state.count < 5:
        response = get_response(user_input)
        st.session_state.count += 1
        st.write(f"🤖 {response}")
        st.write(f"(Questions used: {st.session_state.count}/5)")
    elif st.session_state.count >= 5:
        st.warning("You’ve reached the 5-question limit. Refresh to start again.")

    # 👉 Word Cloud for ML terms
    st.subheader("🧠 Most Common Tech Terms")
    text = "AI blockchain education health AI AI finance chatbot ML chatbot ML"
    wordcloud = WordCloud(background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
