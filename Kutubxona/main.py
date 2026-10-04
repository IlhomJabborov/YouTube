
from read import Book, load_books  
from add_show_delete import add_books, show_books, delete_book


# ==== AOSIY MENYU ====

def main():
    books = load_books()

    while True:
        print("\n=== KUTUBXONA BOSHQARUV DASTURI ===")
        print("1. Kitob qo'shish")
        print("2. Kitoblar ro'yxati")
        print("3. Kitob o'chirish")
        print("4. Dasturdan chiqish")

        choice = input("Tanlang (1-4): ")

        if choice == '1':
            add_books(books)
        elif choice == '2':
            show_books(books)
        elif choice == '3':
            delete_book(books)
        elif choice == '4':
            print("👋 Dastur yakunlandi")
            break
        else :
            print("⚠️ Noto'g'ri tanlov")

main()