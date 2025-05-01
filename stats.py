def get_num_words(booklist):
    return len(booklist.split())

def get_chars(bookstring):
    bookstring_lower = bookstring.lower()
    bookset = set(bookstring_lower)
    bookdict = {}
    for bookchar in bookset:
        bookdict.update({bookchar: bookstring_lower.count(bookchar)})
    return bookdict

def get_list(bookdict):
    booklist = []
    for key, value in bookdict.items():
        booklist.append({"char": key, "num": value})
    return booklist

def sort_on(dict):
    return dict["num"]

def sort_list(booklist):
    booklist.sort(reverse=True, key=sort_on)
    return booklist
