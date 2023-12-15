# rgbxmastree

Code to use with the [3D RGB Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi).

Also contains the code for sending a Telegram message to yourself via a bot as this is included in the script I use when starting up the tree. (Please note this will require setting up a bot on the Telegram platform and having the required information to insert into the code where specified)

Before starting this repository and my own approach to coding for the 3D RGB Xmas Tree, I downloaded the [official repository](https://github.com/ThePiHut/rgbxmastree/) made by [The Pi Hut](https://thepihut.com/).

After getting familiar with the layout of the tree and the [examples](https://github.com/ThePiHut/rgbxmastree/tree/master/examples) provided, I began looking around to see who else had made their own code.

Big thanks to [rgooding](https://github.com/rgooding/rgbxmastree) who's repo helped me rewrite the main tree.py file allowing me to further customise my code.

## Getting Started

I have ran (most of) this code on a Raspberry Pi Zero, Raspberry Pi Zero 2W, Raspberry Pi A+, and Raspberry Pi 5 (Running various versions of [Raspberry Pi OS](https://www.raspberrypi.com/software/) or [DietPi](https://dietpi.com)). It's no surprise to say it runs the smoothest on the Raspberry Pi 5. Most of the code does work on the earlier models, however the Zero and A+ models definitely struggled as the code became more advanced and a lot of the time just gave me random flashes of colour instead of the expected output. Since I won't need a Christmas tree up for long, I've decided to go with using it on the Raspberry Pi 5 so I can fully appreciate my code before moving my Pi5 on to bigger things :) 

When working on the earlier models of Raspberry Pi (0, 02w, A+) I needed to run the following commands to make sure I had the required packages installed and they were running:
sudo apt install python3-gpiozero python3-pigpio pigpio
sudo systemctl start pigpiod
sudo systemctl enable pigpiod  # to start pigpiod on boot

On the Raspberry Pi 5 however, this was not necessary as pigpio hasn't been updated yet to work with the Pi 5. I did follow the instructions on this website (https://abyz.me.uk/lg/download.html) to install an alternative, but I'm not sure if it actually did anything or if the required files were already installed as part of the Raspberry Pi OS.

## Running the code

Run the script:
python3 myTree.py

Install script to start on boot:
sudo cp tree.service /etc/systemd/system/
sudo systemctl enable tree.service
sudo systemctl start tree.service

## Notes

Most of this code was based on the examples found here https://github.com/ThePiHut/rgbxmastree/ and here https://github.com/rgooding/rgbxmastree.

The files in the 'originals' folder are copied directly from The Pi Hut's [repository](https://github.com/ThePiHut/rgbxmastree/).

I've also included my WIP (Work-In-Progress) folder mainly as a backup for myself, so please ignore the code in there if it makes absolutely no sense to you or wouldn't work in reality :D 
