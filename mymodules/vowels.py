vowels = set('aeeiouu')
def search4vowels(word):
    u = vowels.union(set(word))
    print(sorted(list(u)))
    d = vowels.difference(set(word))
    d1 = set(word).intersection(vowels)
    return list(d1)
def search4vowels(word,word1):
    """ return any vowels found in a supplied word."""
    u = vowels.union(set(word))
    print(sorted(list(u)))
    d = vowels.difference(set(word))
    d1 = set(word).intersection(vowels)
    return (d1)
def search4letters(word:str,letter='aeiou'):
    return set(letter).intersection(set(word))
def print2phreas(phreas1,phreas2):
    print(phreas1,phreas2)