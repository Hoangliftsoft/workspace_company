s = 'Pham Quoc Hoang Quoc Hoang'

print(s.split(maxsplit=1))              # tách ra
print(s.rsplit(maxsplit=1))
print(s.splitlines(True))

# print(s.partition('Quoc'))            # vách ngăn
# print(s.rpartition('Quoc'))

# print(s.count('Quoc'))

# print(s[10:15])
# print(s.startswith('Hoang',10,15))    

# print(s.endswith('Pham'))

# print(s.find('Q',6,15))
# print(s.rfind('Q',6,15))

# print(s.index('Q',6,15))
# print(s.rindex('Q',6,15))

# print(s.isupper())
# print(s.islower())
# print(s.istitle())
# print(s.isidentifier())
# print(s.isdigit())
# print(s.isspace())
# import keyword
# print(keyword.iskeyword('def'))