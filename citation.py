cite = None

print ("Jan's Citation Machine")
print ("Press ENTER key to continue")
start_type = input()

print ("What's the Source? 'URL, Book, Etc.'")
url = input()
print ("What's the date? 'Year'")
date = input()
print ("Who wrote/created the source? 'Name'")
author = input()
print ("What's the title of the source?")
title = input()	
print ("What's the name of the association/company that made the source?")
comp = input()
print ("You want to write an annotation? If not, press ENTER to continue.")
next = input()
print ("Citation complete! Hit ENTER to view. . .")
input()
    
cite = author + "." + " " + title + "." + " " + comp + (".") + " " + date + (",") + " " + url + " " + next + "\n" + "\n"
print ("\n" + cite)

if cite != None:
        print("Do you want to add this to a bibliography? 'Y or N'")
        bib_clar = input()

if bib_clar == "Y":
        bib = open("Bibliography.txt", "a")
        bib.write(cite)
        bib.close()
        print("Citation added! Check 'Bibliography.txt'")
else:
        pass
