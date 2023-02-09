import cv2
import numpy
import easygui

try:

    input("select png to extract red channel from (press enter to continue)")
    redPath = easygui.fileopenbox()
    input("select png to extract green channel from (press enter to continue)")
    greenPath = easygui.fileopenbox()
    input("select png to extract blue channel from (press enter to continue)")
    bluePath = easygui.fileopenbox()
    input("select save location; ensure that you save it with a .png extension (press enter to continue)")
    savePath = easygui.filesavebox()

    #read images
    red = cv2.imread(redPath, cv2.IMREAD_UNCHANGED)
    green = cv2.imread(greenPath, cv2.IMREAD_UNCHANGED)
    blue = cv2.imread(bluePath, cv2.IMREAD_UNCHANGED)

    if red.shape == green.shape and red.shape == blue.shape:
        

        redChannel = red[:,:,2]
        greenChannel = green[:,:,1]
        blueChannel = blue[:,:,0]

        output = numpy.zeros(red.shape)
        output[:,:,2] = redChannel
        output[:,:,1] = greenChannel
        output[:,:,0] = blueChannel

        cv2.imwrite(savePath, output)
    else:
        print("images need to all be the same resolution")
except:
    print("there was an error while processing the image file(s)")
    print("did you save the file with a .png extension?")
    input("press enter to close")