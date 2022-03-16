alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


# Part 1
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def has_duplicates(s):
    h = histogram(s)
    return any([value > 1 for value in h.values()])


for word in test_dups:
    print(word, " has duplicates" if has_duplicates(word) else " has no duplicates")


# Part 2
def missing_letters(s):
    return "".join([c for c in alphabet if c not in s])


for word in test_miss:
    missing = missing_letters(word)
    print(word, " uses all letters" if missing == "" else f" is missing letters {missing}")
