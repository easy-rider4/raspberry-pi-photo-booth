# Photo-booth

This is the code for a Raspberry Pi photo-booth in python.

## Hardware
- Raspberry Pi 2 Model B
- Pi Camera V1
- Jump wires and buttons
- T-Cobbler for Raspberry Pi 2
- Breadboard
- Micro SD-Card
- active USB-Hub
- Wlan-adapter (EDIMAX)
- HDMI Display
- HDMI cable


## Software
- Raspbian
- Python
- picamera
- gpio
- Image (PIL)
- feh


## Installation
### OS
1. download and unzip lastest Raspbian (Jessie)
2. install Win32 disk manager (windows)
3. setup a mikro SD card with the OS

### Raspberry Pi - first system start
optional: I'm from germany, so I changed my key layout like this... Menu -> Preferences -> Mouse and Keyboard Settings - Keyboard Layout

```shell
sudo raspi-config
```

set these values:
* expand filesystem
* change password for user pi
* enable camera = true
* advanced options:
	* overscan: false
	* hostname: photobooth
	* ssh: true

then reboot the pi.

### Keep your Pi updated
```shell
sudo apt-get update
sudo apt-get upgrade
```
the upgrade will probably take a while, so lean back and wait...

### Install ftp server
The ftp server will allow you to better access the raspberry pi files and for example
copy the taken pictures to another computer.

These steps are from a tutorial: http://www.forum-raspberrypi.de/Thread-tutorial-raspberry-pi-als-webserver-ftp-server-proftpd-installation

1. `sudo apt-get install profited`
2. `sudo nano /etc/proftpd/proftpd.conf`
```
DefaultRoot ~
AuthOrder mod_auth_file.c mod_auth_unix.c
AuthUserFile /etc/proftpd/ftpd.passwd
AuthPAM off
RequireValidShell off
```
3. `cd /etc/proftpd/`
4. `sudo ftpasswd - -passwd - -name <name> - -uid 33 - -gid 33 - -home /var/www - -shell /bin/false`
5. `sudo /etc/init.d/proftpd restart`
6. `sudo chmod g+s /var/www`
7. `sudo chmod 775 /var/www`
8. `sudo chown -R www-data:www-data /var/www`

### Dependencies
1. python 
	* is preinstalled
2. RPi.GPIO 
	* is preinstalled on newer versions of raspbian e.g. jessie
3. picamera 
	* is also preinstalled on newer versions 
	* if not: `sudo apt-get install python-picamera or python3-picamera	`
4. Image (PIL)
	* `sudo apt-get install python-imaging`
	* http://chriskrz.selfhost.bz/index.php/image-manipulation-mit-pil-bilddateien-veraendern/
	* http://askubuntu.com/questions/156484/how-do-i-install-python-imaging-library-pil
	* Info: Here I got an error message myself, that It it could not install some package, but it works just fine for me.
5. feh
	* `sudo apt-get install feh`
	
### Clone this repository
`git clone https://github.com/easy-rider4/raspberry-pi-photo-booth.git`

### Display pictures in a gallery on a webserver
This part here is optional. You don't need to install the web gallery to run the script.

1. install apache2
	* `sudo apt-get install apache2`
2. install php5
	* `sudo apt-get install php5`
3. test server
	* `cd /var/www/html`
	* `sudo nano phpinfo.php`
	* `<?php phpinfo(); ?>`
	* strg+o
	* strg+x
	* find out your pis ip address with
 		* `ifconfig` or
 		* `sudo ip addr show`
	* open your browser and enter <ipaddress>/phpinfo.php
	* Info: somehow my default public directory is var/www/html, so I have everything in there
4. One page web gallery
	* by sye.dk/sfpg/
	* `cd /var/www/html`
	* `mkdir /var/www/html/photo-booth`
	* `sudo apt-get update`
	* `sudo apt-get -y install php5-gd`
	* `cd ~`
	* `wget http://sye.dk/sfpg/Single_File_PHP_Gallery_4.5.6.zip`
	* `unzip Single_File_PHP_Gallery_4.1.1.zip -d /var/www/html/photo-booth`
	* open browser: <ipaddress>/photo-booth
	
Info: you need to paste some pics into the directory to see the thumbnails

Info2: I somehow had problems to unzip the file, soo I did that on my Mac and copied the files via ftp to the raspberry pi

## Run
1. config.py
	* USB_PATH = set if usb-device is used for storage
	* NUMBER_OF_PICTURES = number of pictures that should be taken
	* INTERVAL_IN_SECONDS = length of the countdown between shooting pics
	* SAVE_TO_GALLERY = default value is false. Set to true if you installed the web gallery
	* GALLERY_DIRECTORY= change your directory to the web gallery here
2. if usb is used
	* format = FAT 
	* name = PHOTOBOOTH
3. make sure you are in the directory /home/pi/raspberry-pi-photo-booth/ and run
	* ./start-booth-usb.sh or
	* ./start-booth.sh
4. when finished run
	* ./remove-usb.sh

