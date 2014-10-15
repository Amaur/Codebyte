#encoding:utf-8
def change(str):
    word=' '
    for w in str:
        if(ord(w) in range(65,91) or ord(w) in range(97,123)):
            if(ord(w)==90):
                word +=chr(65)
            elif(ord(w)==122):
                word +=chr(65)
            else:
                if(chr((ord(w)+1)) in ['a','o','u','i','e']):
                    word += chr(ord(w)+1).upper()
                else:
                    word += chr(ord(w)+1)
        else:
            word +=w
    return word

print(change("czderbyte"))