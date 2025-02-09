sentence =input("")
acr = acronym = ''.join(word[0].upper() for word in sentence.split())
print(acr)