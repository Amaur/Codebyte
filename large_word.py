#encoding:utf-8
print("Teste 2")

def largest_word(string):
    word_split=string.split()
    large=word_split[0]
    i=0
    while (i<len(word_split)-1):
        if(len(large)< len(word_split[i+1])):
            large=word_split[i+1]
            i=i+1
        else:
            large=large
            i=i+1
    return large



word ="determiningFor this challenge you will be  the largest word in a string "
print(largest_word(word))