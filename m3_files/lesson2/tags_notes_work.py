"""РАБОТА С ТЕКСТОМ ЗАМЕТКИ И ТЕГАМИ"""


def add_note():
    """добавить заметку"""
    note_name, ok = QInputDialog.getText(
        notes_win, "Добавить заметку", "Название заметки: "
    )
    if ok and note_name != '':
        notes[note_name] = {'текст': '', 'теги': []}
        list_notes.addItem(note_name)
        list_tags.addItem(notes[note_name]['теги'])
        print(notes)


def del_note():
    """Удаляет выбранную заметку из словаря notes, из файла и из виджетов"""
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=True)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')


def save_note():
    """Сохраняет текст в выбранную заметку из словаря notes и обновляет файл с данными"""
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=True)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')


def show_note():
    """Получает текст из заметки с выделенным названием, отображает его в поле редактирования"""
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])


def add_tag():
    """Добавляет тег в список тегов данной заметки и обновляет файл с данными"""
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            field_tag.clear()
            with open('notes_data.json', 'w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=True)
            print(notes)
    else:
        print('Заметка для добавления тега не выбрана!')


def del_tag():
    """Удаляет тег из списка тегов данной заметки и обновляет файл с данными"""
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['теги'])
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=True)
        print(notes)
    else:
        print('Тег для удаления не выбран!')


def search_tag():
    """Поиск заметок с заданным тегом"""
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == 'Искать заметки по тегу' and tag:
        print(tag)
        notes_searched = {}  # здесь будут заметки с выделенным тегом
        for note in notes:
            if tag in notes[note]['теги']:
                notes_searched[note] = notes[note]
        button_tag_search.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_searched)
        print(button_tag_search.text())
    elif button_tag_search.text() == 'Сбросить поиск':
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText('Искать заметки по тегу')
        print(button_tag_search.text())
    else:
        pass
