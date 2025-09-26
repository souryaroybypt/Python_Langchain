import json;
book = {}
book['abc'] = {
    'name':'abc',
    'address':'1 red street NY',
    'phone': 9024389438
}

book['def'] = {
    'name':'def',
    'address':'2 red street NY',
    'phone': 9014389438
}

book['ghi'] = {
    'name':'ghi',
    'address':'12 red street NY',
    'phone': 9021389438
}

# print(book)

s = json.dumps(book) # dictionary to json
print(s)

with open('example3.txt','w') as f1:
    f1.write(s)
