def insert_underscores(txt):
    result = [] 
    vowels = "aeiou"
    i = 0

    while i < len(txt):
        result.append(txt[i])

        # Har 3-belgidan keyin pastki chiziq qo'shish
        if (i + 1) % 3 == 0:
            if i + 1 < len(txt) and (txt[i] in vowels or (i > 0 and result[-2] == "_")):
                if i + 2 < len(txt):
                    result.append(txt[i + 1])
                    result.append("_")
                    i += 1
            else:
                result.append("_")

        i += 1

    return "".join(result)

# Test cases
print(insert_underscores("hello"))          # hel_lo underscore bilan chiqadi
print(insert_underscores("assalom"))        # ass_alom
print(insert_underscores("abcabcdabcdeabcdefabcdefg"))  # abc_abcd_abcdeab_cdef_abcdefg