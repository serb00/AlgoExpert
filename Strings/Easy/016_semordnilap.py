def semordnilap(words):
    # Write your code here
    res = []
    set_words = set(words)
    for word in words:
        rev = word[::-1]
        if word != rev and rev in set_words:
            res.append([word, rev])
            set_words.remove(word)
            set_words.remove(rev)

    return res


print(semordnilap(["dog", "hello", "desserts", "test", "god", "stressed"]))
