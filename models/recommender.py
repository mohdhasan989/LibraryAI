import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

def load_books_data():
    # Load dataset safely
    df = pd.read_csv("models/Books.csv", encoding='latin-1', low_memory=False)
    
    # Drop rows missing Book-Title or Book-Author
    df = df.dropna(subset=['Book-Title', 'Book-Author'])
    
    # Fill other missing text fields just in case
    df['Book-Title'] = df['Book-Title'].fillna('')
    df['Book-Author'] = df['Book-Author'].fillna('')
    
    # Remove duplicates by title
    df = df.drop_duplicates(subset=['Book-Title'])
    
    return df


def recommend_books(title):
    df = load_books_data()
    
    # Combine features for text similarity
    df['features'] = df['Book-Title'] + " " + df['Book-Author']

    # Create TF-IDF matrix
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['features'])

    # Find closest title match
    all_titles = df['Book-Title'].tolist()
    match = get_close_matches(title, all_titles, n=1, cutoff=0.6)

    if not match:
        return ["❌ No similar book found. Try another title."]

    matched_title = match[0]
    idx = df.index[df['Book-Title'] == matched_title][0]

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Get top 5 similar books
    similar_indices = cosine_sim.argsort()[-6:-1][::-1]
    recommendations = df.iloc[similar_indices][['Book-Title', 'Book-Author']]

    return recommendations.to_dict(orient='records')


# 🔍 Run a quick test
if __name__ == "__main__":
    title = input("Enter a book you've read: ")
    results = recommend_books(title)

    print("\n📚 Recommended Books:\n")
    for r in results:
        print(f"{r['Book-Title']} by {r['Book-Author']}")
