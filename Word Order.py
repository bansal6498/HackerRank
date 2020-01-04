from collections import Counter
a = int(input())
arr=[]
str1=[]
str2=[]
for i in range(a):
    b=(input())
    arr.append(b)
str1=Counter(arr).keys()
str2=Counter(arr).values()
print(len(str1))
print(*str2, sep=' ')