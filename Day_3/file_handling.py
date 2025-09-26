#more: r- read, w- write,a- append

#open file
file = open('example.txt','r')

# read file
file = open('example.txt','r')
content = file.read()
print(content)
file.close()

print('`````````````````````````````````````')

file = open('example.txt','r')
constent = file.readline()
print(constent)
file.close()

print('`````````````````````````````````````')

file = open('example.txt','r')
constent = file.readlines() # converts to a list of strings
print(constent)
file.close()

print('`````````````````````````````````````')

file = open('example2.txt','w') # write mode
file.write('Hello GM!!!!!!!') # overwrites file if anything already written there
file.close()

file = open('example2.txt','a') # append Mode
file.write(f"\nSecond Line !!!!!!")
file.close()
print('`````````````````````````````````````')
print('`````````````````````````````````````')
print('`````````````````````````````````````')
print('`````````````````````````````````````')
#with statement
with open('example.txt','r') as f1:
    c = f1.read()
    print(c)
