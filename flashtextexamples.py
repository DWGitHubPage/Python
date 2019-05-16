# Python3.7.3
from flashtext import KeywordProcessor
import pprint as pp


# Find keywords.

keyword_processor = KeywordProcessor()

keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('\I love the Big Apple'
                                                    '\and Bay Area.')
print(keywords_found)
                                                    

# Replace keywords.
keyword_processor.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor.replace_keywords('I love Big Apple'
                                                  'and new delhi.')
print(new_sentence)


# Case sensitive example.

keyword_processor = KeywordProcessor(case_sensitive=True)
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love big aapple and Bay Area.')
print(keywords_found)


# Span of keywords extracted.

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('\I love Big Apple'
                                                    '\and Bay Area.', span_info=True)
print(keywords_found)


# Get extra information with keywords extracted.
# replace_keywords feature won't work with this.

kp = KeywordProcessor()
kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
kp.add_keyword('Delhi', ('Location', 'Delhi'))

print(kp.extract_keywords('Taj Mahal is in Delhi.'))


# No clean name for Keywords.

keyword_process = KeywordProcessor()
keyword_processor.add_keyword('Big Apple')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('\ I love Big Apple'
                                                    '\ and Bay Area.')
print(keywords_found)


# Add multiple keywords simultaneously.

keyword_process = KeywordProcessor()
keyword_dict = {
    "java": ["java_2e", "java programming"],
    "product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)
keyword_processor.add_keywords_from_list(["java", "python"])

print(keyword_processor.extract_keywords("\I am a product manager"
                                         "\for a java_2e platform"))


# To remove keywords.

keyword_processor = KeywordProcessor()
keyword_dict = {
    "java": ["java_2e", "java programming"],
    "product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)

print(keyword_processor.extract_keywords("\I am a product manager for"
                                         "\a java_2e platform"))

keyword_processor.remove_keyword('java_2e')
keyword_processor.remove_keywords_from_dict({"product management": ["PM"]})
keyword_processor.remove_keywords_from_list(["java programming"])

print(keyword_processor.extract_keywords("\I am a product manager for"
                                         "\a java_2d platform"))


# Check Number of terms in KeywordProcessor.

keyword_processor = KeywordProcessor()
keyword_dict = {
    "java": ["java_2e", "java programming"],
    "product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)

print(len(keyword_processor))


# To check if term is present in KeywordProcessor.

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('j2ee', 'Java')

print('j2ee' in keyword_processor)
print(keyword_processor.get_keyword('j2ee'))

keyword_processor['color'] = 'color'

print(keyword_processor['color'])


# To set or add characters as part of word characters.

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword("Big Apple")

print(keyword_processor.extract_keywords("I love the Big Apple/Bay Area."))

keyword_processor.add_non_word_boundary("/")

print(keyword_processor.extract_keywords("I love the Big Apple/Bay Area."))


# Searching for a single word in a document.
document = """Batman is a fictional superhero appearing in American comic books published by DC Comics. The character was created by artist Bob Kane and writer Bill Finger,[4][5] and first appeared in Detective Comics #27 (1939). Originally named the "Bat-Man", the character is also referred to by such epithets as the Caped Crusader, the Dark Knight, and the World's Greatest Detective.[6]

Batman's secret identity is Bruce Wayne, a wealthy American playboy, philanthropist, and owner of Wayne Enterprises. After witnessing the murder of his parents Dr. Thomas Wayne and Martha Wayne as a child, he swore vengeance against criminals, an oath tempered by a sense of justice. Bruce Wayne trains himself physically and intellectually and crafts a bat-inspired persona to fight crime.[7]

Batman operates in the fictional Gotham City with assistance from various supporting characters, including his butler Alfred, police commissioner Gordon, and vigilante allies such as Robin. Unlike most superheroes, Batman does not possess any superpowers; rather, he relies on his genius intellect, physical prowess, martial arts abilities, detective skills, science and technology, vast wealth, intimidation, and indomitable will. A large assortment of villains make up Batman's rogues gallery, including his archenemy, the Joker.

The character became popular soon after his introduction in 1939 and gained his own comic book title, Batman, the following year. As the decades went on, differing interpretations of the character emerged. The late 1960s Batman television series used a camp aesthetic, which continued to be associated with the character for years after the show ended. Various creators worked to return the character to his dark roots, culminating in 1986 with The Dark Knight Returns by Frank Miller. The success of Warner Bros.' live-action Batman feature films have helped maintain the character's prominence in mainstream culture.[8]

An American cultural icon, Batman has garnered enormous popularity and is among the most identifiable comic book characters. Batman has been licensed and adapted into a variety of media, from radio to television and film, and appears on various merchandise sold around the world, such as toys and video games. The character has also intrigued psychiatrists, with many trying to understand his psyche. In 2015, FanSided ranked Batman as number one on their list of "50 Greatest Super Heroes In Comic Book History".[9] Kevin Conroy, Bruce Greenwood, Peter Weller, Anthony Ruivivar, Jason O'Mara, and Will Arnett, among others, have provided the character's voice for animated adaptations. Batman has been depicted in both film and television by Lewis Wilson, Robert Lowery, Adam West, Michael Keaton, Val Kilmer, George Clooney, Christian Bale, and Ben Affleck. """

processor = KeywordProcessor()
processor.add_keyword('batman')
found = processor.extract_keywords(document)
print(found)
print('\n')

processor.add_keywords_from_dict({'batman':['batman','bruce wayne']})
found = processor.extract_keywords(document, span_info=True)
pp.pprint(found)

