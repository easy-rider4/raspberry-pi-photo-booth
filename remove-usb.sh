#!/bin/bash

echo "removing usb device"
sudo umount /media/photobooth

echo "delete directory"
sudo rm -r /media/photobooth

