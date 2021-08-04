def duplicate_count(text):
    text=text.lower()
    spis = {}
    for sg in text:
        if sg in spis:
            spis[sg] +=1
        else:
            spis[sg] = 1
    k = 0
    for j in spis:
        if spis[j] > 1:
            k += 1
    return k


print(fun('ABBA'))



