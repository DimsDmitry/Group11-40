'''Функционал приложения'''


def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])


def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes) - 1) + ".txt", "w") as file:
            file.write(note[0] + '\n')


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index) + ".txt", "w") as file:
                    file.write(note[0] + '\n')
                    file.write(note[1] + '\n')
                    for tag in note[2]:
                        file.write(tag + ' ')
                    file.write('\n')
            index += 1
        print(notes)
    else:
        print("Заметка для сохранения не выбрана!")
