# -*- coding: utf-8 -*-
"""image_assignment_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j1xbeRI1K85xOQ6jQe83yxQNbK7hUaP_
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

main_image = cv2.imread('F:/4.1/CSE 4128 Image Lab/lab1/lena.png',cv2.IMREAD_GRAYSCALE)

plt.title("Fig 2.     : Original Image")
plt.imshow(cv2.cvtColor(main_image,cv2.COLOR_BGR2RGB))
plt.show()
plt.savefig("Original Image")



#mean kernel function

kernel_size = 3
kernel = np.ones((kernel_size,kernel_size))

n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum/ np.sum(kernel)
    
from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))


plt.title("Fig 2.     : Mean implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()



#meadian kernel function

kernel_size = 5
n = (kernel_size -1)//2
image_size = 420
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    kr_value = []
    for i in range(kernel_size):
      for j in range(kernel_size):
        kr_value.append(image[x-i-n,y-j-n])
    #kr_value.sort()
    #mid = len(kr_value) //2
    mid = np.median(kr_value)
    #print(mid)
    #result[x,y] = kr_value[mid]
    #print(kr_value[mid])
    result[x,y] = mid


from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))

plt.title("Fig 2.     : Median implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()

#--------------CV2 implemantation ---------------
'''image_size = 420
image = cv2.resize(main_image,(image_size,image_size))
cv_output = cv2.medianBlur(image,3)

plt.title("median CV2 output")
plt.imshow(cv2.cvtColor(cv_output,cv2.COLOR_BGR2RGB))
plt.show()'''



#----------Laplacian Filter ------------

kernel = np.array(([0,-1,0],[-1,4,-1],[0,-1,0]), np.float32)
kernel

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
#result = rescale_intensity(result, in_range=(0, 255))

cv2.imwrite("Laplacian.jpg", result)
plt.title("Fig 2.     : Laplacian implementation output")
plt.imshow(result,'gray')
plt.show()


'''#----------Laplacian CV2 ------------
src = cv2.GaussianBlur(main_image, (3, 3), 0)
#cv_laplacian = cv2.Laplacian(src,cv2.CV_16S,3) 
cv_laplacian = cv2.Laplacian(src,2,3)
abs_dst = cv2.convertScaleAbs(cv_laplacian) 

plt.title("Laplacian CV2 output")
plt.imshow(cv2.cvtColor(abs_dst,cv2.COLOR_BGR2RGB))
plt.show()'''



# -----------sobel------

#Vertical
kernel = np.array(([-1,0,1],[-2,0,2],[-1,0,1]), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))


plt.title("Fig 2.     : Sobel Vertical implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()


'''#-----------CV2 implementation------
sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,0,1,ksize=3)
abs_64 = np.absolute(sobel_64)
sobel_8u = np.uint8(abs_64)


plt.title("Sobel cv2 vertical output")
plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
plt.show()'''


#--------Horizontal-------
kernel = np.array(([-1,-2,-1],[0,0,0],[1,2,1]), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))


plt.title("Fig 2.     : Sobel Horizontal implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()

#------------Marge [(x**2+y**2)**1/2]-----
kernelx = np.array(([-1,-2,-1],[0,0,0],[1,2,1]), np.float32)
kernely = np.array(([-1,0,1],[-2,0,2],[-1,0,1]), np.float32)

kernel_size = kernelx.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sumx = 0
    sumy = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sumx+= kernelx[i,j]*image[x-i-n,y-j-n]
        sumy+= kernely[i,j]*image[x-i-n,y-j-n]
    result[x,y] =  np.sqrt(sumx**2+sumy**2)

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))

plt.title("Sobel marge implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()




'''#-----------CV2 implementation--
sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,1,0,ksize=3)
abs_64 = np.absolute(sobel_64)
sobel_8u = np.uint8(abs_64)


plt.title("Sobel cv2 horizontal output")
plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
plt.show()
'''



# -----------Prewitt---------

#Vertical
kernel = np.array(([-1,0,1],[-1,0,1],[-1,0,1]), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum
from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))


plt.title("Fig 2.     : Prewitt Vertical implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()


#-----------CV2 implementation------
#sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,0,1,ksize=3)
#abs_64 = np.absolute(sobel_64)
#sobel_8u = np.uint8(abs_64)


#plt.title("Sobel cv2 vertical output")
#plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
#plt.show()


#--------Horizontal-------
kernel = np.array(([-1,-1,-1],[0,0,0],[1,1,1]), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))

plt.title("Fig 2.     : Prewitt Horizontal implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()


#-----------CV2 implementation--
#sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,1,0,ksize=3)
#abs_64 = np.absolute(sobel_64)
#sobel_8u = np.uint8(abs_64)


#plt.title("Sobel cv2 horizontal output")
#plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
#plt.show()


# -----------Scharr---------

#Vertical
kernel = np.array(([-3,0,3],[-10,0,10],[-3,0,3]), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))


plt.title("Fig 2.     : Scharr Vertical implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()

#-----------CV2 implementation------
#sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,0,1,ksize=3)
#abs_64 = np.absolute(sobel_64)
#sobel_8u = np.uint8(abs_64)


#plt.title("Sobel cv2 vertical output")
#plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
#plt.show()


#--------Horizontal-------
kernel = np.array(([-3,-10,-3],[0,0,0],[3,10,3]), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))


plt.title("Fig 2.     : Scharr Horizontal implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()


#-----------CV2 implementation--
#sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,1,0,ksize=3)
#abs_64 = np.absolute(sobel_64)
#sobel_8u = np.uint8(abs_64)


#plt.title("Sobel cv2 horizontal output")
#plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
#plt.show()


# -----------Robert---------

#Vertical
kernel = np.array(([0,1],[-1,0] ), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))

plt.title("Fig 2.     : Robert Vertical implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()


#-----------CV2 implementation------
#sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,0,1,ksize=3)
#abs_64 = np.absolute(sobel_64)
#sobel_8u = np.uint8(abs_64)


#plt.title("Sobel cv2 vertical output")
#plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
#plt.show()


#--------Horizontal-------
kernel = np.array(([1,0],[0,-1]), np.float32)

kernel_size = kernel.shape[1]
n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))

plt.title("Fig 2.     : Robert Horizonl implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()


#-----------CV2 implementation--
#sobel_64 = cv2.Sobel(main_image,cv2.CV_64F,1,0,ksize=3)
#abs_64 = np.absolute(sobel_64)
#sobel_8u = np.uint8(abs_64)


#plt.title("Sobel cv2 horizontal output")
#plt.imshow(cv2.cvtColor(sobel_8u,cv2.COLOR_BGR2RGB))
#plt.show()


#----------gaussian----------

def guess_helper(x,y,sigma = 2):
    
  pi = math.pi
  pixel_value = (1/(2*pi*sigma**2))*np.exp(-(x*x+y*y)/(2*sigma*sigma))
  return pixel_value

kernel_size =7
guess_kernel = np.zeros((kernel_size, kernel_size),dtype='float32')
n = (kernel_size-1)//2
for i in range(kernel_size):
  for j in range(kernel_size):
    guess_kernel[i][j] = guess_helper((i-n),(j-n),sigma = 2 )

n = (kernel_size -1)//2
image_size = 220
image = cv2.resize(main_image,(image_size,image_size))
result = np.zeros((image_size,image_size),dtype = 'float32')
for x in range(image_size):
  for y in range(image_size):
    sum = 0
    for i in range(kernel_size):
      for j in range(kernel_size):
        sum+= guess_kernel[i,j]*image[x-i-n,y-j-n]
    result[x,y] = sum

from skimage.exposure import rescale_intensity
out = rescale_intensity(result, in_range=(0, 255))

plt.title("Fig 2.     : Gauss implementation output")
plt.imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
plt.show()