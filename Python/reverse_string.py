def reverse(text):
    rev = ""
    for index in range(len(text)-1,-1,-1):
        rev = rev + text[index]
    return rev

print reverse("Socorram-me, subi no onibus em marrocos")