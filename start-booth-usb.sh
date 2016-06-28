#!/bin/bash

echo "clean up old entries"
sudo rm -r /media/photobooth

echo "remove usb - because of auto mount"
sudo umount /media/photobooth

echo "create directory"
sudo mkdir /media/photobooth

echo "mount usb with needed file permissions"
sudo mount /dev/sda1 /media/photobooth -o dmask=000,fmask=111,uid=pi,gid=pi

echo "start photo-booth"
sudo python photo-booth.py