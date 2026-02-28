movies = []

def add_movie():
    title = input("Enter movie title:")
    director = input("Enter movie director:")
    year = input("Enter movie release year:")

    movies.append({
        "title":title,
        "director":director,
        "year":year
    })

def show_movie():
    for m in movies:
        print_movie(m)

def print_movie(movie):
    print(f"Title:{movie["title"]}")
    print(f"Director:{movie["director"]}")
    print(f"Year:{movie["year"]}")

def find_movie():
    movie_title = input("Enter movie title:")
    for m in movies:
        if m["title"] == movie_title:
            print_movie(m)

menu_selection_option = """
To Add Movie Enter  : 'a'
To Show Movie Enter : 's'
To Find Movie Enter : 'f'
To Exit From Movie Menu Enter : 'q'
"""
user_optns={
    "a": add_movie, # Do not call function here, just point it
    "s": show_movie,
    "f": find_movie
}

def menu():
    selection = input(menu_selection_option)
    while selection != 'q':
        # 1st method
        if selection =='a':
            add_movie()
        elif selection =='s':
            show_movie()
        elif selection =='f':
            find_movie()

        # # 2nd method
        # if selection in user_optns:
        #     selected_fun = user_optns[selection]
        #     selected_fun()
        else:
            print('Unknown command, Please try again')
            
        selection = input(menu_selection_option)

menu()