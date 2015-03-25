__author__ = 'andriy'
from vector import ukstemmer, prepositions


def transform_to_vector(text, mode):
    vect = {}
    query_list = []
    i = 0
    word_list = text.split()
    for word in word_list:
        if not (prepositions.is_preposition(word) or prepositions.is_conjunction(word) or prepositions.is_fraction(word)):
            if mode:
                if not i % 8:
                    query_list.append(word)
                else:
                    query_list[-1] += " " + word
            s = ukstemmer.UkrainianStemmer(word)
            if s.stem_word() in vect:
                vect[s.stem_word()] += 1
            else:
                vect.update({s.stem_word(): 1})
            i += 1
    return vect, query_list