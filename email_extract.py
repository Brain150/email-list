import re

with open ('mbox-short.txt') as han :
    lines = han.readlines()
#print(lines)


## [.] exact character: hier MOET dus een . staan
## {m} (cijfer tussen {} zorgt dat de voorgaande RE precies m maal voorkomt (in dit geval: de . mag 1x voorkomen op deze plek ; voorkomt hier mailadresssen zonder volledig domein 
emails = re.findall("[\w\.-]+@[\w\.-]+[.]{1}[\w\.-]+", str(lines)) ## geeft list met alles erin wat x@x.x bevat (ook als er na de @ meer .x.x.x is!) en heeft \n, <,> erafgehaald ; str omdat RE een verzameling STRINGS is
#print(emails)

## check & remove duplicates in list 'emails'
## list(dict.fromkeys(emails)) maakt een dictionary van alleen keys, geen values: unieke keys, want dictionary kan geen duplicaten hebben; verandert de dictionary weer naar list
## gebruik gemaakt van een functie met return, zodat je nog meer kunt met het resultaat

def single(emails):
  return list(dict.fromkeys(emails))

unique = single(emails) ## call function

## unieke emails naar nieuwe file schrijven
with open ("email.txt", "w" ) as file1 :
    for line in unique :
        file1.write(line + "\n") ## \n zodat elk item op een nieuwe regel geschreven wordt


'''
## andere schrijfopdracht (nog niet getest)

new_file = open ("newfile.txt", mode = "a+", encoding = "utf-8")
new_file.writelines(email)
for line in new_file :
    print(line)
new_file.close()

'''
