from PIL import Image
import numpy as np
import math

def histEqualization(img):
    new_img = img.copy() # make a copy of the image
    new_im = new_img.load() # load the image pixels

    width, height = img.size # get the width and height of the image

    hist = np.zeros(256)
    cummulative_hist = np.zeros(256) # initialize the cumulative histogram
    cdf = np.zeros(256) # initialize the cdf
    new_map = np.zeros(256) # initialize the new mapping

    for y in range(height):
        for x in range(width):
            hist[img.getpixel((x,y))] += 1

    cummulative_hist[0] = hist[0]
    for i in range(1,256):
        cummulative_hist[i] = cummulative_hist[i-1]+hist[i]
        cdf[i] = cummulative_hist[i]/(width*height)
        new_map[i] = math.floor(cdf[i]*255)      
    
    # apply the equalization
    for y in range(img.height):
        for x in range(img.width):
            new_im[x,y] = int(new_map[img.getpixel((x,y))])
    return new_img

def convolution(img, filter):
    # filter is a 3x3 matrix
    weights_sum = 0
    for i in range(3):
        for j in range(3):
            weights_sum += filter[i][j]
    if weights_sum == 0:
        weights_sum = 1
    numpy_img = np.array(img)
    filtered_img = numpy_img.copy()
    neighborhood_window = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    
    for row in range(1,img.height-1):
        for col in range(1,img.width-1):
            sum = 0
            for neigh_x,neigh_y in neighborhood_window:
                neigh_row = row+neigh_x
                neigh_col = col+neigh_y
                sum += numpy_img[neigh_row,neigh_col]*filter[neigh_x+1][neigh_y+1]
            filtered_img[row,col] = sum/weights_sum

    return Image.fromarray(filtered_img)

orig_img = Image.open("HW3_image2.tiff") # open the image
gray_img = orig_img.convert('L') # convert the image to grayscale
histEqualization_img = histEqualization(gray_img) # apply the histogram equalization
histEqualization_img.show() # show the image

# # histogram equalization on rgb image
# r_img, g_img, b_img = orig_img.split() # split the image into r,g,b channels
# r_img = histEqualization(r_img) # apply histogram equalization on r channel
# g_img = histEqualization(g_img) # apply histogram equalization on g channel
# b_img = histEqualization(b_img) # apply histogram equalization on b channel
# histEqualization_rgb_img = Image.merge('RGB', (r_img, g_img, b_img)) # merge the r,g,b channels
# histEqualization_rgb_img.show() # show the image

# convolution
filter = [[-1,0,1],[-1,0,1],[-1,0,1]]
conv_img = convolution(histEqualization_img, filter)
conv_img.show() # show the image
