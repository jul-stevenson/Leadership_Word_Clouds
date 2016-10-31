#!/usr/bin/env python
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)

# Read texts
maleText = open(path.join(d, 'male.txt')).read()
femaleText = open(path.join(d, 'female.txt')).read()

# Generate wordcloud images
maleWordCloud = WordCloud().generate(maleText)
femaleWordCloud = WordCloud().generate(femaleText)

# Display images
plt.imshow(maleWordCloud)
plt.axis("off")
plt.show()
plt.imshow(femaleWordCloud)
plt.axis("off")
plt.show()
