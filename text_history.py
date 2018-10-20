#C:\Users\User\Desktop\Python\GitHub\TechnoPark_DZ_3\text_history.py

class TextHistory:
    def __init__(self):
        self.text = ''
        self.version = int(0)
        self.history = []
    def apply_action(self, step):
        self.text = step.apply_action(self.text)
        self.history.append(step)
        self.version += 1
        return self.version

    def insert(self, text, pos):
        step = InsertAction(text, pos, self.version, self.version + 1)
        return self.apply_action(step)


    def replace(self, text, pos):
        pass
    def delete(self, pos, length):
        pass
    def action(self, action):
        pass
    def get_action(self, from_version, to_version):
        pass


class Action:
    def __init_(self, from_version, to_version):
        self.from_version = from_version
        self.to_version = to_version


class InsertAction(Action):
    def __init__(self, text, pos, from_version, to_version):
        if text != None:
            self.text = text
        if pos < 0 or pos is None:
            raise ValueError()
        else:
            self.pos = pos

    def apply_action(self, text_from_history):
        if len(text_from_history) < self.pos:
            raise ValueError()
        else:
            BEGIN = text_from_history[:self.pos]
            END = text_from_history[self.pos:]
            text_from_history = BEGIN + self.text + END
        return text_from_history

class ReplaceAction(Action):
    pass


class DeleteAction(Action):
    pass

'''h = TextHistory()
print(h.text)
print(h.insert('abc', 0))
print(h.text)
print(h.insert('xyz', 2))
print(h.text) '''
