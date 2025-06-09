# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Import our custom modules from the aura_engine package
from aura_engine.ingest import fetch_subreddit_posts
from aura_engine.analysis import analyze_sentiment

# --- Page Configuration ---
st.set_page_config(
    page_title="Aura: Real-Time Insight Engine",
    page_icon="💡",
    layout="wide"
)

# --- Caching Functions for Performance ---
# This tells Streamlit to store the results of these functions. If the inputs don't
# change, Streamlit provides the stored result instead of re-running the slow code.
# This makes the app much faster and reduces unnecessary API calls.

@st.cache_data(show_spinner=False) # We'll use our own spinner in the main logic
def cached_fetch_posts(subreddit, limit):
    """Cached version of the data ingestion function."""
    return fetch_subreddit_posts(subreddit, limit)

@st.cache_data(show_spinner=False)
def cached_analyze_sentiment(df):
    """Cached version of the sentiment analysis function."""
    return analyze_sentiment(df)


# --- App UI ---
st.title("💡 Aura: Real-Time Customer Insight Engine")
st.write("Enter a subreddit name to analyze the sentiment of its latest posts using a RoBERTa-based AI model.")

# --- Sidebar for Inputs ---
with st.sidebar:
    st.header("Analysis Configuration")
    subreddit_name = st.text_input("Subreddit Name (e.g., apple, GooglePixel)", value="apple")
    post_limit = st.slider("Number of Posts to Analyze", min_value=10, max_value=100, value=25, step=5)
    
    # The 'on_click' argument can be used to clear previous results if needed,
    # but for this app, letting the cache handle reruns is sufficient.
    analyze_button = st.button("Analyze Sentiment", type="primary", use_container_width=True)

# --- Main App Logic ---
if analyze_button:
    if not subreddit_name:
        st.warning("Please enter a subreddit name.")
    else:
        # Show a single, overarching spinner for the whole process
        with st.spinner(f"Fetching and analyzing latest {post_limit} posts from r/{subreddit_name}..."):
            try:
                # 1. Fetch data using the cached function
                posts_df = cached_fetch_posts(subreddit_name, post_limit)
                
                # 2. Analyze sentiment using the cached function
                analyzed_df = cached_analyze_sentiment(posts_df)
                
                st.success("Analysis complete!")

                # --- Display Results ---
                st.subheader("Sentiment Analysis Breakdown")

                # Create two columns for metrics and a pie chart
                col1, col2 = st.columns([1, 2])

                with col1:
                    # Calculate and display metrics
                    sentiment_counts = analyzed_df['sentiment_label'].value_counts()
                    st.metric("Total Posts Analyzed", len(analyzed_df))
                    # Use .get(label, 0) to avoid errors if a sentiment label is not present
                    st.metric("✅ Positive Posts", sentiment_counts.get('positive', 0))
                    st.metric("💬 Neutral Posts", sentiment_counts.get('neutral', 0))
                    st.metric("❌ Negative Posts", sentiment_counts.get('negative', 0))

                with col2:
                    # Display a pie chart
                    if not sentiment_counts.empty:
                        fig = px.pie(
                            sentiment_counts, 
                            values=sentiment_counts.values, 
                            names=sentiment_counts.index, 
                            title=f'Sentiment Distribution in r/{subreddit_name}',
                            color=sentiment_counts.index,
                            color_discrete_map={
                                'positive': '#28a745',  # A nice green
                                'neutral': '#ffc107',   # A nice amber
                                'negative': '#dc3545'   # A nice red
                            }
                        )
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.info("No sentiment data to display.")

                # Display the raw data in an expandable section
                with st.expander("View Detailed Post Analysis"):
                    # A more readable display of the results
                    st.dataframe(
                        analyzed_df[['title', 'sentiment_label', 'sentiment_score']],
                        use_container_width=True,
                        hide_index=True
                    )

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.exception(e) # This will print the full traceback for debugging

else:
    st.info("Click 'Analyze Sentiment' in the sidebar to begin.")