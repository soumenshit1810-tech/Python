letter = '''Dear <|NAME|>,
            you are selected!
            <\DATE|>'''

print(letter.replace("<|NAME>","Harry").replace("<|DATE|","24 september 2050"))