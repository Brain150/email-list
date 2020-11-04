import re

with open ('mbox-short.txt') as han :
    lines = han.readlines()

# [.] exact character: in this case it has to be a . 
# {m} (number in between {} makes sure the RE appears exactly  m times (in this case: the . is allowed 1x at this position; prevents email addresses without a complete domain showing up 
# creates list with items containing x@x.x (with unlimited @x.x.x), removes \n, <,>, etc.
# str() because RE is a collection of strings
emails = re.findall("[\w\.-]+@[\w\.-]+[.]{1}[\w\.-]+", str(lines)) 
#print(emails)

# check & remove duplicates in list 'emails'
# list(dict.fromkeys(emails)) generates a dictionary containing unique keys only (no values): dictionary does not support duplicates; changes dictionary back into list
# function with a return defined and called: not really necessary, but it looks neater (other advantages?)
def single(emails):
  return list(dict.fromkeys(emails))
unique = single(emails) # call function

# write unique emails adresses to new file (will be generated automatically)
with open ("email.txt", "w" ) as file1 :
    for line in unique :
        file1.write(line + "\n") # \n to write each item on a separate line


'''.

## alternative for writing (not tested)
new_file = open ("newfile.txt", mode = "a+", encoding = "utf-8")
new_file.writelines(email, "\n")
for line in new_file :
    print(line)
new_file.close()

'''
