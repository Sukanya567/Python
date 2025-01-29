def create_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym
phrase = input("Enter a phrase: ")
acronym = create_acronym(phrase)
print("Acronym:", acronym)
