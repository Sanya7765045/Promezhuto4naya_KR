import json
from datetime import datetime

def display_menu():
    print("Меню:\n")
    print("1. Добавить заметку:\n")
    print("2. Просмотреть список заметок:\n")
    print("3. Редактировать заметку:\n")
    print("4. Удалить заметку:\n")
    print("5. Выйти:\n")

def add_note_file(file_path):
    try:
        note = {}
        note["id"] = int(input("Введите идентификатор заметки: "))
        note["title"] = input("Введите заголовок заметки: ")
        note["body"] = input("Введите текст заметки: ")
        note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, 'a', encoding='utf-8') as file:
            json.dump(note, file)
            file.write('\n')

        print(f"Заметка успешно добавлена в файл '{file_path}'.")
    except IOError:
        print(f"Ошибка при записи файла '{file_path}'.")

def show_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            notes = file.readlines()

        if not notes:
            print("Файл заметок пуст.")
        else:
            print(f"Содержимое файла '{file_path}':")
            for note in notes:
                note_data = json.loads(note)
                print(f"Идентификатор: {note_data['id']}")
                print(f"Заголовок: {note_data['title']}")
                print(f"Текст: {note_data['body']}")
                print(f"Дата/Время: {note_data['timestamp']}")
                print()

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except IOError:
        print(f"Ошибка при чтении файла '{file_path}'.")

def edit_note_file(file_path):
    try:
        notes = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                notes.append(json.loads(line))

        if not notes:
            print("Файл заметок пуст.")
            return

        print("Содержимое файла заметок:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. Идентификатор: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Дата/Время: {note['timestamp']}")

        choice = int(input("Выберите номер заметки для редактирования: ")) - 1

        if 0 <= choice < len(notes):
            edited_note = notes[choice]
            print(f"\nРедактирование заметки: {edited_note}")
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            edited_note["title"] = new_title
            edited_note["body"] = new_body
            edited_note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file_path, 'w', encoding='utf-8') as file:
                for note in notes:
                    json.dump(note, file)
                    file.write('\n')

            print("Заметка успешно отредактирована.")
        else:
            print("Некорректный выбор заметки.")
    except IOError:
        print(f"Ошибка при открытии файла заметок '{file_path}'.")

def delete_note_file(file_path):
    try:
        notes = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                notes.append(json.loads(line))

        if not notes:
            print("Файл заметок пуст.")
            return

        print("Содержимое файла заметок:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. Идентификатор: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Дата/Время: {note['timestamp']}")

        choice = int(input("Выберите номер заметки для удаления: ")) - 1

        if 0 <= choice < len(notes):
            deleted_note = notes.pop(choice)

            with open(file_path, 'w', encoding='utf-8') as file:
                for note in notes:
                    json.dump(note, file)
                    file.write('\n')

            print(f"Заметка '{deleted_note['title']}' успешно удалена из файла.")
        else:
            print("Некорректный выбор заметки.")

        show_file(file_path)
    except IOError:
        print(f"Ошибка при открытии файла заметок '{file_path}'.")