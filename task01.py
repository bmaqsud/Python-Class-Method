class Book:
    def __init__(self,title:str, author:str ):
       self.title=title
       self.author=author
    def get_info(self)-> str:
        book=f"muallif {self.author} uning nomi {self.title}"
        return book
book_mal=Book("Bo'ri", "Lera")
b=book_mal.get_info()
print(b)
   