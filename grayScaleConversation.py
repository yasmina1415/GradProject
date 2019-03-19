
#.........................Gray scale conversation..........................................#
def grayScaleConversation(image):
    import numpy
    import cv2
    from matplotlib import pyplot as plt
    # To read the original image, simply call the imread function of the cv2 module,
    # passing as input the path to the image, as a string.
    # the imread function will have the channels stored in BGR (Blue, Green and Red) order by default.


    # Next, we need to convert the image to gray scale. To do it, we need to call the cvtColor function,
    # which allows to convert the image from a color space to another.
    # As first input, this function receives the original image. As second input,
    # it receives the color space conversion code. Since we want to convert our original image from the BGR color space to gray,
    # we use the code COLOR_BGR2GRAY.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # and background to ensure foreground is now "white" and
    # the background is "black"
    gray = cv2.bitwise_not(gray)
    # threshold the image, setting all foreground pixels to
    # 255 and all background pixels to 0
    #A thresholding operation (Lines 23 and 24) is then applied to binarize the image:
    (thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = 127
    binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
    # Now, to display the images, we simply need to call the imshow function of the cv2 module.
    # This function receives as first input a string with the name to assign to the window, and as second argument the image to show.
    # We will display both images so we can compare the converted image with the original one.
    #cv2.imshow('Original image',image)
    #cv2.imshow('Gray image', gray)
    #cv2.imshow('binary image', binary)
    cv2.imwrite('binary_image.png', binary)
    return binary



