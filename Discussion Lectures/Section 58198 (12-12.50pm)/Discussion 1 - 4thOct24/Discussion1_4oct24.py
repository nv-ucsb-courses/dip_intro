# ECE 178 – Discussion 1
# Introduction to digital image processing
# 4th October 2024
# Hardik Prajapati

from PIL import Image, ImageFilter
import cv2
import numpy as np

# Import necessary libraries

def main():
    # Load an image using Pillow
    pil_image = Image.open('example.jpg')
    pil_image.show(title='Original Image (Pillow)')

    # Check the size of the image
    width, height = pil_image.size
    print(f"Original Image Size: {width}x{height}")

    blurred_image = pil_image.filter(ImageFilter.BLUR)
    blurred_image.show(title='Blurred Image (Pillow)')

    # Convert Pillow image to OpenCV format
    open_cv_image = np.array(pil_image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR
    
    # CV_IMAGE=cv2.imread('example.jpg')

    # Display the image using OpenCV
    cv2.imshow('Original Image (OpenCV)', open_cv_image)
    cv2.waitKey(0)

    # Convert the image to grayscale using OpenCV
    gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image (OpenCV)', gray_image)
    cv2.waitKey(0)

    # Apply a Gaussian blur using OpenCV
    blurred_image_cv = cv2.GaussianBlur(open_cv_image, (15, 15), 0)
    cv2.imshow('Blurred Image (OpenCV)', blurred_image_cv)
    cv2.waitKey(0)

    # Apply a Gaussian blur using OpenCV
    blurred_image_cv2 = cv2.GaussianBlur(open_cv_image, (30, 30), 0)
    cv2.imshow('Blurred Image -2 (OpenCV)', blurred_image_cv2)
    cv2.waitKey(0)

    # Clean up and close windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    # Instructions to install the necessary libraries
    print("To install the necessary libraries, run the following commands in your terminal or command prompt:")
    print("pip install pillow")
    print("pip install opencv-python")

    main()