# -*- coding: utf-8 -*-
"""

Super Project Group 5

Daniel Molar Hurtado

Nicholas Hayes

Rebeca Lopez Valerio

EE104 Super Project Option 4

"""
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
TestImage='1stShip'

print('\n')

#Plot Original Image
print("The Image Chosen Is:",TestImage +'.png\n')

OriginalImage = mpimg.imread(TestImage +'.png')

plt.figure(1)

plt.subplot(221)

plt.imshow(OriginalImage)

#Convert Image
img = Image.open(''+ TestImage +'.png')

new_width  = 32

new_height = 32

img = img.resize((new_width, new_height), Image.ANTIALIAS)

img.save(TestImage+'Converted.png') 

#Plot Converted Image
print("Converted Image Name:",''+ TestImage +'Converted.png\n')

ConvertedImage = mpimg.imread(''+ TestImage  +'Converted.png')

plt.subplot(222)

plt.imshow(ConvertedImage)

plt.show()