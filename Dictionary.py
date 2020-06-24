import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def searchDef(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff=0.5)) > 0:
        #yn = input("Did you mean %s ? Y/N : " % get_close_matches(w,data.keys())[0])
        for word in get_close_matches(w,data.keys()):
            yn = input("Did you mean %s ? Y/N : " % word)
            if yn == "Y" or yn == "y":
                return data[word]
            elif yn == "N" or yn == "n":
                continue
            else:
                return "Didn't understand"
        return "The word '%s' doesn't exist in this dictionary" % w
    else:
        return "The word '%s' doesn't exist in this dictionary" % w

search = input("Enter a word: ")
output = searchDef(search)
if type(output) == list:
    print("")
    for item in output:
        print(str(output.index(item)+1) + ". " + item)
else:
    print(output)
