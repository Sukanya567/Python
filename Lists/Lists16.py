sentence = "You cannot end a sentence with because because because is a conjunction"
phrase = "because because because"
start_index = sentence.find(phrase)
end_index = start_index + len(phrase)
sliced_sentence = sentence[:start_index] + sentence[end_index:]
print("Sentence after slicing out the phrase:", sliced_sentence)
