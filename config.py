#if true -> timestamp will be printed on the taken picture
TIMESTAMP = False


#the amount of pics that will be taken in one go
NUMBER_OF_PICTURES = 3


#the interval of the countdown
INTERVAL_IN_SECONDS = 3


# define the ratio of the picamera: default is monitor size and max is 2592,1944
RATIO_X = 1920
RATIO_Y = 1200


#example /media/<usbstick>/
USB_PATH = '/media/photobooth/';


#webserver - gallery directory
SAVE_TO_GALLERY = False
GALLERY_DIRECTORY = '/var/www/html/photo-booth/pictures/';


#will be shown as default background image when no pictures are taken
BACKGROUND_IMAGE = '/home/pi/raspberry-pi-photo-booth/images/photos.jpg'


#number of seconds the last taken picture is shown after capturing it
DISPLAY_TIME = 5


#the space between pics in a collage
COLLAGE_MARGIN = 20
