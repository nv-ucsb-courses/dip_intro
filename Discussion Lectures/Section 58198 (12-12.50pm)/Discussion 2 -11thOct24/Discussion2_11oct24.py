from PIL import Image
import numpy as np

#working with pillow, (x,y) is the coordinate of the pixel, whre x is the width and y is the height
print("Pillow")
pil_m = Image.open("homework_1.jpg")
print(pil_m.getpixel((200,300)))
pil_m.show()

im=pil_m.load()
for x in range(pil_m.width): 
    im[x, 60] = (0, 0, 0)
    im[x, 61] = (0, 0, 0)
    im[x, 62] = (0, 0, 0)


pil_m.show()
print(pil_m.getpixel((0,61)))

#working with numpy, (x,y) is the coordinate of the pixel, whre x is the height and y is the width
print("Numpy")
pil_m = Image.open("homework_1.jpg")
np_m = np.array(pil_m)
print(np_m[200,300])
for x in range(np_m.shape[1]):
    np_m[60,x] = [0,0,0]
    np_m[61,x] = [0,0,0]
    np_m[62,x] = [0,0,0]
np_m = Image.fromarray(np_m)
np_m.show()
print(np_m.getpixel((61,0)))

# convert an image to grayscale
pil_m = Image.open("homework_1.jpg").convert('L')
pil_m.show()
np_m = np.array(pil_m)
Rotate_180 = np.zeros((np_m.shape[0],np_m.shape[1]))

# implement function to rotate an image by 180 degrees
for x in range(np_m.shape[0]): # iterate over the rows
    for y in range(np_m.shape[1]): # iterate over the columns
        new_x = np_m.shape[0]-1-x # calculate the new x coordinate, -1 because the index starts from 0
        new_y = np_m.shape[1]-1-y # calculate the new y coordinate, -1 because the index starts from 0
        Rotate_180[new_x,new_y] = np_m[x,y]

Rotate_180 = Image.fromarray(Rotate_180)
Rotate_180.show()
