from googletrans import Translator

translate = Translator()

# user text input
word = input('''\n 
_______________________________________________________
        Type in the text you want to translate: 
------------------------------------------------------- \n
''')

# language dictionaries
languages = {
    'French':'fr',
    'Spanish':'es',
    'Chinese':'zh-CN',
    'Japanese':'ja'
}

while True:
    # user language input
    lang = input('''
*****************************************************  
*    Choose a language from the following selection *
*    below:                                         *
*    1.) French                                     *
*    2.) Spanish                                    *
*    3.) Chinese                                    *
*    4.) Japanese                                   *
*****************************************************\n
''')

    try:
        new_translation = translate.translate(word, languages.get(lang), 'en')
        new_translation.text
        print(new_translation.text)
        break

    except (KeyError and AttributeError):
        print('''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Please, enter a country code from the selection: 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n
''')
        continue
