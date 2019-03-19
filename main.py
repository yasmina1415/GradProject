
import cv2
from grayScaleConversation import grayScaleConversation
from imageDenoising import imageDenoising
from correct_skew import correct_skew
from cornerDetection import cornerDetection
from segmentation import segmentation
from templateMatching import templateMatching


# To read the original image, simply call the imread function of the cv2 module,
# passing as input the path to the image, as a string.
# the imread function will have the channels stored in BGR (Blue, Green and Red) order by default.


image= cv2.imread('Test.jpg')
binary= grayScaleConversation(image)
Denoised= imageDenoising(binary)
#dst= correct_skew(image,Denoised)
#cornerDetection(image,Denoised)
segmentation(Denoised)
templateMatching()



# Finally, once the user pressed a key, we call the destroyAllWindows function,
# which will destroy the previously created windows.
cv2.waitKey(0)
cv2.destroyAllWindows()



