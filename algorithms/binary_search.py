# algorithms/binary_search.py

def binary_search(books, target_title):
    """
    Perform binary search on sorted list of books (by title).
    Each book is a dict: {'title': ..., 'author': ..., 'description': ...}
    """
    low, high = 0, len(books) - 1
    target_title = target_title.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_title = books[mid]['title'].lower()

        if mid_title == target_title:
            return books[mid]  # Found
        elif mid_title < target_title:
            low = mid + 1
        else:
            high = mid - 1
    return None  # Not found
