# ------------- IMPORTS 
import os, glob
import subprocess
import datetime
import sys
import time
import RPi.GPIO as GPIO
import picamera
import config
from PIL import Image


# -------------- set GPIO-Input
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # start taken pics
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # exit program


# -------------- functions
def generate_collage(files):
    images = map(Image.open, files)
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)
    margin = config.COLLAGE_MARGIN

    if (config.NUMBER_OF_PICTURES == 2):
        new_im = Image.new('RGB', (total_width + margin, max_height), (255,255,255))
        
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset = x_offset + im.size[0] + margin

        # save & display
        display_image(save_image(new_im))


    if (config.NUMBER_OF_PICTURES == 3):
        image_width = total_width/3*2 + margin
        image_height = max_height*2 + margin
        new_im = Image.new('RGB', (image_width, image_height), (255,255,255))
        
        x_offset = 0
        y_offset = 0
        counter = 1
        for im in images:
            if (counter == 3):
                x_offset = (image_width / 2) - (im.size[0] / 2)
                y_offset = max_height + margin
            new_im.paste(im, (x_offset, y_offset))
            x_offset = x_offset + im.size[0] + margin
            counter = counter + 1

        # save & display
        display_image(save_image(new_im))       

def save_taken_pics_to_usb(pictureList):
    countList = 0
    while (countList < len(pictureList)):
        currentImage = Image.open(pictureList[countList])

        newUsbImage = Image.new("RGB", (currentImage.size[0], currentImage.size[1]), "white")
        newUsbImage.paste(currentImage, (0,0))

        timestampAsString = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
        usbFileName = config.USB_PATH + '' + str(timestampAsString) + '.jpg'
        newUsbImage.save(usbFileName)

        countList = countList + 1

    
#returns filename collage
def save_image(new_im):
    timestampAsString = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')

    if (config.SAVE_TO_GALLERY):
        #webserver gallery enabled = true -> save to gallery
        collageFile = config.GALLERY_DIRECTORY + 'collage_' + str(timestampAsString) + '.jpg'
    else:
        #else -> save to local pictures directory
        collageFile = 'pictures/collage_' + str(timestampAsString) + '.jpg'
    new_im.save(collageFile)

    if (config.USB_PATH != ''):
        usbFile = config.USB_PATH + 'collage_' + str(timestampAsString) + '.jpg'
        new_im.save(usbFile)
        
    return collageFile


#displays one pic               
def display_image(dis_im):
    viewer = subprocess.Popen(['feh', '--fullscreen', dis_im])
    time.sleep(3);
    viewer.terminate()
    viewer.kill()           

    
#displays a list of pics
def display_taken_pics(takenPics):
    pictureList = []

    counter = 0
    while (counter < len(takenPics)):
        pictureList.append(subprocess.Popen(['feh', '--fullscreen', takenPics[counter]]))
        time.sleep(3)
        counter = counter + 1

    counter2 = 0
    while (counter2 < len(pictureList)):
        pictureList[counter2].terminate()
        pictureList[counter2].kill()
        counter2 = counter2 + 1



# -------------- script

print('Welcome to raspberry-pi-photo-booth')

# open background image
viewer = subprocess.Popen(['feh', '--fullscreen', config.BACKGROUND_IMAGE])


# wait for input 
while True:

    # ----- take normal pics
    if (GPIO.input(24) == False):

        # get pi camera
	camera = picamera.PiCamera()
	takenPics = []
        
        try:
            camera.resolution = (config.RATIO_X, config.RATIO_Y)
            camera.start_preview()

            #take x pics
            countPictures = 0
            while countPictures < config.NUMBER_OF_PICTURES:
                countPictures += 1

                #show countdown
                countSeconds = config.INTERVAL_IN_SECONDS + 1
                while countSeconds > 1:
                    countSeconds -= 1
                    camera.annotate_text = str(countSeconds)
                    time.sleep(1)

                #get current time as file name
                timestamp = time.time()
                timestampAsString = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S')

                #save pic with timestamp overlay
                if config.TIMESTAMP == True:
                    camera.annotate_text = str(timestampAsString)

                else:
                    camera.annotate_text = ' '

                #create file path
                if (config.SAVE_TO_GALLERY):
                    #webserver gallery enabled = true -> save to gallery
                    newFilePath = config.GALLERY_DIRECTORY + '' + str(timestampAsString) + '.jpg'
                else:
                    #else -> save to local pictures directory
                    newFilePath = 'pictures/' + str(timestampAsString) + '.jpg'


                #take picture
                camera.capture(newFilePath)
                takenPics.append(newFilePath)

                    
            #stop preview
            camera.stop_preview()
                
        finally:
            camera.close()


        #save pics to usb
        if (config.USB_PATH != ''):
            save_taken_pics_to_usb(takenPics)


        #display taken pictures
        display_taken_pics(takenPics)    


        #create collage
        #if(config.NUMBER_OF_PICTURES > 1):    
            #generate_collage(takenPics)
        #else:
            #display_image(takenPics[0])
        

    # ----- exit program
    if (GPIO.input(25) == False):
        print('Bye bye!')
        viewer.terminate()
	viewer.kill()
        exit()


    time.sleep(0.1);

    







    
