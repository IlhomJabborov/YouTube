from read import Book

#  ==== FAYLGA KITOBLARNI YOZISH ====
def save_books(books):
    file = open("books.txt",'w')
    for book in books:
        file.write(book.to_string() + '\n') # itob_bomi;avftor_nomi\n
    file.close()

# ===== QO'SHISH KITOBNI ====

def add_books(books):
    title = str(input("Kitob nomi : "))
    author = str(input("Muallif : "))

    book = Book(title=title,author=author)
    books.append(book)
    save_books(books)

    print("✅ Kitob muvaffaqiyatli qo'shildi !")

# ==== KITOBLARNI KO'RISH ====
def show_books(books):
    if not books:
        print("📚 Kutubxonada kitob yo'q !")
        return
    
    print("\n📖 Kitoblar ro'yxati : ")
    for index,book in enumerate(books,start=1):
        print(f"{index}. {book.title} - {book.author}")


# ==== KITOB O'CHIRISH ====
def delete_book(books):

    show_books(books)

    if not books:
        return
    
    number = int(input("O'chirmoqchi bo'lgan kitob raqamingizni kiriting : "))

    if 1 <= number <= len(books) :
        removed = books.pop(number - 1) # 0. kitob - muallif  1,2,3
        save_books(books)

        print(f"❌ '{removed.title}' o'chirildi !")
    else:
        print("⚠️ Noto'g'ri raqam ! ")