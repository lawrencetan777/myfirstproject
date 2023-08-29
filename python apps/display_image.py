## [imports]
import cv2 as cv
import sys

## [imports]
## [imread]
img = cv.imread(cv.samples.findFile("\\Users\\lawrence\\Documents\\coding\\myfirstproject\\python apps\\tlozootendscreen.png" , 0))
## [imread]
## [empty]
if img is None:
    sys.exit("Could not read the image.")
## [empty]
## [imshow]
cv.imshow("Display window", img)
k = cv.waitKey(0)
## [imshow]
## [imsave]
if k == ord("s"):
    cv.imwrite("imagepants.jpg", img)
## [imsave]

