def chng(a):
    if(a[-3]=="ing"):
        a+="ly"
    else:
        if(len(a)>3):
            a+="ing"
    return a
print(chng("struing"))
