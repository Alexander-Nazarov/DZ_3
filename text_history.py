#C:\Users\User\Desktop\Python\GitHub\TechnoPark_DZ_3\text_history.py

class TextHistory:
    def __init__(self):
        self.text = 'abc'
        self.version = int(0)
    def insert(self, tekst, pos = None):
        if pos is None:
            pos = len(self.text)
        self.insert = InsertAction.insert(self, self.text, tekst, pos)

class Action:
    def __init_(self, from_version, to_version):
        self.from_version = from_version
        self.to_version = to_version
    def apply(stroka, action):
        #if action is InsertAction:

        return new_stroka


class InsertAction(Action):
    def insert(self ,text, tekst, pos):
        #print(text)
        if len(text) >= pos >= 0:
            BEGIN = text[0:int(pos)]
            #print(tekst)
            END = text[int(pos):]
            text = BEGIN + tekst + END
            #print(text)
            return #self.version + 1
        else:
            raise ValueError
        return


class ReplaceAction(Action):
    pass


class DeleteAction(Action):
    pass

h = TextHistory()
#print(h.text, h.version)
print(h.insert('xyz', 1))
