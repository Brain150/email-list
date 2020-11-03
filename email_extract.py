import re

with open ('mbox-short.txt') as han :
    lines = han.readlines()


# [.] exact character: hier MOET dus een . staan
# {m} (cijfer tussen {} zorgt dat de voorgaande RE precies m maal voorkomt (in dit geval: de . mag 1x voorkomen op deze plek ; voorkomt hier mailadressen zonder volledig domein 
# creates list with items containing x@x.x (with unlimited @x.x.x), remoes \n, <,>, etc.
# str() because RE is a collection of strings

emails = re.findall("[\w\.-]+@[\w\.-]+[.]{1}[\w\.-]+", str(lines)) 
#print(emails)

# check & remove duplicates in list 'emails'
# list(dict.fromkeys(emails)) generates a dictionary containing unique keys only (no values): dictionarie does not supoprt duplicates; changes dictionary back into list
# finction with a return defined and called: not really necessary, but it looks neater (other advantages?)

def single(emails):
  return list(dict.fromkeys(emails))

unique = single(emails) # call function

# wirte unique emails adresses to new file (automatically generated
with open ("email.txt", "w" ) as file1 :
    for line in unique :
        file1.write(line + "\n") # \n to write eacht item on a separate line


'''
## alternative for writing (not tested)
new_file = open ("newfile.txt", mode = "a+", encoding = "utf-8")
new_file.writelines(email, "\n")
for line in new_file :
    print(line)
new_file.close()

'''
