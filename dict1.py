import json
import difflib as db

data = json.load(open("./data.json"))

def means(word):
    if word in data:
        return data[word]
    elif len(db.get_close_matches(word,data.keys()))>0:
        ch = input("Word not found. Did you mean %s instead? Enter Y for yes, N for no - "%db.get_close_matches(word,data.keys())[0])
        if(ch.lower()=="y"):
            w1 = db.get_close_matches(word,data.keys())[0]
            return data[w1]
        if(ch.lower()=="n"):
            return "Please recheck the word."
        else:
            return "Incorrect Input Type."
    else:
        return "Please recheck the word."

word = input("Enter Word : ")
word = word.lower()
output = means(word)
ctr = 1
if(type(output)==list):
    for x in output:
        print("%d"%ctr,x)
        ctr+=1
else:
    print(output)
