from conlltoken import ConLLToken

class AbstractTokenBuilder:
    def __init__(self):
        pass
    
    def buildToken(self, line):
        pass
        
class ConLLUTokenBuilder(AbstractTokenBuilder):
    def __init__(self):
        pass
    
    def buildToken(self, line):
        parts = line.split()
        word = parts[1]
        lemma = parts[2]
        pos = parts[3]
        morph = parts[5]
        return ConLLToken(word, lemma, pos, morph)
    
class ConLL09TokenBuilder(AbstractTokenBuilder):
    def __init__(self):
        pass
    
    def buildToken(self, line):
        parts = line.split()
        word = parts[1]
        lemma = parts[2]
        pos = parts[4]
        morph = parts[6]
        return ConLLToken(word, lemma, pos, morph)
    
   
if __name__ == "__main__":
    # we have to have our own 'eq' function
    def eqTok(t1, t2):
        assert t1.word == t2.word
        assert t1.lemma == t2.lemma
        assert t1.pos == t2.pos
        assert t1.morph == t2.morph
        
    # checking ConLLUTokenBuilder
    builder = ConLLUTokenBuilder()
    conllULine = "1       President       President       PROPN   NNP     Number=Sing     5       nsubj   _       _"
    assert builder.buildToken(conllULine), ConLLToken("President", "President", "PROPN", "Number=Sing")
    
    # checking ConLL09TokenBuilder
    builder = ConLL09TokenBuilder()
    conll09Line = "44216_1 comes   come   _       VERB      _       Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin  _       4       _       SB      _       _       _       _"
    assert builder.buildToken(conll09Line), ConLLToken("comes", "come", "VERB", "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin")
    
    # for the exercises
    # checking ConLLUTokenBuilder
    builder = ConLLUTokenBuilder()
    conllULine = "1 The the DET _ Definite=Def|PronType=Art _ _ _ _"
    tok = builder.buildToken(conllULine)
    print("Token:", str(tok))
    print("Type:", type(tok))
    
   
