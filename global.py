
def file_write():

	sample_text = 'write this sentence to file\n'
	write = open ('exam.txt', 'w');
	write.write(sample_text)
	write.close()

	# if the file is not closed after write, the following read does not reture any value

	readMe = open ('exam.txt', 'r').read()
	print (readMe)


file_write()