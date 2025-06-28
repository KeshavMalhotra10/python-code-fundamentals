# 🗂️ Project: Book Management System

'''🔧 Features:
- Add a book (title, author, year)
- View all books
- Search for a book by title
- Delete a book by title
- Exit the program
'''

bookDict = {}

def bookApp():
    while True:
        userInput = input("\nType Add, Delete, View, Search or Exit: ").lower()

        if userInput == 'add':
            title = input("Enter a book title: ").lower()
            year = input("Enter year of publication: ").lower()
            author = input("Enter author's last name: ").lower()
            bookDict[title] = {'year': year, 'author': author}
            print(f"Book '{title}' added successfully!")

        elif userInput == 'delete':
            delete = input("Enter title of book you want to delete: ").lower()
            if delete in bookDict:
                del bookDict[delete]
                print(f"Book '{delete}' deleted.")
            else:
                print("Book not found.")

        elif userInput == 'view':
            if not bookDict:
                print("No books in your collection.")
            else:
                print("Here are all the books in your collection:")
                for title in bookDict:
                    print(f"Title: {title.title()}, Author: {bookDict[title]['author'].title()}, Year: {bookDict[title]['year']}")

        elif userInput == 'search':
            search = input("Enter the title of the book you want to search for: ").lower()
            if search in bookDict:
                print(f"Title: {search.title()}, Author: {bookDict[search]['author'].title()}, Year: {bookDict[search]['year']}")
            else:
                print("Book not found.")

        elif userInput == 'exit':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please type Add, Delete, View, Search or Exit.")

bookApp()
