import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

psy = pd.read_csv('./Youtube05-Shakira.csv')

words = ''
stopwords = set(STOPWORDS)

for comment in psy.CONTENT:
    tokens = str(comment).split()
    tokens = [i.lower() for i in tokens] 
    words += ' '.join(tokens) + ' '

wordcloud = WordCloud(stopwords=stopwords, min_font_size=10).generate(words)

plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout()
plt.show()