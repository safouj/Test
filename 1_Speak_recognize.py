#!/usr/bin/env python
# coding: utf-8

# In[5]:


import speech_recognition as sr     
r = sr.Recognizer()                 # initialiser le recognizer
with sr.Microphone() as source:     # source {Microphone , audio files.}
    print("Speak Anything :")
    audio = r.listen(source)        # ecouter la source
    


# In[6]:


try:
    text = r.recognize_google(audio,  language="fr-FR" )  # ituliser le recognizer pour convertir au texte
    print("You said : {}".format(text))
except:
    print("Sorry could not recognize your voice")    # si pas reconnu


# In[ ]:




