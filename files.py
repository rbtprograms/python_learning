#jupyter notebooks can create text files super easily, pyhton can read them esasily.
#this reads a file
mytextfile.read()
#you need this one to reset the cursor to the beginning to read again
mytextfile.seek(0)
#the most interesting. breaks up text lines into a list, so you can process line by line
mytextfile.readlines()