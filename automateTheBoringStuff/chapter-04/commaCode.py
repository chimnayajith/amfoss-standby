def commaCode(x):
    if len(x)==0:
        return None
    else:
        res=""
        for i in range(len(x)-1):
            res+=x[i]+ ", "
        res+='and ' + x[-1]
    return res