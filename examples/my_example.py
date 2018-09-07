# https://github.com/amueller/word_cloud/blob/master/examples/simple.py

import os

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'wordlist.txt')).read()

# From the matplotlib colormap docs:
# colormap = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
wordcloud = WordCloud(max_font_size=45,background_color="cornsilk",colormap="plasma").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
