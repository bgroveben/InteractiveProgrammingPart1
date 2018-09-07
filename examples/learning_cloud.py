#!/usr/bin/env python

# https://github.com/amueller/word_cloud/blob/master/examples/simple.py

"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

import os

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
# text = open(path.join(d, 'constitution.txt')).read()
text = open(path.join(d, 'mly_book/mly04.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(max_font_size=45, background_color='white', colormap='plasma').generate(text)
# colormap = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
