str = input()

k = ""
for v in str:
    if v.isupper():
        k += v.lower()
    else:
        k += v.upper();
        
print(k)