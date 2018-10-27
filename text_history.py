#C:\Users\User\Desktop\Python\GitHub\TechnoPark_DZ_3\text_history.py

class TextHistory:
    def __init__(self):
        self.text = ''
        self.version = 0
        self.history = []
    def action(self, action_):
        if action_.from_version >= action_.to_version:
            raise ValueError()
        else:
            self.text = action_.apply(self.text)
            self.history.append(action_)
            self.version = action_.to_version
            return self.version

    def insert(self, text, pos = None):
        if pos is None:
            pos = len(self.text)
        action_ = InsertAction(text, pos, self.version)
        return self.action(action_)

    def replace(self, text, pos = None):
        if pos is None:
            pos = len(self.text)
        action_ = ReplaceAction(text, pos, self.version)
        return self.action(action_)

    def delete(self, pos, length):
        if pos + length > len(self.text):
            raise ValueError()
        else:
            action_ = DeleteAction(pos, length, self.version)
            return self.action(action_)

    def get_actions(self, from_version = None, to_version = None):
        optimisation_flag = False
        if self.history == []:
            return []
        if from_version is None:
            from_version = 0
        if to_version is None:
            to_version = self.history[-1].to_version
        if from_version > to_version:
            raise ValueError()
        if from_version < 0:
            raise ValueError()
        if to_version > self.history[-1].to_version:
            raise ValueError()
        actions = []
        for i in self.history:
            if i.from_version >= from_version and i.to_version <= to_version:
                actions.append(i)
        if optimisation_flag:
            return optimisation(actions)
        else:
            return actions

    def optimisation(self, actions):

        for i in range(len(actions)-1):
            if isinstance(actions[i], InsertAction) and isinstance(actions[i+1], DeleteAction):
                '''Вставить текст и удалить в случае разных длины текста и длины удаления'''
                if actions[i].pos == actions[i+1].pos:
                    if len(actions[i].text) >= actions[i+1].length:
                        start = len(actions[i].text) - actions[i+1].length
                        text = actions[i].text[start:]
                        from_version = actions[i].from_version
                        to_version = actions[i+1].to_version
                        pos = actions[i].pos
                        action_ = InsertAction(text, pos, from_version, to_version)
                        actions.pop(i), actions.pop(i)
                        actions.insert(i, action_)
                    elif len(actions[i].text) >= actions[i+1].length:
                        actions.pop(i), actions.pop(i)
                    else:
                        pos = actios[i].pos
                        length -= len(actions[i].text)
                        from_version = actions[i].from_version
                        to_version = actions[i+1].to_version
                        action_ = DeleteAction(pos, length, from_version, to_version)
                        actions.pop(i), actions.pop(i)
                        actions.insert(i, action_)
            if isinstance(actions[i], ReplaceAction) and isinstance(actions[i+1], DeleteAction):
                '''Последовательно замена и удаление текста той же длины, что и в замене'''
                if actions[i].pos == actions[i+1].pos and len(actions[i].text) == actions[i+1].length:
                    pos = actions[i].pos
                    length = actions[i+1].length
                    from_version = actions[i].from_version
                    to_version = actions[i+1].to_version
                    action_=DeleteAction(pos, length, from_version, to_version)
                    actions.pop(i), actions.pop(i)
                    actions.insert(i, action_)
        return actions

class Action:
    def __init_(self, from_version, to_version):
        self.from_version = from_version
        self.to_version = to_version

class InsertAction(Action):
    def __init__(self, text, pos, from_version, to_version = None):
        if from_version is None:
             self.from_version = 0
        else:
            self.from_version = from_version
        if to_version is None:
            self.to_version = self.from_version + 1
        else:
            self.to_version = to_version
        if text is not None:
            self.text = text
        if pos < 0:
            raise ValueError()
        else:
            self.pos = pos

    def apply(self, text_from_history):
        if len(text_from_history) < self.pos:
            raise ValueError()
        else:
            BEGIN = text_from_history[:self.pos]
            END = text_from_history[self.pos:]
            text_from_history = BEGIN + self.text + END
        return text_from_history

class ReplaceAction(Action):
    def __init__(self, text, pos, from_version, to_version = None):
        self.from_version = from_version
        if to_version is None:
            self.to_version = self.from_version + 1
        else:
            self.to_version = to_version
        if text is not None:
            self.text = text
        if pos < 0 or pos is None:
            raise ValueError()
        else:
            self.pos = pos

    def apply(self, text_from_history):
        if len(text_from_history) < self.pos:
            raise ValueError()
        else:
            BEGIN = text_from_history[:self.pos]
            END = text_from_history[self.pos + len(self.text):]
            text_from_history = BEGIN + self.text + END
        return text_from_history

class DeleteAction(Action):
    def __init__(self, pos,length, from_version, to_version = None):
        self.from_version = from_version
        self.length = length
        if to_version is None:
            self.to_version = self.from_version + 1
        else:
            self.to_version = to_version
        if pos < 0 or pos is None:
            raise ValueError()
        else:
            self.pos = pos

    def apply(self, text_from_history):
        if len(text_from_history) < self.pos:
            raise ValueError()
        else:
            BEGIN = text_from_history[:self.pos]
            END = text_from_history[self.pos + self.length:]
            text_from_history = BEGIN + END
        return text_from_history
