print ("Jan's Citation Machine")
print ("Press ENTER key to continue")
start_type = input()

if start_type == (""):
	print ("What's the Source? 'URL, Book, Etc.'")
	url = input()

if url == url:
	print ("What's the date? 'Year'")
	date = input()

if date == date:
	print ("Who wrote/created the source? 'Name'")
	author = input()

if author == author:
	print ("What's the title of the source?")
	title = input()	

if title == title:
	print ("What's the name of the association/company that made the source?")
	comp = input()

if comp == comp:
	print ("You want to write an annotation? If not, press ENTER to continue.")
	next = input()

if next == next:
	print ("Processed Bibliography... Press ENTER to view.")
	finish = input()

if finish == finish:
	print (author + "." + " " + title + "." + " " + comp + (".") + " " + date + (",") + " " + url + " " + next)
