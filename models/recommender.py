import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

def recommend_books(title, books):
    # Convert MongoDB data to DataFrame
    df = pd.DataFrame(books)

    if 'title' not in df.columns:
        raise ValueError("Books must have a 'title' field.")

    # Create TF-IDF matrix from book titles
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['title'])

    # Try to find closest match to user input
    all_titles = df['title'].tolist()
    match = get_close_matches(title, all_titles, n=1, cutoff=0.6)

    if not match:
        return []  # No close match found

    matched_title = match[0]

    # Get index of matched title
    idx = df.index[df['title'] == matched_title][0]

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Get top 5 similar book indexes (excluding the book itself)
    similar_indices = cosine_sim.argsort()[-6:-1][::-1]

    # Return recommended titles
    recommendations = df.iloc[similar_indices]['title'].tolist()

    return recommendations
