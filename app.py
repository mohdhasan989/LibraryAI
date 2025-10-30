from flask import Flask, render_template, request, redirect
from database.db_connection import get_db
from models.recommender import recommend_books
import pandas as pd

app = Flask(__name__)
db = get_db()

@app.route('/')
def home():
    books = list(db.books.find({}, {'_id': 0}))
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    data = {k: v for k, v in request.form.items()}
    db.books.insert_one(data)
    return redirect('/')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        title = request.form.get('title')
        print("🔍 User entered title:", title)

        try:
            # 🔹 Load books from MongoDB
            books_data = list(db.books.find({}, {'_id': 0}))
            if not books_data:
                return render_template('recommend.html', message="No books found in database.")

            books_df = pd.DataFrame(books_data)

            # 🔹 Call the ML model
            recs = recommend_books(title, books_df)
            print("Recommendations:", recs)

            if not recs:
                message = f"No recommendations found for '{title}'. Please check spelling."
                return render_template('recommend.html', title=title, message=message)

            return render_template('recommend.html', title=title, recs=recs)

        except Exception as e:
            print("Error in recommendation:", e)
            return render_template('recommend.html', error=str(e))

    return render_template('recommend.html')


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
