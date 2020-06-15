"""
websites for regular expressions:
https://regex101.com/ - teaches the syntax
https://regexone.com/ - test the code
"""
# import for regular expression
import re
# import for translating the language
from googletrans import Translator
# import for file rename
import os
# NOTE THE FILE RENAME ONLY WORKS ONCE DUE TO THE FILE HAVEN ALREADY BEEN CREATED THE SECOND TIME


translator = Translator()

lang = input('''
*****************************************************  
*    Choose a language from the following selection 
*    below:
*        Language      Code    
*    1.) French    -   fr
*    2.) Spanish   -   es                           
*    3.) Chinese   -  zh-CN                         
*    4.) Japanese  -   ja                           
*****************************************************\n
''')

while True:
	# get the file name input
	file_name = input('''\n
_______________________________________________________
	 Type in the name of the text file you want to translate:
------------------------------------------------------- \n
			''')
	try:
		# reads the file before translation
		with open(f'text_files/{file_name}', mode='r') as my_file:
			new_translation = translator.translate(my_file.readline(), dest=lang)
			new = new_translation.text
			print("\nThe Translation is:")
			print(new)
		# rewrites the file into the translated language, note! only works with french, japanese encoding is nonsense
			with open(f'text_files/translation.txt', mode='w') as my_file1:
				my_file1.write(new)
				break
	except (FileNotFoundError and NameError):
		print('File not found!')
		continue


# regular expression that removes the '.txt' and prints just the file name
pattern = re.compile(r"^[a-zA-Z0-9]*")
# store file name without '.txt' into the new name variable
new_name = pattern.findall(file_name)

# NOTE THE FILE RENAME ONLY WORKS ONCE DUE TO THE FILE HAVEN ALREADY BEEN CREATED THE SECOND TIME
# IN ORDER TO RUN AND CREATE A TEMPORARY TRANSLATION FILE COMMENT FROM LINE 46 DOWN TO LINE 54
#translate the file from "temp.txt" to the "old file name'_translation.txt
os.rename(f'text_files/temp.txt',f'text_files/{new_name[0]}_translation.txt')
