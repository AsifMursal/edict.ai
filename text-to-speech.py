# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = '''We propose a novel network that generates a video corresponding to a given description. The learning framework
of our network is established on the basic concept that connected frames of a video have substantial continuity. If we
can create one high-quality video frame, it will be easier
to create a linked frame because they are related. Rather
than first finding a mapping function between the text and
all video frames, we train our network with respect to one image and gradually extend it to longer frames (Figure 1). Our
model call this scheme as TiVGAN, which stands for Text-toImage-to-Video Generative Adversarial Network framework.
In the process of progressively learning to generate a large
number of adjacent frames, TiVGAN can learn to create long
consecutive scenes. Our extensive experimental results show
that our model not only produces an accurate video for a given
text but also produces qualitatively and quantitatively sharper
and better results than those presented in other comparable
works.
'''
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("mpg321 welcome.mp3")