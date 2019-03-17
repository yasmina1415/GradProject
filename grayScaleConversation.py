
#.........................Gray scale conversation..........................................#
def grayScaleConversation():
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
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # Now, to display the images, we simply need to call the imshow function of the cv2 module.
    # This function receives as first input a string with the name to assign to the window, and as second argument the image to show.
    # We will display both images so we can compare the converted image with the original one.
    cv2.imshow('Original image',image)
    cv2.imshow('Gray image', gray)
