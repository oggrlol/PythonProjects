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
    key = list_notes.selectedItems()[0].text()
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])

def add_note():
    note_name, ventana = QInputDialog.getText(
        notes_win, 'Añadir nota', 'nombre de la nota:'
    )
    if ventana and note_name != '':
        note = list()
        note = [note_name,"",[]]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')

def save_note():
    if list_notes.selectedItems():
        i = 0
        clave = list_notes.selectedItems()[0].text()
        for note in notes:
            if note[0] == clave:
                note[1] = field_text.toPlainText()
                with open(str(i)+'.txt','w') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            i += 1
    else:
        print('No hay seleccionado nada')


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

num_name = 0

notes = []

while True:
    filename = str(num_name)+".txt"
    try:
        with open(filename, "r", encoding = 'utf-8') as file:
            for line in file:
                line = line.replace('\n','')
                notes.append(line)
        tags = note[2].split(' ')
        note[2] = tags

        notes.append(note)
        note = []
        name += 1
    except IOError:
        break


#ejecutar app
notes_win.show()

app.exec_()