import nltk
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

DOC_PATTERN = r'[\w_\s]+/[\w\s\d\-]+\.TXT'
CAT_PATTERN = r'([\w_\s]+)/.*'

corpus = CategorizedPlaintextCorpusReader('ENGLISH', DOC_PATTERN, cat_pattern= CAT_PATTERN)

print(corpus.categories())
print(corpus.fileids()[100:110])
print(corpus.words())
