def triple_x(s):
    if s.count('x') >= 3 :
        k=0
        for i in range(len(s)):
            if s[i]=='x':
                k+=1
            if k==1 and s[i+1]=='x' and s[i+2]=='x':
                return 'true'
                break
            elif k==1:
                return 'false'
                break
    return 'false'
print(triple_x('softx kitty, warm kitty, xxxxx'))