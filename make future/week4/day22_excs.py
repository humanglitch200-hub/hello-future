#printing keys, values, all items 
country = dict(Nepal = 'ksathmandu', India = 'Delih', Canada = 'New york', Pakistan = 'Lahor', Japan = 'Tokiyo')
print(list(country))
print(country.values())
print(country.items())

#adding a country, updating the capital, and removing one with .pop()
country['Indonasia'] = 'Ball'
country['Indonasia'] = 'Bali'
country.pop('Nepal')
print( )
print(country.items())
print( )
#asking user a name of country and printing it's capital:
lookup = 'Nepal' # input("Enter a country name: ")
if lookup in country.keys(): 
    print(country.get(lookup))   
    
if lookup not in country.keys():
    print("Not found.") 
    
#Take a sentence, count each word using .get()
sentence = input("Enter a sentecne: ")
splitted = sentence.split()
counting = {}
for word in splitted:
    counting[word] = counting.get(word, 0) + 1 

print(counting.items())


#marging two dicts:
dict1 = {'Name': 'Kamlal'}
dict2 = {'Name': 'Ramlal'}
print(dict1.update(dict2))  #amaging prints None

