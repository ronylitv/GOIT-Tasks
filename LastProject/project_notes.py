import pickle


class Note:
    def __init__(self, note: str):
        self.note = note

    def change_note(self, mode, new_text):
        if mode == '--rw':
            self.note = new_text
        elif mode == '--a':
            self.note += new_text


class NoteRecord:
    def __init__(self, note, *tag: str):
        self.note = Note(note)
        self.tag = tag

    def serialize(self):
        with open(str(self.tag), 'wb') as file:
            pickle.dump(self.note, file)



while True:
    command = input(': ')
    sep_val = command.split(' ')
    if sep_val[0] == 'note':
        if '-tag' in sep_val:
            tag_index = sep_val.index('-tag')
            note = NoteRecord(' '.join(sep_val[:tag_index]), )





