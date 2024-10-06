def add_book(l_dict,name,author):
    if name not in l_dict:
        l_dict[name]=author
        print(f"{name} added to library")
    else:
        print("Book already exists")

def remove_book(l_dict,name):
    if name in l_dict:
        del l_dict[name]
        print(f"{name} deleted from library")
    else:
        print(f"{name} not found in library")

def display_book(l_dict):
    for name,author in l_dict.items():
        print(f"{name} : {author}")

def search_book(l_dict,name):
    if name in l_dict:
        print(f"{name} : {l_dict[name]}")
    else:
        print(f"{name} not found in library")

def main():
    library_dict={}

    while 1:
        print("1. Add Book\n2. Remove Book\n3. Display Book\n4. Search Book\n5. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                book_name=input("Enter book name: ")
                author_name=input("Enter author name: ")
                add_book(library_dict,book_name,author_name)
            case 2:
                book_name=input("Enter book name: ")
                remove_book(library_dict,book_name)
            case 3:
                display_book(library_dict)
            case 4:
                book_name=input("Enter book name: ")
                search_book(library_dict,book_name)
            case 5:
                print("Exiting...")
                exit()

if __name__=="__main__":
    main()  

