import datetime
class Note:
    def __init__(self,memo,tags=""):
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
    def match(self,search_filter):
        if search_filter in self.memo:
            return True
        if search_filter in self.tags:
            return True
        return False
    def __str__(self):
        return f"{str(self.creation_date)} tags:{self.tags}; Message: \n {self.memo}"
    def __repr__(self):
        return f"Note({str(self.creation_date)},{self.memo},{self.tags})"

class Notebook:
    def __init__(self,notes=[]):
        self.notes = notes
    def search(self,search_filter):
        found = []
        for note in self.notes:
            if note.match(search_filter):
                found.append(note)
        return found
    def new_note(self,memo,tags=""):
        self.notes.append(Note(memo,tags))
    def modify_memo(self,note_id,memo):
        self.notes[note_id].memo = memo
    def modify_tags(self,note_id,tags):
        self.notes[note_id].tags = tags
    def __str__(self):
        notes = ""
        for note in self.notes:
            notes = notes + str(note) + "\n"
        return f"Notes in notebook:\n {notes}"
    def __repr__(self):
        return f"Notebook({self.notes})"

if __name__ == "__main__":
    p = Note('Do something','current action')
    book = Notebook()
    book.notes.append(p)
    book.new_note("Stop, take a break","don't do this")
    book.new_note('Template note')
    print(book.search('current action'))
    book.modify_tags(2,"generic tag")
    book.modify_memo(1,"don't procrastinate")
    print(book)