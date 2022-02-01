
class ConLLToken:
    def __init__(self, form, lemma, pos, morph):
        self.form = form
        self.lemma = lemma
        self.pos = pos
        self.morph = morph
        self.__parsed_morph = self.__parse_morph(morph)

    def is_punctuation(self):
        return self.pos == "PUNCT"
    
    def get_person(self):
        if "Person" in self.__parsed_morph:
            return self.__parsed_morph["Person"]
        else:
            return None
        
    def is_inflected(self):
        return self.form.lower() != self.lemma.lower()
    
    def __str__(self):
        return self.form + "," + self.lemma + "," + self.pos + "," + self.morph
        
    def __parse_morph(self, morph):
        if morph == "_":
            return { }
        
        result = { }
        for part in morph.split("|"):
            name, val = part.split("=")
            result[name] = val
        return result

if __name__ == "__main__":
    tok1 = ConLLToken("comes", "come", "VERB", "Mood=Ind|Number=Sing|Person=3")
    tok2 = ConLLToken("years", "year", "NOUN", "Number=Plur")
	  	 
                 
    print("Token 1:", str(tok1))
    print("Token 2:", tok2)

    tok2 = ConLLToken("year", "year", "NOUN", "Number=Sing")
    tok3 = ConLLToken(",", ",", "PUNCT", "_")

    print("Punctuation?",
        tok1.is_punctuation(),
        tok2.is_punctuation(),
        tok3.is_punctuation())

    print("Inflected?",
        tok1.is_inflected(),
        tok2.is_inflected(),
        tok3.is_inflected())

    print("Person?",
        tok1.get_person(),
        tok2.get_person(),
        tok3.get_person())
