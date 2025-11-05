from flask import Flask, render_template, request, redirect
from database.db_connection import get_db
from models.recommender import recommend_books
import pandas as pd
import requests

app = Flask(__name__)
db = get_db()

# ------------------ HOME PAGE ------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    # ✅ Replaced MongoDB with MySQL — everything else same
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT title, author, description FROM books;")
    books = cursor.fetchall()
    cursor.close()
    conn.close()

    author_books = []
    author = ''

    if request.method == 'POST':
        form_type = request.form.get('form_type', '')
        
        # Only run author search if this form is submitted
        if form_type == 'author_search':
            author = request.form.get('author', '').strip()
            if author:
                url = f'https://www.googleapis.com/books/v1/volumes?q=inauthor:{author}'
                response = requests.get(url)
                data = response.json()
                if 'items' in data:
                    for item in data['items'][:5]:
                        volume = item['volumeInfo']
                        author_books.append({
                            'title': volume.get('title', 'No title'),
                            'authors': ', '.join(volume.get('authors', [])),
                            'thumbnail': volume.get('imageLinks', {}).get('thumbnail', ''),
                            'previewLink': volume.get('previewLink', '#')
                        })

    return render_template('index.html', books=books, author_books=author_books, author=author)


# ------------------ ADD BOOK PAGE ------------------
@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title', '').strip()
    author = request.form.get('author', '').strip()
    description = request.form.get('description', '').strip()

    if title and author and description:
        conn = get_db()  # connect to MySQL (from db_connection.py)
        cursor = conn.cursor()

        # Insert into MySQL table
        sql = "INSERT INTO books (title, author, description) VALUES (%s, %s, %s)"
        cursor.execute(sql, (title, author, description))

        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/')


#-----------RECOMMENDATION--------------
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    recs = []
    title = ''
    message = ''

    if request.method == 'POST':
        title = request.form.get('title', '').strip()

        if title:
            results = recommend_books(title)
            if isinstance(results, list) and results:
                recs = results
            else:
                message = "⚠️ No recommendations found. Try another title!"
        else:
            message = "⚠️ Please enter a book title."

    return render_template('recommend.html', title=title, recs=recs, message=message)

# ------------------ AUTHOR BOOK SEARCH (ONLINE) ------------------
@app.route('/author_books', methods=['POST'])
def author_books_online():
    author = request.form.get('author', '').strip()
    author_books = []

    if author:
        # ✅ Get books from MySQL
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT title, author, description FROM books WHERE author LIKE %s;", (f"%{author}%",))
        all_books = cursor.fetchall()
        cursor.close()
        conn.close()

        # ✅ Optionally call Google Books API for extra data
        url = f'https://www.googleapis.com/books/v1/volumes?q=inauthor:{author}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            for item in data['items'][:5]:
                volume = item['volumeInfo']
                author_books.append({
                    'title': volume.get('title', 'No title'),
                    'authors': ', '.join(volume.get('authors', [])),
                    'thumbnail': volume.get('imageLinks', {}).get('thumbnail', ''),
                    'previewLink': volume.get('previewLink', '#')
                })

    return render_template('index.html', books=all_books, author_books=author_books, author=author)
#--------------binary_search-----------------
from algorithms.binary_search import binary_search


@app.route('/binary_search', methods=['GET', 'POST'])
def binary_search_books():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books ORDER BY title ASC")
    books = cursor.fetchall()

    result = None
    if request.method == 'POST':
        title = request.form.get('title')
        result = binary_search(books, title)

    cursor.close()
    db.close()
    return render_template('binary_search.html', books=books, result=result)




# ------------------ RUN APP ------------------
if __name__ == '__main__':
    app.run(debug=True, port=8000)

