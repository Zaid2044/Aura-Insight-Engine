# Aura: Real-Time Customer Insight Engine

![Aura Dashboard Screenshot](docs/aura_screenshot.png)
_**Figure 1:** The Aura dashboard providing an at-a-glance sentiment analysis for the r/apple subreddit._

---

## 🚀 The Problem: Drowning in Customer Feedback

In today's digital world, brands are inundated with a constant stream of customer feedback on platforms like Reddit, Twitter/X, and news sites. This data is a goldmine for understanding customer needs, identifying product issues, and tracking marketing campaign effectiveness. However, the sheer volume and speed make it impossible for human teams to manually process and analyze it in a timely manner.

This project addresses the critical business need for **automated, real-time customer intelligence.**

## 💡 The Solution: An AI-Powered Insight Dashboard

Aura is a full-stack web application that acts as a central nervous system for brand monitoring. It leverages a state-of-the-art Natural Language Processing (NLP) pipeline to ingest, analyze, and visualize customer sentiment from any public subreddit.

This tool empowers product managers, marketing teams, and executives to move from guesswork to data-driven decision-making by answering key questions instantly:
*   What is the overall sentiment surrounding our brand right now?
*   Are there more positive or negative conversations happening?
*   What are the specific posts driving these sentiments?

### Key Features:
*   **Dynamic Data Ingestion:** Connects directly to the Reddit API using **PRAW** to fetch the latest posts from any specified subreddit.
*   **State-of-the-Art Sentiment Analysis:** Utilizes the `cardiffnlp/twitter-roberta-base-sentiment-latest` model via the **Hugging Face `transformers`** library to accurately classify post sentiment as Positive, Negative, or Neutral.
*   **Robust Text Processing:** The pipeline is built to handle real-world data, automatically truncating oversized posts to prevent model errors.
*   **Interactive Web Dashboard:** A user-friendly frontend built with **Streamlit** allows for easy configuration and visualization of the results.
*   **Insightful Visualizations:** Leverages **Plotly Express** to create clear, interactive pie charts and metrics that summarize the sentiment landscape at a glance.

---

## 🛠️ Technology Stack

*   **Core Language:** Python 3.12
*   **Data Ingestion:** PRAW (The Python Reddit API Wrapper)
*   **AI / NLP:** Hugging Face `transformers`, PyTorch
*   **Data Handling:** Pandas
*   **Web Dashboard & Visualization:** Streamlit, Plotly Express
*   **Configuration:** python-dotenv

---

## 🏁 Getting Started

### Prerequisites
*   Python 3.12 or higher
*   Git
*   Reddit API Credentials (see instructions below)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Zaid2044/Aura-Insight-Engine.git
    cd Aura-Insight-Engine
    ```

2.  **Set up Reddit API Credentials:**
    *   Create a script-type application at [Reddit Apps](https://www.reddit.com/prefs/apps).
    *   Create a `.env` file in the project root.
    *   Add your credentials to the `.env` file:
        ```
        REDDIT_CLIENT_ID="YOUR_CLIENT_ID"
        REDDIT_CLIENT_SECRET="YOUR_SECRET"
        REDDIT_USER_AGENT="Aura Insight Engine v0.1 by u/your_username"
        REDDIT_USERNAME="your_username"
        REDDIT_PASSWORD="your_password"
        ```

3.  **Create and activate a virtual environment:**
    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate
    ```

4.  **Install the required dependencies:**
    ```bash
    python -m pip install -r requirements.txt
    ```

### Running the Application
1.  **Launch the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
2.  Your browser will automatically open to the Aura dashboard.
3.  Enter a subreddit name, choose the number of posts, and click "Analyze Sentiment".