def most_frequent(str):
    freq={}
    final={}
    for char in str:
        if char in final:
            final[char]+=1
        else:
            freq[char]=1
            freq={char:freq[char]}
            final={**final,**freq}
    return final
s=input("Please enter a string:")
f=most_frequent(s)
f1=sorted(f.items(),key=lambda x:x[1],reverse=True)
for i in f1:
    print("{}={}".format(i[0],i[1]))
