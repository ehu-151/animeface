import os
from PIL import Image

path='pos/'
files = os.listdir(path)
text=open(r'positives.txt','a')
for file in files:
    im = Image.open(path+file)
    w, h = im.size
    s=str(path+file)+' 1 1 1 '+str(w)+' '+str(h)+'\n'

    text.write(s)