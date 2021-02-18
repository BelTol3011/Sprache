from data_source import *

singular = "number singular"
plural = "number plural"

feminine = "gender feminine"
masculine = "gender masculine"
neutral = "gender neutral"

nominative = "case nominative"
genitive = "case genitive"
dative = "case dative"
accusative = "case accusative"

plusquamperfekt = "tense plusquamperfekt"
perfekt = "tense perfekt"
präteritum = "tense präteritum"
präsens = "tense präsens"
futur_I = "tense futur_I"
futur_II = "tense futur_II"

attributive = "adjective attributive"
predikative = "adjective predikative"
adverbial = "adjective adverbial"

positiv = "comparison positive"
komparativ = "comparison comparative"
superlativ = "comparison superlative"

strong = "declination strong"
weak = "declination weak"
mixed = "declination mixed"


class Word:
    def __init__(self, word):
        self.word = word

    def modify(self, *_, **__):
        return Word(self.word)


class Noun(Word):
    def __init__(self, word):
        super().__init__(word)
        self.number = None
        self.gender = None
        self.kasus = None
        self.declination = None

    def modify(self, new_numerus, new_kasus, *_, **__):
        self.number = new_numerus
        self.kasus = new_kasus

        self.word = decline_substantiv()


class Verb(Word):
    def __init__(self, word):
        super().__init__(word)
        self.number = None
        self.gender = None
        self.modus = None
        self.tempus = None


class AttributAdjektiv(Word):
    def __init__(self, word):
        super().__init__(word)
        self.number = None
        self.gender = None
        self.kasus = None
        self.komparation = None


class AdverbialAdjektiv(Word):
    def __init__(self, word):
        super().__init__(word)
        self.komparation = None


class Artikel(Word):
    def __init__(self, word):
        super().__init__(word)
        self.number = None
        self.gender = None
        self.kasus = None


class Pronomen(Word):
    def __init__(self, word):
        super().__init__(word)
        self.number = None
        self.gender = None
        self.kasus = None
