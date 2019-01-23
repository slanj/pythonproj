import spacy
import textacy.extract

# Загрузка английской NLP-модели
nlp = spacy.load('en_core_web_lg')

# Текст для анализа
text = """London is the capital and most populous city of England and  the United Kingdom.
Standing on the River Thames in the south east of the island of Great Britain,
London has been a major settlement  for two millennia.  It was founded by the Romans,
who named it Londinium.
"""

# Анализ
doc = nlp(text)

# Извлечение полуструктурированных выражений со словом London
statements = textacy.extract.semistructured_statements(doc, "London")

# Вывод результатов
print("Here are the things I know about London:")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {subject}, {verb}, {fact}")