#new version do Change letters..!

def change_let(str):

    word=' '
    str= str.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    voyel = "aeoui"
    for w in str:
        if ( w in alpha):

            if(w=='z' or w=='Z'):
                word +=alpha[0].upper()
            elif ( (alpha[alpha.index(w)+1]) in ['a','o','u','i','e']):
                word += alpha[alpha.index(w)+1].upper()
            else:
                word += alpha[alpha.index(w)+1]
        else:
            word += w
    return (word)


print(change_let("DEs#46540%--@$zefdnth"))