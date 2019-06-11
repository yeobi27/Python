from typing import List, Any

class Book:

    def __init__(self, title: str, authors: List[str], publisher: str,
                 isbn: str, price: float) -> None:

        self.title = title
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price        

    def num_authors(self) -> int:

        return len(self.authors)
    
