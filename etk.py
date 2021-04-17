
input = "Batuq batuq BatuQ" # Reads all inputs up to the EOF character

input = input.replace('-',' ')#Replace (-, + .etc) expressions with a space character.
input = input.replace('.','')
input = input.replace(',','')
input = input.replace("`",'')
input = input.replace("'",'')

#input= input.split(' ') #if you use it, it will sort by the most repetitive words
dictionary = dict()
count = 0
for word in input:
    dictionary[word] = input.count(word)
    
print(dictionary)

#Writes the 5 most repetitive characters
for k in sorted(dictionary,key=dictionary.get,reverse=True)[:5]:
    print(k,dictionary[k])