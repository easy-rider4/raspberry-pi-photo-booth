#if true -> timestamp will be printed on the taken picture
TIMESTAMP = False

#the amount of pics that will be taken in one go
NUMBER_OF_PICTURES = 3

#the interval of the countdown
INTERVAL_IN_SECONDS = 3

# define the ratio of the picamera
# default is monitor size; max is 2592,1944
RATIO_X = 1920
RATIO_Y = 1125

#example /media/<usbstick>/
USB_PATH = '';

#will be shown as default background image when no pictures are taken
#at the moment
BACKGROUND_IMAGE = '/home/pi/raspberry-pi-photo-booth/images/background1.jpg'


#set true if not only a collage should be created but also a
#stripe with the taken pictures for printing
PRINT = False # todo

#number of seconds the last taken picture is shown after capturing it
DISPLAY_TIME = 5


COLLAGE_MARGIN = 20
