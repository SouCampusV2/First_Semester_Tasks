import re

def findP(text):
    charac = r'\b[P]\w+\b'
    result = re.findall(charac, text)
    words = set(word for word in result if word)
    
    return words

def findWar(text):
    charac = r'\w*(?:war|wra|rwa|raw|arw|awr)\w*'
    result = re.findall(charac, text)
    words = set(word for word in result if word)
    
    return words

def findWithout(text):
    charac = re.compile(r'\b[^eiokl\s]+\b', re.IGNORECASE)
    result = charac.findall(text)

    return result   
    
fl = 'war_and_peace.txt' 
with open(fl, 'r', encoding='utf-8') as fl:
    fileTxt = fl.read().strip()
    

print("\n\n\n--------------------------------------------------")
print("------------------Words P------------------------")
print("\n\n\n--------------------------------------------------\n")
print(findP(fileTxt))
print("\n\n\n--------------------------------------------------")
print("----------------Words War etc...-----------------")
print("\n\n\n--------------------------------------------------\n")
print(findWar(fileTxt))
print("\n\n\n--------------------------------------------------")
print("------------Without letters e,i,o,k,l-------------")
print("\n\n\n--------------------------------------------------\n")
print(findWithout(fileTxt))