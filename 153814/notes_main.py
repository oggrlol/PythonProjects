#empezar a crear smart notes 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QTextEdit, QListWidget, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QLineEdit, QInputDialog)
import json

app = QApplication([])

#parametros ventana
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(800,600)

#funcionalidad de la app

def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]['texto'])
    list_tags.clear()
    list_tags.addItems(notes[name]['etiquetas'])

def add_note():
    note_name, ventana = QInputDialog.getText(
        notes_win, 'Añadir nota', 'nombre de la nota:'
    )
    if ventana and note_name != '':
        notes[note_name] = {
                'texto' : '',
                'etiquetas' : []
            }
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['etiquetas'])

def save_note():
    if list_notes.selectedItems():
        clave = list_notes.selectedItems()[0].text()
        notes[clave]["texto"] = field_text.toPlainText()
        with open('notes_data.json','w') as file:
            json.dump(notes, file, sort_keys = True)
    else:
        print('No hay seleccionado nada')

def del_note():
    if list_notes.selectedItems():
        clave = list_notes.selectedItems()[0].text()
        del notes[clave]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys = True)
    else:
        print('No hay seleccionado nada')

def add_tag():
    if list_notes.selectedItems():
        clave = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if tag not in notes[clave]["etiquetas"]:
            notes[clave]["etiquetas"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys = True)
    else:
        print('No hay seleccionado nada')

def del_tag():
    if list_notes.selectedItems() and list_tags.selectedItems():
        clave = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[clave]["etiquetas"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[clave]["etiquetas"])
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys = True)
    else:
        print('No hay seleccionado nada')

def search_tag():
    tag = field_tag.text()
    if button_search_tag.text() == 'Buscar nota por etiqueta' and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["etiquetas"]:
                notes_filtered[note] = notes[note]
        button_search_tag.setText('Restablecer búsqueda')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif button_search_tag.text() == 'Restablecer búsqueda':
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_search_tag.setText('Buscar nota por etiqueta')

#widgets
list_notes_label = QLabel('Lista de notas')
list_notes = QListWidget()

button_create_note = QPushButton('Crear nota')
button_del_note = QPushButton('Eliminar nota')
button_save_note = QPushButton('Guardar nota')

list_tags_label = QLabel('Lista de etiquetas')
list_tags = QListWidget()
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Ingresar etiqueta...')
button_add_tag = QPushButton('Añadir a la nota')
button_del_tag = QPushButton('Eliminar etiqueta de nota')
button_search_tag = QPushButton('Buscar nota por etiqueta')

field_text = QTextEdit()

#organizar widgets

layout_notes = QHBoxLayout()

col1 = QVBoxLayout()
col1.addWidget(field_text)

col2 = QVBoxLayout()
col2.addWidget(list_notes_label)
col2.addWidget(list_notes)

row1 = QHBoxLayout()
row1.addWidget(button_create_note)
row1.addWidget(button_del_note)
col2.addLayout(row1)

row2 = QHBoxLayout()
row2.addWidget(button_save_note)
col2.addLayout(row2)
col2.addWidget(list_tags_label)
col2.addWidget(list_tags)
col2.addWidget(field_tag)

row3 = QHBoxLayout()
row3.addWidget(button_add_tag)
row3.addWidget(button_del_tag)
col2.addLayout(row3)

row4 = QHBoxLayout()
row4.addWidget(button_search_tag)
col2.addLayout(row4)

layout_notes.addLayout(col1)
layout_notes.addLayout(col2)

notes_win.setLayout(layout_notes)


list_notes.itemClicked.connect(show_note)
button_create_note.clicked.connect(add_note)
button_save_note.clicked.connect(save_note)
button_del_note.clicked.connect(del_note)
button_add_tag.clicked.connect(add_tag)
button_del_tag.clicked.connect(del_tag)
button_search_tag.clicked.connect(search_tag)

#ejecutar app
notes_win.show()

with open('notes_data.json','r') as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()