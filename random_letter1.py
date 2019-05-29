import random 
s = ["самовар","весна","лето"] 
p = random.choice(s) 
k = p.index(random.choice(p)) 
p1 = list(p) 
p1[k] = "?" 
p1 = "".join(p1) 
print(p1) 
l = input("Введите букву:\n") 
if l == p[k]: 
    print("Победа!\nСлово:\n",p) 
else: 
    print("Увы! Попробуй в другой раз.\nСлово:\n",p)
