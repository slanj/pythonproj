import spacy

# Загрузка английской NLP-модели
nlp = spacy.load('en_core_web_lg')

# Текст для анализа
text = """London is the capital and most populous city of England and
the United Kingdom.  Standing on the River Thames in the south east
of the island of Great Britain, London has been a major settlement
for two millennia. It was founded by the Romans, who named it Londinium.
"""

# Парсинг текста с помощью spaCy. Эта команда запускает целый конвейер
doc = nlp(text)

# в переменной 'doc' теперь содержится обработанная версия текста
# мы можем делать с ней все что угодно!
# например, распечатать все обнаруженные именованные сущности
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")

