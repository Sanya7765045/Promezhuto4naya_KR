from logic import *

file_path = "Notes.json"

while True:
    display_menu()
    user_choice = input("Выберите вариант (1-5): ")
    if user_choice == '5':
        break
    if user_choice == '1':
        add_note_file(file_path)
    elif user_choice == '2':
        show_file(file_path)
    elif user_choice == '3':
        edit_note_file(file_path)
    elif user_choice == '4':
        delete_note_file(file_path)
    else:
        print("Неверный выбор")