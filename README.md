Trying to get my Raspberry Pi 3 set up to serve as a Solaris 2.6 netboot server, so have to keep track of RARP, TFTP, and Bootparam settings. Set up a dead simple Flask app to serve some network config info.

Based on instructions foundd here: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

rpi_setup.service gets copied to /etc/systemd/system

`sudo cp rpi_setup.service /etc/systemd/system
sudo systemctl start rpi_setup
sudo systemctl enable rpi_setup`

