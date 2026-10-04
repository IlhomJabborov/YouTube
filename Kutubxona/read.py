# ==== Kitob Klassi ====

class Book:

    def __init__(self,title,author):
        self.title = title
        self.author =author

    
    def to_string(self):
        return self.title + ";" + self.author   # kitob_bomi;avftor_nomi
    

# ==== FAYLDAN KITOBLARNI O'QISH ====

def load_books():

    books = []

    try :
        file = open("books.txt",'r')
        lines = file.readline()
        file.close()

        for line in lines:
            data = line.strip().split(";")  # kitob;muallik , ['kitob','muallif']
            if len(data) == 2:
                book = Book(data[0],data[1])
                books.append(book)
    
    except:
        pass

    return books