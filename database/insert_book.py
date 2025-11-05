from db_connection import get_db

# Get the database connection
db = get_db()
cursor = db.cursor()

# Books data
books_data = [
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling",
     "A young boy discovers he is a wizard and attends Hogwarts School of Witchcraft and Wizardry, where he faces magical adventures and dark secrets."),
    ("The Hobbit", "J.R.R. Tolkien",
     "Bilbo Baggins, a humble hobbit, is pulled into a thrilling adventure to reclaim a lost dwarf kingdom from a fearsome dragon."),
    ("The Da Vinci Code", "Dan Brown",
     "A symbologist and cryptologist uncover shocking secrets hidden within famous artworks and religious history."),
    ("Pride and Prejudice", "Jane Austen",
     "A romantic and witty tale about Elizabeth Bennet and Mr. Darcy, exploring themes of class, love, and misunderstanding."),
    ("The Fault in Our Stars", "John Green",
     "Two teenage cancer patients fall in love and embark on a journey to meet their favorite author, learning about life and loss."),
    ("The Lord of the Rings", "J.R.R. Tolkien",
     "An epic quest to destroy a powerful ring that could bring darkness to all of Middle-earth."),
    ("The Martian", "Andy Weir",
     "An astronaut stranded on Mars must use his ingenuity and science skills to survive until rescue arrives."),
    ("Gone Girl", "Gillian Flynn",
     "A suspenseful thriller about a woman’s disappearance and the disturbing secrets that unfold about her marriage."),
    ("To Kill a Mockingbird", "Harper Lee",
     "A powerful story about racial injustice and moral growth told through the eyes of young Scout Finch in 1930s Alabama."),
    ("The Alchemist", "Paulo Coelho",
     "A philosophical journey of a shepherd named Santiago who follows his dream of finding treasure and discovers his purpose in life.")
]

# SQL Query
query = """
INSERT INTO books (title, author, description)
VALUES (%s, %s, %s)
"""

# Insert all books
cursor.executemany(query, books_data)
db.commit()

print("✅ 10 books inserted successfully!")

# Close connection
cursor.close()
db.close()
