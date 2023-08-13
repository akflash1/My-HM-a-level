#https://www.codewars.com/kata/5a81b78d4a6b344638000183/train/python
def conjugate(verb):
    verb_type = verb[-2:]
    suffixes = []
    if verb_type == "AR":
        suffixes = ["o", "as", "a", "amos", "áis", "an"]
    elif verb_type == "ER":
        suffixes = ["o", "es", "e", "emos", "éis", "en"]
    elif verb_type == "IR":
        suffixes = ["o", "es", "e", "imos", "ís", "en"]
    else:
        None

    conjugated = [verb + suffix for suffix in suffixes]
    return conjugated
