import json;

s = 0;
with open('example3.txt','r') as f:
    s = f.read()

book = json.loads(s)
print(book,type(book))
print(book['def']['phone'])