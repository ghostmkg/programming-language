def count_books_by_author(book_catalog, title):
    for book in book_catalog :
        count = 0
        if book == title :
            count += 1
    return count