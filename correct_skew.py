#................................skew-correction...............................................................#
def correct_skew(image,gray):
    import numpy as np
    import argparse
    import cv2

    #Trail to use terminal arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-image", required=True, help="path to input image file")
    # args = vars(ap.parse_args())
    # # load the image from disk
    # #The image is then loaded from disk on Line 13.
    # IMG = args["image"]
    # image = cv2.imread("images/IMG")


    #Given this thresholded image,
    # we can now compute the minimum rotated bounding box that contains the text regions:
    # grab the (x, y) coordinates of all pixel values that
    # are greater than zero, then use these coordinates to
    # compute a rotated bounding box that contains all
    # coordinates
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle)

    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
        angle = -angle

    # rotate the image to deskew it
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(gray, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)



    #Finally, we display the results to our screen:
    #Text skew correction with OpenCV and Pytho

    # draw the correction angle on the image so we can validate it
    cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # show the output image
    print("[INFO] angle: {:.3f}".format(angle))
    cv2.imshow("Input", gray)
    cv2.imshow("Rotated", rotated)



    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    image[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst',image)
    if cv2.waitKey(0) & 0xff == 27:
     return dst