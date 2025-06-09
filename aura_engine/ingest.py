import os
import praw
import pandas as pd
from dotenv import load_dotenv

def get_reddit_instance():
    """
    Loads API credentials from .env and creates a PRAW instance.
    """
    # Load environment variables from the .env file
    load_dotenv()

    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")
    username = os.getenv("REDDIT_USERNAME")
    password = os.getenv("REDDIT_PASSWORD")

    # Check if all credentials are present
    if not all([client_id, client_secret, user_agent, username, password]):
        raise ValueError("Missing Reddit API credentials in .env file.")

    # Create and return the PRAW instance
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password,
    )
    print(f"✅ Successfully authenticated as Reddit user: {reddit.user.me()}")
    return reddit

def fetch_subreddit_posts(subreddit_name: str, limit: int = 25):
    """
    Fetches the latest posts from a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit (e.g., 'apple').
        limit (int): The maximum number of posts to fetch.

    Returns:
        pandas.DataFrame: A DataFrame containing post data.
    """
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)

    print(f"🔥 Fetching latest {limit} posts from r/{subreddit_name}...")

    posts_data = []
    for post in subreddit.hot(limit=limit):
        # We collect the title and the main text body (selftext)
        posts_data.append({
            'id': post.id,
            'title': post.title,
            'text': post.selftext,
            'score': post.score,
            'url': post.url,
            'created_utc': post.created_utc
        })
    
    # Convert list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(posts_data)
    print(f"✅ Fetched {len(df)} posts successfully.")
    return df

if __name__ == '__main__':
    apple_posts_df = fetch_subreddit_posts('apple', limit=10)
    
    print("\n--- Latest 10 Post Titles from r/apple ---")
    for index, row in apple_posts_df.iterrows():
        print(f"- {row['title']}")