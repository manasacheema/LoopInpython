a="sowji12"
i=0
str_count=0
digit=0
while i<len(a):
    if type(a[i])==str:
        str_count=str_count+1
    elif type(int(a[i]))==int:
        digit=digit=+1
    i=i+1
print("letters are",str_count)
print("digits are",digit)
