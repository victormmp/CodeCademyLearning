def censor(text, word):
    cens = ""
    te = text.split()
    for char in range(len(word)):
        cens += '*'
    for index, wo in enumerate(te):
        if wo == word:
            te[index] = cens
    return " ".join(te)