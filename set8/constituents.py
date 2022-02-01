class Token:
    def __init__(self, pos, word):

        self.pos = pos
        self.word = word

    def __str__(self):
        return f"({self.pos} {self.word})"


class Phrase:
    def __init__(self, phrase_type, children):

        self.phrase_type = phrase_type
        self.children = children

    def __str__(self):
        x = f"({self.phrase_type} "
        for item in self.children:
            x += str(item)
        x += ")"
        return x
