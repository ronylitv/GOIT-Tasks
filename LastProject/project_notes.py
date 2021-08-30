import json


class Note:
    def __init__(self, note: str):
        self.note = note

    # def change_note(self, mode, new_text):
    #     if mode == '--rw':
    #         self.note = new_text
    #     elif mode == '--a':
    #         self.note += new_text

    def __repr__(self):
        return f'{self.note}'


class NoteRecord:
    def __init__(self, note, tag=None):
        self.note = Note(note)
        self.tag = tag
        self.filename = 'data.json'
        self.record = {
            'note': str(self.note),
            'tag': self.tag
        }

    def serialize(self, list_of_notes=None):
        if list_of_notes is None:
            list_of_notes = []
        if list_of_notes:
            with open(self.filename, 'w') as file:
                json.dump(list_of_notes + [self.record], file)
        else:
            with open(self.filename, 'w') as file:
                json.dump([self.record], file)

    def deserialize(self):
        with open(self.filename, 'r') as file:
            return json.load(file)


while True:
    command = input(': ')
    sep_val = command.split(' ')
    if sep_val[0] == 'note' and sep_val[1] != 'change':
        tag_index = sep_val.index('-tag') if '-tag' in sep_val else len(sep_val)
        main_note = NoteRecord(
            ' '.join(sep_val[1:tag_index]),
            sep_val[tag_index + 1:] if tag_index != len(sep_val) else None
        )
        try:
            note_list = main_note.deserialize()
            main_note.serialize(note_list)
        except FileNotFoundError:
            main_note.serialize()
    elif sep_val[0] == '.':
        break
    else:
        print('Try again!')
