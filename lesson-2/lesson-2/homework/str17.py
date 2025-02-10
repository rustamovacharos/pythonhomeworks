string=input("")
vowels = "a,o,u,i,e"
translation = str.maketrans("aouie","*****")
modified_string = string.translate(translation)
print(modified_string)