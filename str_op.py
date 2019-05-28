s = "У лукоморья 123 дуб зеленый 456"
print("Позиция буквы 'я': ",s.find('я'))
print("Сколько букв 'у': ",s.count('у'))
print(s.isalpha())
if s.isalpha() == False:
    print(s.upper())
l = int(len(s))
if l > 4:
    print(s.lower())
print(s.replace('У','О'))
