#Esta função remove as vogais das frases de entrada
def anti_vowel(text):
    resp = ""
    for index in range(0,len(text)):
        for letter in "aeiouAEIOU":
            if text[index] != letter:
                vogal = False
            else:
                vogal = True
                break
        if not vogal:
            resp += text[index]
    return resp
            