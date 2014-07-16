videojsXblock
=========

XBlock to use the Video.js player (www.videojs.com) instead of the default one.

- True full screen allowed
- More video speeds available : | 0.75 | 1 | 1.25 | 1.5 | 1.75 | 2 | by default (and easy to customize)

### Installation / Updating ###
See https://github.com/polimediaupv/paellaXBlock installation

    # Move to the folder where you want to download the XBlock
    cd /edx/app/edxapp
    # Download the XBlock
    sudo -u edxapp git clone https://github.com/MarCnu/videojsXBlock.git
    # Install the script
    sudo -u edxapp /edx/bin/pip.edxapp install videojsXBlock/
    # Upgrade the script if it is already installed, using --upgrade
    sudo -u edxapp /edx/bin/pip.edxapp install videojsXBlock/ --upgrade
    # Remove the installation files
    sudo rm -r videojsXBlock

If necessary, try to reboot :
    sudo /edx/bin/supervisorctl -c /edx/etc/supervisord.conf restart edxapp:

Go to Settings -> Advanced Settings and set `advanced_modules` to `["videojs"]`.
