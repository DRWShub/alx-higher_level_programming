#!/usr/bin/pytho3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    best = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        if a_dictionary.get(key) < a_dictionary[key]:
            best = key
    return best
