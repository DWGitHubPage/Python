# Python3.7.3
from flashtext import KeywordProcessor


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

