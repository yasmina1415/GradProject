#................................. image denoising .............................................................#
def imageDenoising(gray):
    import numpy
    import cv2
    from matplotlib import pyplot as plt
    # h : parameter deciding filter strength. Higher h value removes noise better, but removes details of image also(4 by try and error)
    # templateWindowSize : should be odd. (recommended 7)
    # searchWindowSize : should be odd. (recommended 21)
    Denoised = cv2.fastNlMeansDenoising(gray,None,4,7,21)
    cv2.imshow('Denoised image',Denoised )
    cv2.imwrite('Denoised.png', Denoised)
    return(Denoised)


