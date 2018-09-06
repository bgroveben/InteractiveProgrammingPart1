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

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
# text = open(path.join(d, 'constitution.txt')).read()
text = open(path.join(d, 'wordlist.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# lower max_font_size
# From the matplotlib colormap docs:
# colormap = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
wordcloud = WordCloud(max_font_size=45,background_color="cornsilk",colormap="plasma").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
