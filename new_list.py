#for
s = [2, 4, 9, 16, 25]
for i in range(len(s)):
    s[i] = s[i]**2
print(s)
#map
s = [2, 4, 9, 16, 25]
print(list(map((lambda x: x**2),s)))
#gen
s = [2, 4, 9, 16, 25]
print([i**2 for i in s])
