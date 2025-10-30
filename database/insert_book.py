from db_connection import get_db

db = get_db()

books_data = [
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling",
     "description": "A young boy discovers he is a wizard and attends Hogwarts School of Witchcraft and Wizardry, where he faces magical adventures and dark secrets."},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien",
     "description": "Bilbo Baggins, a humble hobbit, is pulled into a thrilling adventure to reclaim a lost dwarf kingdom from a fearsome dragon."},
    {"title": "The Da Vinci Code", "author": "Dan Brown",
     "description": "A symbologist and cryptologist uncover shocking secrets hidden within famous artworks and religious history."},
    {"title": "Pride and Prejudice", "author": "Jane Austen",
     "description": "A romantic and witty tale about Elizabeth Bennet and Mr. Darcy, exploring themes of class, love, and misunderstanding."},
    {"title": "The Fault in Our Stars", "author": "John Green",
     "description": "Two teenage cancer patients fall in love and embark on a journey to meet their favorite author, learning about life and loss."},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien",
     "description": "An epic quest to destroy a powerful ring that could bring darkness to all of Middle-earth."},
    {"title": "The Martian", "author": "Andy Weir",
     "description": "An astronaut stranded on Mars must use his ingenuity and science skills to survive until rescue arrives."},
    {"title": "Gone Girl", "author": "Gillian Flynn",
     "description": "A suspenseful thriller about a woman’s disappearance and the disturbing secrets that unfold about her marriage."},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",
     "description": "A powerful story about racial injustice and moral growth told through the eyes of young Scout Finch in 1930s Alabama."},
    {"title": "The Alchemist", "author": "Paulo Coelho",
     "description": "A philosophical journey of a shepherd named Santiago who follows his dream of finding treasure and discovers his purpose in life."}
]

db.books.insert_many(books_data)
print("✅ 10 books inserted successfully!")
