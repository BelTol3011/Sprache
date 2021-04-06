singular = "number singular"
plural = "number plural"
numbers = [singular, plural]

first_person = "person 1."
second_person = "person 2."
third_person = "person 3."
persons = [first_person, second_person, third_person]

feminine = "gender feminine"
masculine = "gender masculine"
neuter = "gender neutral"
genders = [feminine, masculine, neuter]

nominative = "case nominative"
genitive = "case genitive"
dative = "case dative"
accusative = "case accusative"
cases = [nominative, genitive, dative, accusative]

plusquamperfekt = "tense plusquamperfekt"
perfekt = "tense perfekt"
präteritum = "tense präteritum"
präsens = "tense präsens"
futur_I = "tense futur_I"
futur_II = "tense futur_II"
tenses = [plusquamperfekt, perfekt, präteritum, präsens, futur_I, futur_II]

positive = "comparison positive"
comparative = "comparison comparative"
superlative = "comparison superlative"
comparisons = [positive, comparative, superlative]

strong = "declension strong"
weak = "declension weak"
mixed = "declension mixed"
declension_types = [strong, weak, mixed]

verb_suffixes = {
    singular: {first_person: "e",
               second_person: "st",
               third_person: "t"},
    plural: {first_person: "en",
             second_person: "t",
             third_person: "en"}
}
verb_suffixes_list = ["e", "st", "t", "en"]

personal_pronouns = {
    nominative: {singular: {first_person: {masculine: "ich", feminine: "ich", neuter: "ich"},
                            second_person: {masculine: "du", feminine: "du", neuter: "du"},
                            third_person: {masculine: "er", feminine: "sie", neuter: "es"}},
                 plural: {first_person: {masculine: "wir", feminine: "wir", neuter: "wir"},
                          second_person: {masculine: "ihr", feminine: "ihr", neuter: "ihr"},
                          third_person: {masculine: "sie", feminine: "sie", neuter: "sie"}}},
    genitive: {singular: {first_person: {masculine: "mich", feminine: "mich", neuter: "mich"},
                          second_person: {masculine: "dich", feminine: "dich", neuter: "dich"},
                          third_person: {masculine: "sich", feminine: "sich", neuter: "sich"}},
               plural: {first_person: {masculine: "uns", feminine: "uns", neuter: "uns"},
                        second_person: {masculine: "euch", feminine: "euch", neuter: "euch"},
                        third_person: {masculine: "sich", feminine: "sich", neuter: "sich"}}},
    dative: {singular: {first_person: {masculine: "mir", feminine: "mir", neuter: "mir"},
                        second_person: {masculine: "dir", feminine: "dir", neuter: "dir"},
                        third_person: {masculine: "sich", feminine: "sich", neuter: "sich"}},
             plural: {first_person: {masculine: "uns", feminine: "uns", neuter: "uns"},
                      second_person: {masculine: "euch", feminine: "euch", neuter: "euch"},
                      third_person: {masculine: "sich", feminine: "sich", neuter: "sich"}}},
    accusative: {singular: {first_person: {masculine: "mich", feminine: "mich", neuter: "mich"},
                            second_person: {masculine: "dich", feminine: "dich", neuter: "dich"},
                            third_person: {masculine: "sich", feminine: "sich", neuter: "sich"}},
                 plural: {first_person: {masculine: "uns", feminine: "uns", neuter: "uns"},
                          second_person: {masculine: "euch", feminine: "euch", neuter: "euch"},
                          third_person: {masculine: "sich", feminine: "sich", neuter: "sich"}}}
}

from data_source import *


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
        self.declination_type = None

    def modify(self, new_numerus, new_kasus, *_, **__):
        self.word = decline_noun(self.word, new_numerus, new_kasus, self.declination_type)

        self.number = new_numerus
        self.kasus = new_kasus


class Verb(Word):
    def __init__(self, word: str, number: str = None, person: str = None, word_stem: str = None):
        super().__init__(word)
        self.number = number
        self.person = person
        self.word_stem = word_stem
        if self.word_stem is None:
            self.word_stem = get_verb_word_stem(self.word)

    def get_conjugation(self, number: str, person: str) -> str:
        return conjugate_verb(self.word_stem, number, person)

    def modify(self, new_number: str, new_person: str):
        self.word = self.get_conjugation(new_number, new_person)


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


class NounPhrase:
    ...


class VerbPhrase:
    ...
