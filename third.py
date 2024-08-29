def format_string(s, operations):
    def _uppercase(str):
        strmod=""
        for i in range(len(str)):
            if s[i]==" ":
                strmod=strmod+" "
            else:
                strmod=strmod+chr(ord(s[i])-32)
        return strmod
    
    def _reverse(str):
        strmod=""
        for i in range(len(str)-1,-1,-1):
            strmod=strmod+str[i]
        return strmod
    
    def _capitalize(str):
        strmod=""
        strmod=strmod+chr(ord(s[0])-32)
        for i in range(1,len(str)):
            strmod=strmod+str[i]
        return strmod
    
    for op in operations:
        if op=='uppercase':
            s=_uppercase(s)
        elif op=='reverse':
            s=_reverse(s)
        elif op=='capitalize':
            s=_capitalize(s)
    
    return s




s = "hello world"

operations = ['uppercase', 'reverse']
format_string(s, operations)
print(format_string(s, operations))
