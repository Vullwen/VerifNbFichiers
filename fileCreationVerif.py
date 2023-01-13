import time
import os

nb = input('How many files should be processed? ')
nb = int(nb)

# Set the directory containing the PDF files
input_directory = 'C://Users//cpinquier//Documents//taf//input'

while True:
	#count the number of files in the input directory
	pdf_filenames = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]
	act = len(pdf_filenames)

	#say the progress in percentage
	print('Progress: {}/{} - {}%, {}'.format(act, nb, round(act/nb*100, 2), time.strftime('%H:%M:%S')))
	#stop the loop when the number of files in the input directory is equal to the number of files to process
	if act == nb:
		break
	
	#wait 5 seconds
	time.sleep(5)