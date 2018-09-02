import os

from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'med_school.txt')).read()

wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt

wordcloud = WordCloud(max_font_size=40, background_color='gray').generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
