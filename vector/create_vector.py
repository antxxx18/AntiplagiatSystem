__author__ = 'andriy'
from vector import ukstemmer, prepositions

num_words = 8

def transform_to_vector(text, mode):
    vect = {}
    query_list = []
    i = 0
    word_list = text.split()
    for word in word_list:
        if not (prepositions.is_preposition(word) or prepositions.is_conjunction(word) or prepositions.is_fraction(word)):
            if mode and ukstemmer.ukstemmer_search_preprocess(word) != "":
                if not i % num_words:
                    #query_list[0].append(word)
                    query_list.append(ukstemmer.ukstemmer_search_preprocess(word))
                else:
                    #query_list.append(query_list[-1][1:])
                    #query_list[-1].append(word)
                    query_list[-1] += " " + ukstemmer.ukstemmer_search_preprocess(word)
                i += 1
            s = ukstemmer.UkrainianStemmer(word)
            if s.stem_word() in vect:
                vect[s.stem_word()] += 1
            else:
                vect.update({s.stem_word(): 1})
    return vect, query_list