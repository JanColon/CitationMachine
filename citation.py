print ("Jan's Citation Machine")
print ("Press ENTER key to continue")
start_type = input()

#The actual source of the citation 
if start_type == (""):
	print ("What's the Source? 'URL, Book, Etc.'")
	url = input()
#The date of the source
if url == url:
	print ("What's the date? 'Year'")
	date = input()

#The author/creator of the source
if date == date:
	print ("Who wrote/created the source? 'Name'")
	author = input()

#The source's title
if author == author:
	print ("What's the title of the source?")
	title = input()	

#The publisher of the source
if title == title:
	print ("What's the name of the association/company that made the source?")
	comp = input()

#An optional annotation for the citation
if comp == comp:
	print ("You want to write an annotation? If not, press ENTER to continue.")
	next = input()

#Just filler
if next == next:
	print ("Processed Bibliography... Press ENTER to view.")
	finish = input()

###--The finished citation--###
if finish == finish:
	print (author + "." + " " + title + "." + " " + comp + (".") + " " + date + (",") + " " + url + " " + next)
