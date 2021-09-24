# virtual-pad-
## Our target is to create a virtual pad that moves or dawing same as user is drawing in front of a camera using a stylus as a drawing tool.
> ### So first we need to capture frame by frame images by camera.
> ### And than we converted normal BGR image into HSV image for color thersholding.
> ### We thresholded blue color of the stylus as we have considered that. 
> ### After thresholding we find contour of the image (Frame).
> ### It helps us to find centroid of the stylus .
> ### ussing centroid we created a pad in another frame that draws what actually we wanted.
### The same video link of the pad : 
https://user-images.githubusercontent.com/83019850/134730827-cd9480f8-a528-454e-8fa9-9213013e31ba.mp4
### It has a limitation that stylus must be of similar color as in the sample video. 
