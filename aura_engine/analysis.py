# aura_engine/analysis.py

from transformers import pipeline
import pandas as pd

# --- Constants --
SENTIMENT_MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

def analyze_sentiment(df: pd.DataFrame):
    """
    Analyzes the sentiment of posts in a DataFrame using a pre-trained AI model.

    Args:
        df (pd.DataFrame): DataFrame containing a 'title' and 'text' column.

    Returns:
        pd.DataFrame: The original DataFrame with added 'sentiment_label' and 'sentiment_score' columns.
    """
    print("🤖 Initializing AI Sentiment Analysis pipeline...")

    sentiment_pipeline = pipeline(
        "sentiment-analysis", 
        model=SENTIMENT_MODEL_NAME,
        truncation=True,
        max_length=512    )
    print("✅ AI Pipeline ready.")

    texts_to_analyze = (df['title'] + ". " + df['text'].fillna('')).tolist()

    print(f"🧠 Analyzing sentiment for {len(texts_to_analyze)} posts...")
    
    sentiments = sentiment_pipeline(texts_to_analyze)

    # Extract just the label (e.g., 'Positive') and the score from the results
    df['sentiment_label'] = [s['label'] for s in sentiments]
    df['sentiment_score'] = [s['score'] for s in sentiments]

    print("✅ Sentiment analysis complete.")
    return df

# This block allows us to test this script directly
if __name__ == '__main__':
    from .ingest import fetch_subreddit_posts

    # 1. Fetch the data
    test_df = fetch_subreddit_posts('apple', limit=5)

    # 2. Analyze the data
    analyzed_df = analyze_sentiment(test_df)

    print("\n--- Sentiment Analysis Results ---")
    # Display the relevant columns of the resulting DataFrame
    print(analyzed_df[['title', 'sentiment_label', 'sentiment_score']])