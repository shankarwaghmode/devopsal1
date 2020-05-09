#def count_character(text):
'''    result={}
    for letter in text:
        if letter not in text :
            bool=isalpha(letter)
            if bool == 'True' :
                result[letter]=result[letter]+1
            else :
                pass
    else :
        pass
print(count_character("AaBbCc"))'''
def count_character(text):
    result=dict()
    for letter in text :
        if letter.isalpha() :
            if letter not in result :
                result[letter]=1
count_character("shankar")
print(result)
