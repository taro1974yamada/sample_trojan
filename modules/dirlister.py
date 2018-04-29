
# coding: utf-8

# In[1]:




import os

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)

